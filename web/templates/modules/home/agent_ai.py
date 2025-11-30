from web.templates.base import get_base_template
from colors import get_css_variables, THEME_COLORS, PRIMARY_ACCENT

def generate_agent_page():
    # Ottieni le variabili CSS dalla nuova palette
    css_variables = get_css_variables()

    content = f"""
    <style>
        {css_variables}
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css'); /* For icons */

        :root {{
            --bg-primary: var(--color-bg-dark-900);
            --bg-secondary: var(--color-bg-dark-800);
            --bg-tertiary: var(--color-bg-dark-700);
            --text-primary: var(--color-text-light-100);
            --text-secondary: var(--color-text-light-200);
            --text-muted: var(--color-text-light-300);
            --accent-main: var(--color-accent-primary-500);
            --accent-hover: var(--color-accent-primary-400);
            --border-color: var(--color-border-dark);
            --border-light: var(--color-border-light);
            --success-color: var(--color-accent-success);
            --danger-color: var(--color-accent-danger);
        }}

        body {{
            margin: 0;
            padding: 0;
            background: var(--bg-primary);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        .chat-container {{
            display: flex;
            flex-direction: column;
            height: 100%;
            max-width: 900px;
            margin: 0 auto;
            width: 100%;
        }}

        .chat-header {{
            padding: 15px 20px;
            background: var(--bg-secondary);
            border-bottom: 1px solid var(--border-color);
            text-align: center;
            font-size: 1.1em;
            font-weight: 600;
            color: var(--text-primary);
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            position: relative;
            z-index: 10;
        }}

        .messages-container {{
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
            -ms-overflow-style: none;  /* IE and Edge */
            scrollbar-width: none;  /* Firefox */
        }}
        .messages-container::-webkit-scrollbar {{
            display: none; /* Chrome, Safari, Opera */
        }}

        .message-bubble {{
            max-width: 85%;
            padding: 12px 18px;
            border-radius: 20px;
            line-height: 1.5;
            font-size: 0.95em;
            animation: fadeIn 0.3s ease-out forwards;
            word-wrap: break-word; /* Ensure long words break */
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .message-user {{
            align-self: flex-end;
            background: var(--accent-main);
            color: white;
            border-bottom-right-radius: 4px;
        }}

        .message-assistant {{
            align-self: flex-start;
            background: var(--bg-tertiary);
            color: var(--text-primary);
            border-bottom-left-radius: 4px;
        }}

        .message-timestamp {{
            font-size: 0.75em;
            color: var(--text-muted);
            margin-top: 5px;
            text-align: right; /* For user messages */
        }}
        .message-assistant + .message-timestamp {{
            text-align: left;
        }}

        .input-area {{
            padding: 15px 20px;
            background: var(--bg-secondary);
            border-top: 1px solid var(--border-color);
            display: flex;
            align-items: flex-end;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
            position: relative;
            z-index: 10;
        }}

        #message-input {{
            flex: 1;
            background: var(--bg-tertiary);
            border: 1px solid var(--border-light);
            border-radius: 25px;
            padding: 12px 18px;
            color: var(--text-primary);
            font-size: 1em;
            outline: none;
            resize: none;
            min-height: 20px;
            max-height: 120px; /* Limit height for textarea */
            line-height: 1.4;
            transition: border-color 0.2s ease;
        }}

        #message-input::placeholder {{
            color: var(--text-muted);
        }}

        #message-input:focus {{
            border-color: var(--accent-main);
        }}

        .send-button {{
            background: var(--accent-main);
            color: white;
            border: none;
            border-radius: 50%;
            width: 44px;
            height: 44px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2em;
            margin-left: 10px;
            cursor: pointer;
            transition: background 0.2s ease, transform 0.2s ease;
            flex-shrink: 0; /* Prevent button from shrinking */
        }}

        .send-button:hover {{
            background: var(--accent-hover);
            transform: scale(1.05);
        }}

        .send-button:disabled {{
            background: var(--border-color);
            cursor: not-allowed;
            opacity: 0.6;
            transform: none;
        }}

        .status-indicator {{
            text-align: center;
            padding: 10px;
            font-size: 0.85em;
            color: var(--text-muted);
        }}
        .status-indicator.loading {{
            color: var(--accent-main);
        }}
        .status-indicator.error {{
            color: var(--danger-color);
        }}
    </style>

    <div class="chat-container">
        <div class="chat-header">Assistente AI</div>
        <div class="messages-container" id="messages-container">
            <div class="message-bubble message-assistant">
                Buongiorno! Sono il tuo assistente. Come posso aiutarti oggi?
            </div>
        </div>
        <div class="input-area">
            <textarea id="message-input" placeholder="Scrivi un messaggio..." rows="1"></textarea>
            <button id="send-button" class="send-button" disabled>
                <i class="fas fa-paper-plane"></i>
            </button>
        </div>
    </div>

    <script>
        const messageInput = document.getElementById('message-input');
        const sendButton = document.getElementById('send-button');
        const messagesContainer = document.getElementById('messages-container');

        const API_ENDPOINT = '/api/agent/chat'; // Define your API endpoint here

        function getCurrentTime() {{
            const now = new Date();
            return now.toLocaleTimeString('it-IT', {{ hour: '2-digit', minute: '2-digit' }});
        }}

        function addMessage(text, isUser = false) {{
            const messageWrapper = document.createElement('div');
            messageWrapper.className = `message-bubble ${isUser ? 'message-user' : 'message-assistant'}`;
            messageWrapper.innerHTML = text.replace(/\n/g, '<br>');

            const timestamp = document.createElement('div');
            timestamp.className = 'message-timestamp';
            timestamp.textContent = getCurrentTime();

            messagesContainer.appendChild(messageWrapper);
            messagesContainer.appendChild(timestamp);

            messagesContainer.scrollTop = messagesContainer.scrollHeight; // Scroll to bottom
        }}

        async function sendMessage() {{
            const text = messageInput.value.trim();
            if (!text) return;

            addMessage(text, true);
            messageInput.value = '';
            adjustTextareaHeight();
            sendButton.disabled = true; // Disable button after sending

            // Simulate haptic feedback if Telegram WebApp is available
            if (typeof Telegram !== 'undefined' && Telegram.WebApp) {{
                Telegram.WebApp.HapticFeedback.impactOccurred('light');
            }}

            try {{
                const response = await fetch(API_ENDPOINT, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ message: text }})
                }});

                if (!response.ok) {{
                    throw new Error(`HTTP error! status: ${{response.status}}`);
                }}

                const data = await response.json();
                addMessage(data.reply || "Mi dispiace, non sono riuscito a ottenere una risposta.");
            }} catch (error) {{
                console.error('Errore durante l'invio del messaggio:', error);
                addMessage("Si è verificato un errore. Riprova più tardi.", false);
            }} finally {{
                // Re-enable button if there's text in the input field
                sendButton.disabled = messageInput.value.trim().length === 0;
            }}
        }}

        function adjustTextareaHeight() {{
            messageInput.style.height = 'auto';
            messageInput.style.height = messageInput.scrollHeight + 'px';
        }}

        // Event Listeners
        messageInput.addEventListener('input', () => {{
            sendButton.disabled = messageInput.value.trim().length === 0;
            adjustTextareaHeight();
        }});

        messageInput.addEventListener('keydown', (e) => {{
            if (e.key === 'Enter' && !e.shiftKey) {{
                e.preventDefault(); // Prevent new line
                sendMessage();
            }}
        }});

        sendButton.addEventListener('click', sendMessage);

        // Initial setup
        document.addEventListener('DOMContentLoaded', () => {{
            if (typeof Telegram !== 'undefined' && Telegram.WebApp) {{
                Telegram.WebApp.ready();
                Telegram.WebApp.expand();
            }}
            messageInput.focus();
            adjustTextareaHeight(); // Adjust initial height
        }});
    </script>
    """
    return get_base_template("Assistente AI", content, "agent")
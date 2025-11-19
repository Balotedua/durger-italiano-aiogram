# web/templates/agent.py
from web.templates.base import get_base_template


def generate_agent_page():
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --bg: #000000;
            --text: #eeeeee;
            --text-muted: #888888;
            --gold: #D4AF37;
        }

        body {
            margin: 0;
            padding: 0;
            background: var(--bg);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px 20px 100px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            scrollbar-width: none;
        }
        .messages::-webkit-scrollbar { display: none; }

        .message {
            max-width: 82%;
            padding: 12px 18px;
            border-radius: 20px;
            line-height: 1.6;
            font-size: 15.5px;
            animation: fadeIn 0.4s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: none; }
        }

        .assistant {
            align-self: flex-start;
            background: #111111;
            border-bottom-left-radius: 4px;
            color: var(--text);
        }

        .user {
            align-self: flex-end;
            background: #222222;
            color: white;
            border-bottom-right-radius: 4px;
        }

        /* Input stile WhatsApp / ChatGPT pulitissimo */
        .input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 16px 20px 28px;
            background: var(--bg);
            border-top: 1px solid #111;
        }

        .input-wrapper {
            position: relative;
            max-width: 900px;
            margin: 0 auto;
        }

        #message-input {
            width: 100%;
            background: #111111;
            border: none;
            border-radius: 28px;
            padding: 16px 56px 16px 24px;
            color: white;
            font-size: 16px;
            outline: none;
            resize: none;
            min-height: 24px;
            max-height: 140px;
            line-height: 1.5;
        }

        #message-input::placeholder {
            color: #666;
        }

        #message-input:focus {
            background: #181818;
        }

        .send-btn {
            position: absolute;
            right: 8px;
            top: 10px;
            width: 44px;
            height: 44px;
            background: var(--gold);
            color: black;
            border: none;
            border-radius: 50%;
            font-size: 18px;
            opacity: 0;
            transform: scale(0.8);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .send-btn.visible {
            opacity: 1;
            transform: scale(1);
        }

        /* Stelle cadenti sottilissime - 90% bianche, 10% oro */
        .star {
            position: fixed;
            pointer-events: none;
            background: white;
            border-radius: 50%;
            opacity: 0;
            animation: shooting linear infinite;
        }

        .star.gold { background: var(--gold); box-shadow: 0 0 12px var(--gold); }

        @keyframes shooting {
            0%   { opacity: 0; transform: translateY(100vh) translateX(-50px) rotate(30deg); }
            4%   { opacity: 0.7; }
            15%  { opacity: 0.3; }
            100% { opacity: 0; transform: translateY(-200px) translateX(400px) rotate(30deg); }
        }
    </style>

    <div class="messages" id="messages">
        <div class="message assistant">
            Buongiorno.<br><br>
            Sono il tuo assistente.<br>
            Come posso aiutarti?
        </div>
    </div>

    <div class="input-container">
        <div class="input-wrapper">
            <textarea id="message-input" placeholder="Scrivi un messaggio..." rows="1"></textarea>
            <button class="send-btn" id="send-btn">↑</button>
        </div>
    </div>

    <script>
        // Stelle cadenti sottili e rare
        setInterval(() => {
            if (Math.random() < 0.25) {  // circa 1 ogni 4-5 secondi
                const star = document.createElement('div');
                star.className = 'star';
                if (Math.random() < 0.1) star.classList.add('gold');

                const size = Math.random() * 2.5 + 0.8;
                star.style.width = size + 'px';
                star.style.height = size + 'px';
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 30 + '%';
                star.style.animationDuration = (Math.random() * 8 + 8) + 's';
                star.style.animationDelay = Math.random() * 3 + 's';

                document.body.appendChild(star);
                setTimeout(() => star.remove(), 20000);
            }
        }, 1200);

        const input = document.getElementById('message-input');
        const sendBtn = document.getElementById('send-btn');
        const messages = document.getElementById('messages');

        function add(text, isUser = false) {
            const div = document.createElement('div');
            div.className = `message ${isUser ? 'user' : 'assistant'}`;
            div.innerHTML = text.replace(/\\n/g, '<br>');
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }

        async function send() {
            let text = input.value.trim();
            if (!text) return;

            add(text, true);
            input.value = '';
            sendBtn.classList.remove('visible');
            adjustHeight();
            Telegram.WebApp.HapticFeedback.impactOccurred('light');

            const res = await fetch('/api/agent/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: text})
            });
            const data = await res.json();
            add(data.reply || "Nessuna risposta.");
        }

        // Pulsante appare solo quando c'è testo
        input.addEventListener('input', () => {
            sendBtn.classList.toggle('visible', input.value.trim().length > 0);
            adjustHeight();
        });

        function adjustHeight() {
            input.style.height = 'auto';
            input.style.height = input.scrollHeight + 'px';
        }

        input.addEventListener('keydown', e => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                send();
            }
        });

        sendBtn.addEventListener('click', send);
        input.focus();
    </script>
    """
    return get_base_template("Assistant", content, "agent")
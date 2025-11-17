# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """Concierge AI • Black & Gold • 2025 Premium Chat"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-light: #E8C867;
            --black: #000000;
            --dark: #0D0D0D;
            --gray: #1A1A1A;
        }

        body {
            margin: 0;
            background: var(--black);
            color: white;
            font-family: 'Inter', sans-serif;
            height: 100vh;
            height: calc(var(--vh, 1vh) * 100);
            display: flex;
            flex-direction: column;
        }

        /* Header sottile ma elegante */
        header {
            text-align: center;
            padding: 40px 20px 20px;
            flex-shrink: 0;
        }

        .logo {
            width: 72px; height: 72px;
            margin: 0 auto 16px;
            background: radial-gradient(circle, var(--gold) 10%, transparent 60%);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 32px;
            box-shadow: 0 0 40px rgba(212,175,55,0.3);
        }

        h1 {
            font-size: 28px;
            font-weight: 700;
            background: linear-gradient(90deg, #F4E5B2, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
        }

        .tagline {
            font-size: 14px;
            color: rgba(212,175,55,0.8);
            margin-top: 6px;
            letter-spacing: 1px;
        }

        /* Area messaggi - come ChatGPT */
        #messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            max-width: 800px;
            margin: 0 auto;
            width: 100%;
        }

        .message {
            max-width: 80%;
            padding: 14px 20px;
            border-radius: 18px;
            font-size: 16px;
            line-height: 1.55;
            animation: fadeIn 0.4s ease;
            position: relative;
        }

        .message.user {
            align-self: flex-end;
            background: linear-gradient(135deg, var(--gold), #B8973A);
            color: black;
            font-weight: 500;
            border-bottom-right-radius: 4px;
        }

        .message.bot {
            align-self: flex-start;
            background: var(--gray);
            color: #eee;
            border: 1px solid rgba(212,175,55,0.15);
            border-bottom-left-radius: 4px;
        }

        .message.bot::before {
            content: '◆';
            position: absolute;
            top: -8px;
            left: 14px;
            color: var(--gold);
            font-size: 16px;
        }

        /* Input fisso in basso - PERFETTO su Telegram */
        .input-container {
            padding: 16px 20px 28px;
            background: var(--black);
            border-top: 1px solid rgba(212,175,55,0.1);
            flex-shrink: 0;
        }

        .input-wrapper {
            max-width: 800px;
            margin: 0 auto;
            position: relative;
        }

        #messageInput {
            width: 100%;
            padding: 16px 60px 16px 20px;
            background: rgba(30,30,30,0.95);
            border: 1.5px solid rgba(212,175,55,0.25);
            border-radius: 24px;
            color: white;
            font-size: 16.5px;
            outline: none;
            backdrop-filter: blur(10px);
            transition: all 0.3s;
        }

        #messageInput:focus {
            border-color: var(--gold);
            box-shadow: 0 0 30px rgba(212,175,55,0.25);
        }

        #messageInput::placeholder {
            color: rgba(212,175,55,0.5);
        }

        .send-btn {
            position: absolute;
            right: 8px;
            top: 8px;
            width: 44px; height: 44px;
            border-radius: 50%;
            background: var(--gold);
            border: none;
            color: black;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
        }

        .send-btn:active {
            transform: scale(0.9);
        }

        /* Typing */
        #typing {
            display: none;
            align-self: flex-start;
        }
        #typing.active { display: block; }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: none; }
        }
    </style>

    <header>
        <div class="logo">◆</div>
        <h1>Concierge AI</h1>
        <div class="tagline">Il tuo assistente privato premium</div>
    </header>

    <div id="messages">
        <div class="message bot">
            Buongiorno.<br>Sono il tuo Concierge AI. Come posso aiutarti oggi?
        </div>
    </div>

    <div id="typing" class="message bot">
        <span style="display:inline-flex;gap:6px;">
            <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:bounce 1.4s infinite;"></span>
            <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:bounce 1.4s infinite 0.2s;"></span>
            <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:bounce 1.4s infinite 0.4s;"></span>
        </span>
    </div>

    <div class="input-container">
        <div class="input-wrapper">
            <input 
                type="text" 
                id="messageInput" 
                placeholder="Scrivi un messaggio..." 
                autocomplete="off"
                onkeypress="if(event.key==='Enter' && !event.shiftKey){event.preventDefault();sendMessage();}"
            >
            <button class="send-btn" onclick="sendMessage()">→</button>
        </div>
    </div>

    <script>
        function addMessage(text, isUser = false) {
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'bot');
            div.innerHTML = text.replace(/\\n/g, '<br>');
            document.getElementById('messages').appendChild(div);
            window.scrollTo(0, document.body.scrollHeight);
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const text = input.value.trim();
            if (!text) return;

            addMessage(text, true);
            input.value = '';
            document.getElementById('typing').classList.add('active');

            Telegram.WebApp.HapticFeedback.impactOccurred('light');

            setTimeout(() => {
                document.getElementById('typing').classList.remove('active');
                addMessage("Perfetto. Sto preparando una risposta personalizzata per te...");
            }, 1000 + Math.random() * 1500);
        }

        // Fix altezza mobile
        let vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
        window.addEventListener('resize', () => {
            vh = window.innerHeight * 0.01;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        });
    </script>

    <style>
        @keyframes bounce {
            0%,100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
    """
    return get_base_template("Concierge AI", content, "agent")
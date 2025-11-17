# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """Concierge AI • Black & Gold • 2025 Ultra Premium (Telegram-safe)"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --gold: #C9A96A;     /* Oro elegante, non giallo */
            --black: #000000;
            --dark: #0D0D0D;
            --msg-bg: #111111;
        }

        * { margin:0; padding:0; box-sizing:border-box; }
        html, body {
            height: 100%;
            background: var(--black);
            color: white;
            font-family: 'Inter', sans-serif;
            overscroll-behavior: none;
        }

        .app {
            display: flex;
            flex-direction: column;
            height: 100%;
            padding-bottom: env(safe-area-inset-bottom, 0px);
        }

        /* Header minimal */
        header {
            padding: 50px 24px 20px;
            text-align: center;
        }
        .logo {
            width: 64px; height: 64px;
            margin: 0 auto 16px;
            background: radial-gradient(circle at 30% 30%, var(--gold) 0%, transparent 65%);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 30px;
        }
        h1 {
            font-size: 28px; font-weight: 700; margin: 0;
            background: linear-gradient(90deg, #E8DAB2, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .tag { font-size: 13px; color: var(--gold); margin-top: 6px; letter-spacing: 1.8px; }

        /* Messaggi stile ChatGPT Pro */
        #messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px 24px 100px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .message {
            max-width: 100%;
            padding: 16px 20px;
            border-radius: 12px;
            font-size: 16px;
            line-height: 1.55;
            animation: fade 0.4s ease;
        }

        .message.user {
            align-self: flex-end;
            background: var(--msg-bg);
            border: 1.5px solid var(--gold);
            color: white;
            max-width: 85%;
        }

        .message.bot {
            align-self: flex-start;
            background: var(--msg-bg);
            border: 1px solid rgba(201,169,106,0.25);
            color: #eee;
            max-width: 92%;
        }

        /* Input che NON viene mai coperto */
        .input-container {
            position: fixed;
            bottom: 0; left: 0; right: 0;
            padding: 16px 20px;
            padding-bottom: max(20px, env(safe-area-inset-bottom));
            background: var(--black);
            border-top: 1px solid rgba(201,169,106,0.15);
            z-index: 1000;
        }

        .input-box {
            max-width: 900px;
            margin: 0 auto;
            position: relative;
        }

        #input {
            width: 100%;
            padding: 16px 60px 16px 20px;
            background: #0A0A0A;
            border: 1.5px solid rgba(201,169,106,0.4);
            border-radius: 16px;
            color: white;
            font-size: 16.5px;
            font-family: inherit;
            outline: none;
            resize: none;
            min-height: 56px;
            max-height: 140px;
            field-sizing: content;
        }

        #input:focus {
            border-color: var(--gold);
            box-shadow: 0 0 0 4px rgba(201,169,106,0.15);
        }

        #input::placeholder {
            color: rgba(201,169,106,0.5);
        }

        .send-btn {
            position: absolute;
            right: 10px;
            top: 10px;
            width: 42px; height: 42px;
            border-radius: 50%;
            background: var(--gold);
            border: none;
            color: black;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Typing indicator */
        #typing {
            display: none;
            padding: 16px 20px;
            background: var(--msg-bg);
            border: 1px solid rgba(201,169,106,0.25);
            border-radius: 12px;
            align-self: flex-start;
            max-width: 92%;
        }
        #typing.active { display: block; }

        @keyframes fade { from { opacity:0; transform:translateY(8px); } }
    </style>

    <div class="app">
        <header>
            <div class="logo">◆</div>
            <h1>Concierge</h1>
            <div class="tag">ASSISTENTE PRIVATO</div>
        </header>

        <div id="messages">
            <div class="message bot">
                Buongiorno.<br>
                Sono il tuo assistente personale privato.<br>
                Come posso esserle utile oggi?
            </div>
        </div>

        <div id="typing">
            <span style="display:inline-flex;gap:8px;">
                <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite;"></span>
                <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite .2s;"></span>
                <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite .4s;"></span>
            </span>
        </div>

        <div class="input-container">
            <div class="input-box">
                <textarea id="input" placeholder="Scrivi qui..." rows="1"></textarea>
                <button class="send-btn" onclick="send()">→</button>
            </div>
        </div>
    </div>

    <script>
        const messages = document.getElementById('messages');
        const input = document.getElementById('input');
        const typing = document.getElementById('typing');

        function add(text, user = false) {
            const div = document.createElement('div');
            div.className = 'message ' + (user ? 'user' : 'bot');
            div.innerHTML = text.replace(/\\n/g, '<br>');
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }

        function send() {
            const text = input.value.trim();
            if (!text) return;

            add(text, true);
            input.value = '';
            input.style.height = 'auto';
            typing.classList.add('active');
            Telegram.WebApp.HapticFeedback.impactOccurred('medium');

            setTimeout(() => {
                typing.classList.remove('active');
                add("Perfetto. Sto elaborando la sua richiesta con la massima cura.");
            }, 1000 + Math.random() * 1200);
        }

        input.addEventListener('keydown', e => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                send();
            }
        });

        input.addEventListener('input', () => {
            input.style.height = 'auto';
            input.style.height = input.scrollHeight + 'px';
        });
    </script>

    <style>
        @keyframes b { 0%,100% {transform:translateY(0)} 50% {transform:translateY(-10px)} }
        textarea { field-sizing: content; }
    </style>
    """
    return get_base_template("Concierge", content, "agent")
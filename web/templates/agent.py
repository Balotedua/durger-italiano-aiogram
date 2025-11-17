# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """Concierge AI • Black & Gold • Telegram-Safe Premium Chat"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        :root {
            --gold: #D4AF37;
            --black: #000000;
            --dark: #0F0F0F;
            --gray: #1C1C1C;
        }

        html, body {
            margin: 0; padding: 0; height: 100%; background: var(--black);
            font-family: 'Inter', sans-serif; color: white;
            overscroll-behavior: none;
        }

        .container {
            display: flex;
            flex-direction: column;
            height: 100%;
            padding-bottom: env(safe-area-inset-bottom, 20px); /* <-- CRITICO per Telegram */
        }

        /* Header pulito */
        header {
            padding: 50px 20px 10px;
            text-align: center;
            flex-shrink: 0;
        }
        .logo {
            width: 68px; height: 68px; margin: 0 auto 14px;
            background: radial-gradient(circle at 30% 30%, var(--gold) 0%, transparent 70%);
            border-radius: 50%; display: flex;
            align-items: center; justify-content: center; font-size: 32px;
        }
        h1 {
            font-size: 26px; font-weight: 700; margin: 0;
            background: linear-gradient(90deg, #F4E5B2, var(--gold));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .subtitle {
            font-size: 13px; color: #B8973A; margin-top: 6px; letter-spacing: 1.5px;
        }

        /* Messaggi */
        #messages {
            flex: 1; overflow-y: auto; padding: 20px; 
            display: flex; flex-direction: column; gap: 18px;
            -webkit-overflow-scrolling: touch;
        }
        .message {
            max-width: 82%; padding: 14px 18px; border-radius: 20px;
            font-size: 15.8px; line-height: 1.55; word-wrap: break-word;
            animation: fade 0.4s ease;
        }
        .message.user {
            align-self: flex-end;
            background: linear-gradient(135deg, var(--gold), #B8973A);
            color: black; font-weight: 500;
            border-bottom-right-radius: 4px;
        }
        .message.bot {
            align-self: flex-start;
            background: var(--gray);
            color: #ddd;
            border: 1px solid rgba(212,175,55,0.18);
            border-bottom-left-radius: 4px;
        }

        /* Input fisso in basso - Telegram safe */
        .input-area {
            padding: 12px 20px 20px;
            background: var(--black);
            border-top: 1px solid rgba(212,175,55,0.12);
        }
        .input-wrapper {
            position: relative; max-width: 100%;
        }
        #messageInput {
            width: 100%; padding: 16px 60px 16px 20px;
            background: #1A1A1A; border: 1.5px solid rgba(212,175,55,0.3);
            border-radius: 24px; color: white; font-size: 16px;
            outline: none; resize: none;
        }
        #messageInput:focus {
            border-color: var(--gold);
            box-shadow: 0 0 30px rgba(212,175,55,0.25);
        }
        #messageInput::placeholder { color: rgba(212,175,55,0.5); }

        .send {
            position: absolute; right: 8px; top: 8px;
            width: 44px; height: 44px; border-radius: 50%;
            background: var(--gold); border: none; color: black;
            font-size: 19px; cursor: pointer;
        }

        /* Typing */
        #typing {
            display: none; align-self: flex-start;
            padding: 14px 18px; background: var(--gray);
            border-radius: 20px; border-bottom-left-radius: 4px;
            border: 1px solid rgba(212,175,55,0.18);
        }
        #typing.active { display: block; }

        @keyframes fade { from { opacity:0; transform:translateY(10px); } }
    </style>

    <div class="container">
        <header>
            <div class="logo">◆</div>
            <h1>Concierge AI</h1>
            <div class="subtitle">Assistente privato premium</div>
        </header>

        <div id="messages">
            <div class="message bot">
                Buongiorno.<br>Sono il tuo assistente personale. In cosa posso aiutarti?
            </div>
        </div>

        <div id="typing">
            <span style="display:inline-flex;gap:7px;">
                <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite;"></span>
                <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite .2s;"></span>
                <span style="width:8px;height:8px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite .4s;"></span>
            </span>
        </div>

        <div class="input-area">
            <div class="input-wrapper">
                <textarea id="messageInput" rows="1" placeholder="Scrivi un messaggio..." 
                          onkeypress="if(event.key==='Enter' && !event.shiftKey){event.preventDefault();send();}"></textarea>
                <button class="send" onclick="send()">→</button>
            </div>
        </div>
    </div>

    <script>
        const msg = document.getElementById('messages');
        const input = document.getElementById('messageInput');
        const typing = document.getElementById('typing');

        function add(text, user=false) {
            const div = document.createElement('div');
            div.className = 'message ' + (user?'user':'bot');
            div.innerHTML = text.replace(/\\n/g,'<br>');
            msg.appendChild(div);
            msg.scrollTop = msg.scrollHeight;
        }

        function send() {
            const text = input.value.trim();
            if (!text) return;
            add(text, true);
            input.value = '';
            typing.classList.add('active');
            Telegram.WebApp.HapticFeedback.impactOccurred('light');

            setTimeout(() => {
                typing.classList.remove('active');
                add("Perfetto. Sto preparando la risposta su misura per te...");
            }, 1200 + Math.random()*1000);
        }

        // Auto-resize textarea
        input.addEventListener('input', () => {
            input.style.height = 'auto';
            input.style.height = input.scrollHeight + 'px';
        });

        // Enter = invia, Shift+Enter = a capo
        input.addEventListener('keydown', e => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                send();
            }
        });
    </script>

    <style>
        @keyframes b { 0%,100% {transform:translateY(0)} 50% {transform:translateY(-10px)} }
        textarea { field-sizing: content; max-height: 120px; }
    </style>
    """
    return get_base_template("Concierge AI", content, "agent")
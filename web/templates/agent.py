# web/templates/agent.py - AI Assistant
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """AI Concierge – DURGER KING  Style – FINAL FIX (2025)"""
    content = """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-light: #F4E5B2;
            --gold-dark: #9B7F1B;
            --black: #0A0A0A;
            --black-light: #1A1A1A;
        }

        * { margin:0; padding:0; box-sizing:border-box; }
        html, body {
            height: 100dvh;
            background: var(--black);
            color: white;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
        }

        .app {
            display: flex;
            flex-direction: column;
            height: 100dvh;
            padding-bottom: env(safe-area-inset-bottom, 10px);
        }

        /* HEADER COMPATTO – solo 120px max */
        .header {
            padding: 28px 20px 16px;
            text-align: center;
            flex-shrink: 0;
        }
        .logo-icon { 
            font-size: 48px; 
            filter: drop-shadow(0 6px 16px rgba(212,175,55,0.4)); 
            animation: float 6s ease-in-out infinite; 
            margin-bottom: 8px;
        }
        .title { 
            font-family: 'Playfair Display', serif; 
            font-size: 32px; 
            font-weight: 900;
            background: linear-gradient(135deg, var(--gold-light), var(--gold), var(--gold-dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.8px;
        }
        .subtitle { 
            font-size: 12px; 
            color: var(--gold-light); 
            letter-spacing: 3.5px; 
            text-transform: uppercase; 
            opacity: 0.9;
        }

        /* MESSAGGI – area grande, scroll perfetta */
        #chat {
            flex: 1;
            overflow-y: auto;
            padding: 0 20px 20px;
            display: flex;
            flex-direction: column;
            gap: 18px;
            -webkit-overflow-scrolling: touch;
        }

        .message {
            max-width: 84%;
            padding: 16px 22px;
            border-radius: 20px;
            font-size: 15.5px;
            line-height: 1.58;
            animation: fadeInUp 0.4s ease backwards;
        }
        .message.bot {
            align-self: flex-start;
            background: var(--black-light);
            border: 1px solid rgba(212,175,55,0.25);
            color: #eee;
        }
        .message.user {
            align-self: flex-end;
            background: linear-gradient(135deg, var(--gold-dark), var(--gold));
            color: #000;
            font-weight: 600;
            box-shadow: 0 8px 24px rgba(212,175,55,0.3);
        }

        /* INPUT – sempre visibile, mai coperto */
        .input-area {
            padding: 14px 20px 20px;
            background: var(--black);
            border-top: 1px solid rgba(212,175,55,0.15);
            flex-shrink: 0;
        }

        .input-box {
            position: relative;
        }

        #input {
            width: 100%;
            padding: 16px 68px 16px 22px;
            background: var(--black-light);
            border: 1.5px solid rgba(212,175,55,0.3);
            border-radius: 24px;
            color: white;
            font-size: 16px;
            outline: none;
            resize: none;
            min-height: 58px;
            max-height: 130px;
            font-family: inherit;
        }

        #input:focus {
            border-color: var(--gold);
            box-shadow: 0 0 35px rgba(212,175,55,0.22);
        }

        #input::placeholder { color: rgba(212,175,55,0.5); }

        .send-btn {
            position: absolute;
            right: 10px;
            top: 9px;
            width: 46px; height: 46px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--gold), var(--gold-dark));
            border: none;
            color: #000;
            font-size: 19px;
            cursor: pointer;
            box-shadow: 0 5px 18px rgba(212,175,55,0.4);
        }

        .send-btn:active { transform: scale(0.9); }

        /* Typing */
        #typing {
            display: none;
            align-self: flex-start;
        }
        #typing.active { display: block; }

        @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }
        @keyframes fadeInUp { from{opacity:0;transform:translateY(15px)} to{opacity:1;transform:none} }
    </style>

    <div class="app">
        <div class="header">
            <div class="logo-icon">AI</div>
            <h1 class="title">AI Concierge</h1>
            <div class="subtitle"> Assistant</div>
        </div>

        <div id="chat">
            <div class="message bot">
                Buongiorno.<br>
                Sono il suo assistente personale.<br>
                Come posso servirla oggi?
            </div>
        </div>

        <div id="typing" class="message bot">
            <div style="display:inline-flex;gap:8px;">
                <div style="width:9px;height:9px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite;"></div>
                <div style="width:9px;height:9px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite .2s;"></div>
                <div style="width:9px;height:9px;background:var(--gold);border-radius:50%;animation:b 1.4s infinite .4s;"></div>
            </div>
        </div>

        <div class="input-area">
            <div class="input-box">
                <textarea id="input" placeholder="Scrivi qui..." rows="1"></textarea>
                <button class="send-btn" onclick="send()">Send</button>
            </div>
        </div>
    </div>

    <script>
        const chat   = document.getElementById('chat');
        const input  = document.getElementById('input');
        const typing = document.getElementById('typing');

        function scrollToBottom() {
            chat.scrollTop = chat.scrollHeight;
        }

        function send() {
            const text = input.value.trim();
            if (!text) return;

            const msg = document.createElement('div');
            msg.className = 'message user';
            msg.innerHTML = text.replace(/\\n/g, '<br>');
            chat.appendChild(msg);

            input.value = '';
            input.style.height = '58px';
            typing.classList.add('active');
            Telegram.WebApp.HapticFeedback.impactOccurred('heavy');
            scrollToBottom();

            setTimeout(() => {
                typing.classList.remove('active');
                const bot = document.createElement('div');
                bot.className = 'message bot';
                bot.innerHTML = 'Perfetto. Sto elaborando la sua richiesta con la massima cura.';
                chat.appendChild(bot);
                scrollToBottom();
            }, 1200 + Math.random() * 1000);
        }

        input.addEventListener('input', () => {
            input.style.height = 'auto';
            input.style.height = (input.scrollHeight) + 'px';
        });

        input.addEventListener('focus', () => {
            setTimeout(scrollToBottom, 300);
        });

        input.addEventListener('keydown', e => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                send();
            }
        });

        // Animazione puntini
        const s = document.createElement('style');
        s.textContent = `@keyframes b {0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}`;
        document.head.appendChild(s);

        // Scroll iniziale
        scrollToBottom();
    </script>
    """
    return get_base_template("AI Concierge", content, "agent")
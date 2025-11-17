# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """AI Concierge – Stile DURGER KING Premium + Input 100% visibile (Telegram-safe 2025)"""
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
            height: 100%;
            height: 100dvh;            /* <-- fondamentale 2025 */
            background: var(--black);
            color: white;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
        }

        .app {
            display: flex;
            flex-direction: column;
            height: 100dvh;
            padding-bottom: env(safe-area-inset-bottom, 20px);
        }

        /* Header */
        .header {
            text-align: center;
            padding: 60px 20px 30px;
            flex-shrink: 0;
        }
        .logo-icon { font-size:68px; filter:drop-shadow(0 8px 24px rgba(212,175,55,0.4)); animation:float 6s ease-in-out infinite; margin-bottom:16px; }
        .title { font-family:'Playfair Display',serif; font-size:40px; font-weight:900;
                 background:linear-gradient(135deg,var(--gold-light),var(--gold),var(--gold-dark));
                 -webkit-background-clip:text; -webkit-text-fill-color:transparent; letter-spacing:-1px; }
        .subtitle { font-size:14px; color:var(--gold-light); letter-spacing:4px; text-transform:uppercase; margin-top:8px; }
        .divider { width:60px; height:2px; background:linear-gradient(90deg,transparent,var(--gold),transparent); margin:30px auto 0; }

        /* Messaggi */
        #messages {
            flex: 1;
            overflow-y: auto;
            padding: 0 20px 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            scroll-behavior: smooth;
        }

        .message {
            max-width: 85%;
            padding: 18px 24px;
            border-radius: 20px;
            font-size: 15.5px;
            line-height: 1.6;
            animation: fadeInUp 0.5s ease backwards;
        }
        .message.bot  { align-self:flex-start; background:var(--black-light); border:1px solid rgba(212,175,55,0.25); color:#eee; }
        .message.user { align-self:flex-end; background:linear-gradient(135deg,var(--gold-dark),var(--gold)); color:#000; font-weight:600; box-shadow:0 10px 30px rgba(212,175,55,0.3); }

        /* Input container – la magia è qui */
        .input-wrapper {
            padding: 16px 20px;
            background: var(--black);
            border-top: 1px solid rgba(212,175,55,0.15);
            position: sticky;
            bottom: 0;
            width: 100%;
            z-index: 10;
        }

        .input-box {
            position: relative;
            max-width: 100%;
        }

        #input {
            width: 100%;
            padding: 18px 70px 18px 24px;
            background: var(--black-light);
            border: 1.5px solid rgba(212,175,55,0.3);
            border-radius: 24px;
            color: white;
            font-size: 16px;
            outline: none;
            resize: none;
            min-height: 62px;
            max-height: 140px;
            font-family: inherit;
        }

        #input:focus {
            border-color: var(--gold);
            box-shadow: 0 0 40px rgba(212,175,55,0.2);
        }

        #input::placeholder { color: rgba(212,175,55,0.5); }

        .send-btn {
            position: absolute;
            right: 10px; top: 10px;
            width: 48px; height: 48px;
            border-radius: 50%;
            background: linear-gradient(135deg,var(--gold),var(--gold-dark));
            border: none; color: #000; font-size: 20px;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(212,175,55,0.4);
        }

        .send-btn:active { transform: scale(0.92); }

        /* Typing */
        #typing { display:none; align-self:flex-start; }
        #typing.active { display:block; }

        @keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
        @keyframes fadeInUp { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:none} }
    </style>

    <div class="app">
        <div class="header">
            <div class="logo-icon">AI</div>
            <h1 class="title">AI Concierge</h1>
            <div class="subtitle">Premium Assistant</div>
            <div class="divider"></div>
        </div>

        <div id="messages">
            <div class="message bot">
                Buongiorno.<br>
                Sono il tuo assistente personale premium.<br>
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

        <div class="input-wrapper">
            <div class="input-box">
                <textarea id="input" placeholder="Il suo desiderio..." rows="1"></textarea>
                <button class="send-btn" onclick="send()">Send</button>
            </div>
        </div>
    </div>

    <script>
        const messages = document.getElementById('messages');
        const input    = document.getElementById('input');
        const typing   = document.getElementById('typing');

        // Auto-resize + scroll quando tastiera si apre
        input.addEventListener('input', () => {
            input.style.height = 'auto';
            input.style.height = input.scrollHeight + 'px';
        });

        input.addEventListener('focus', () => {
            setTimeout(() => {
                messages.scrollTop = messages.scrollHeight;
            }, 300);
        });

        function send() {
            const text = input.value.trim();
            if (!text) return;

            const div = document.createElement('div');
            div.className = 'message user';
            div.innerHTML = text.replace(/\\n/g, '<br>');
            messages.appendChild(div);

            input.value = '';
            input.style.height = 'auto';
            typing.classList.add('active');
            Telegram.WebApp.HapticFeedback.impactOccurred('heavy');

            messages.scrollTop = messages.scrollHeight;

            setTimeout(() => {
                typing.classList.remove('active');
                const bot = document.createElement('div');
                bot.className = 'message bot';
                bot.innerHTML = 'Perfetto. Sto preparando una risposta su misura per lei...';
                messages.appendChild(bot);
                messages.scrollTop = messages.scrollHeight;
            }, 1200 + Math.random()*1000);
        }

        input.addEventListener('keydown', e => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                send();
            }
        });

        // Animazione puntini typing
        const style = document.createElement('style');
        style.textContent = `@keyframes b {0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}`;
        document.head.appendChild(style);
    </script>
    """
    return get_base_template("AI Concierge", content, "agent")
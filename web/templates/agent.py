# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """Concierge AI • Ultra Luxury Premium • Deep Black & 18K Gold"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-light: #F4E5B2;
            --gold-dark: #B8973A;
            --black: #000000;
            --dark: #0A0A0A;
            --darker: #050505;
            --deep-black: #000000;
        }

        * { 
            margin: 0; 
            padding: 0; 
            box-sizing: border-box; 
        }

        body { 
            background: var(--deep-black); 
            color: white; 
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
            min-height: calc(var(--vh, 1vh) * 100);
            overflow-x: hidden;
            background: linear-gradient(135deg, #000000 0%, #0A0A0A 50%, #000000 100%);
            position: relative;
        }

        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 80%, rgba(212, 175, 55, 0.03) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(212, 175, 55, 0.02) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(212, 175, 55, 0.01) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
        }

        /* Header ultra luxury */
        .header {
            text-align: center;
            padding: 50px 20px 30px;
            position: relative;
            border-bottom: 1px solid rgba(212, 175, 55, 0.1);
            background: linear-gradient(to bottom, rgba(0,0,0,0.9) 0%, transparent 100%);
            backdrop-filter: blur(20px);
        }

        .logo-container {
            position: relative;
            width: 100px;
            height: 100px;
            margin: 0 auto 25px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .logo-glow {
            position: absolute;
            width: 120%;
            height: 120%;
            background: radial-gradient(circle, var(--gold) 0%, transparent 70%);
            opacity: 0.1;
            filter: blur(15px);
            animation: glowPulse 4s ease-in-out infinite;
        }

        .logo {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            position: relative;
            z-index: 2;
            box-shadow: 
                0 0 30px rgba(212, 175, 55, 0.4),
                inset 0 1px 0 rgba(255,255,255,0.2),
                inset 0 -1px 0 rgba(0,0,0,0.5);
            transition: all 0.3s ease;
        }

        .logo:hover {
            transform: scale(1.05);
            box-shadow: 
                0 0 40px rgba(212, 175, 55, 0.6),
                inset 0 1px 0 rgba(255,255,255,0.3);
        }

        .title {
            font-family: 'Cinzel', serif;
            font-size: 2.8rem;
            font-weight: 600;
            background: linear-gradient(135deg, #F4E5B2 0%, var(--gold) 50%, #B8973A 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
            margin-bottom: 8px;
            text-shadow: 0 2px 10px rgba(212, 175, 55, 0.3);
        }

        .subtitle {
            font-size: 0.9rem;
            color: rgba(212, 175, 55, 0.8);
            letter-spacing: 4px;
            text-transform: uppercase;
            font-weight: 400;
            position: relative;
            display: inline-block;
        }

        .subtitle::after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 50%;
            transform: translateX(-50%);
            width: 40px;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
        }

        /* Chat container luxury */
        .chat {
            max-width: 800px;
            margin: 0 auto;
            padding: 0 20px 120px;
            position: relative;
        }

        .messages {
            display: flex;
            flex-direction: column;
            gap: 25px;
            padding-top: 30px;
        }

        .message {
            max-width: 78%;
            padding: 22px 26px;
            border-radius: 24px;
            font-size: 16px;
            line-height: 1.6;
            animation: messageAppear 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) backwards;
            word-wrap: break-word;
            position: relative;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .message:hover {
            transform: translateY(-2px);
        }

        .message.user {
            align-self: flex-end;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
            color: #000;
            font-weight: 500;
            border-bottom-right-radius: 8px;
            box-shadow: 
                0 8px 32px rgba(212, 175, 55, 0.3),
                0 2px 8px rgba(212, 175, 55, 0.2),
                inset 0 1px 0 rgba(255,255,255,0.4);
            position: relative;
            overflow: hidden;
        }

        .message.user::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
        }

        .message.bot {
            align-self: flex-start;
            background: rgba(18, 18, 18, 0.95);
            color: #f0f0f0;
            border: 1px solid rgba(212, 175, 55, 0.2);
            border-bottom-left-radius: 8px;
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.4),
                0 2px 8px rgba(212, 175, 55, 0.1);
            position: relative;
        }

        .message.bot::after {
            content: '';
            position: absolute;
            top: -1px;
            left: -1px;
            right: -1px;
            bottom: -1px;
            background: linear-gradient(135deg, transparent, rgba(212, 175, 55, 0.1), transparent);
            border-radius: 24px;
            z-index: -1;
        }

        /* Input bar ultra premium */
        .input-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 20px 20px 30px;
            background: linear-gradient(to top, rgba(0,0,0,0.98) 0%, transparent 100%);
            backdrop-filter: blur(25px);
            border-top: 1px solid rgba(212, 175, 55, 0.1);
            z-index: 1000;
        }

        .input-wrapper {
            max-width: 800px;
            margin: 0 auto;
            position: relative;
        }

        #messageInput {
            width: 100%;
            padding: 20px 75px 20px 28px;
            background: rgba(15, 15, 15, 0.95);
            border: 1.5px solid rgba(212, 175, 55, 0.3);
            border-radius: 30px;
            color: white;
            font-size: 16.5px;
            font-family: inherit;
            outline: none;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            backdrop-filter: blur(20px);
            box-shadow: 
                0 4px 20px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
        }

        #messageInput:focus {
            border-color: var(--gold);
            box-shadow: 
                0 0 40px rgba(212, 175, 55, 0.3),
                0 4px 20px rgba(0, 0, 0, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }

        #messageInput::placeholder {
            color: rgba(212, 175, 55, 0.5);
            font-weight: 300;
        }

        .send-btn {
            position: absolute;
            right: 8px;
            top: 8px;
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
            border: none;
            color: #000;
            font-size: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 
                0 4px 20px rgba(212, 175, 55, 0.4),
                inset 0 1px 0 rgba(255,255,255,0.3),
                inset 0 -1px 0 rgba(0,0,0,0.2);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            font-weight: bold;
        }

        .send-btn:hover {
            transform: scale(1.05) rotate(5deg);
            box-shadow: 
                0 6px 25px rgba(212, 175, 55, 0.6),
                inset 0 1px 0 rgba(255,255,255,0.4);
        }

        .send-btn:active {
            transform: scale(0.95) rotate(0deg);
        }

        /* Typing indicator luxury */
        .typing {
            display: none;
            align-self: flex-start;
            padding: 20px 26px;
            background: rgba(18, 18, 18, 0.95);
            border: 1px solid rgba(212, 175, 55, 0.2);
            border-radius: 24px;
            border-bottom-left-radius: 8px;
            gap: 8px;
            margin-bottom: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }

        .typing.active { 
            display: flex; 
            animation: typingAppear 0.3s ease;
        }

        .typing span {
            width: 10px;
            height: 10px;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
            border-radius: 50%;
            animation: typingBounce 1.4s ease-in-out infinite;
            box-shadow: 0 2px 8px rgba(212, 175, 55, 0.3);
        }

        .typing span:nth-child(2) { animation-delay: 0.16s; }
        .typing span:nth-child(3) { animation-delay: 0.32s; }

        /* Animazioni premium */
        @keyframes glowPulse {
            0%, 100% { opacity: 0.08; transform: scale(1); }
            50% { opacity: 0.15; transform: scale(1.05); }
        }

        @keyframes typingBounce {
            0%, 100% { transform: translateY(0); opacity: 0.6; }
            50% { transform: translateY(-8px); opacity: 1; }
        }

        @keyframes messageAppear {
            from { 
                opacity: 0; 
                transform: translateY(20px) scale(0.95); 
            }
            to { 
                opacity: 1; 
                transform: translateY(0) scale(1); 
            }
        }

        @keyframes typingAppear {
            from { 
                opacity: 0; 
                transform: translateY(10px); 
            }
            to { 
                opacity: 1; 
                transform: translateY(0); 
            }
        }

        /* Effetti di lusso aggiuntivi */
        .gold-divider {
            height: 1px;
            background: linear-gradient(90deg, 
                transparent 0%, 
                rgba(212, 175, 55, 0.3) 20%, 
                rgba(212, 175, 55, 0.6) 50%, 
                rgba(212, 175, 55, 0.3) 80%, 
                transparent 100%);
            margin: 20px auto;
            max-width: 200px;
        }

        /* Scrollbar personalizzata */
        ::-webkit-scrollbar {
            width: 6px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(20, 20, 20, 0.8);
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(to bottom, var(--gold), var(--gold-dark));
            border-radius: 3px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(to bottom, var(--gold-light), var(--gold));
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .title {
                font-size: 2.2rem;
            }

            .message {
                max-width: 88%;
                padding: 18px 22px;
            }

            .logo-container {
                width: 80px;
                height: 80px;
            }

            .logo {
                width: 70px;
                height: 70px;
                font-size: 28px;
            }
        }
    </style>

    <div class="header">
        <div class="logo-container">
            <div class="logo-glow"></div>
            <div class="logo">◇</div>
        </div>
        <h1 class="title">Concierge</h1>
        <div class="subtitle">Assistenza Premium</div>
        <div class="gold-divider"></div>
    </div>

    <div class="chat">
        <div class="messages" id="messages">
            <div class="message bot">
                Buongiorno, sono il suo Concierge personale.<br><br>
                Sono qui per assisterla con la massima discrezione e competenza. Come posso esserle utile oggi?
            </div>
        </div>

        <div class="typing" id="typing">
            <span></span><span></span><span></span>
        </div>
    </div>

    <div class="input-bar">
        <div class="input-wrapper">
            <input 
                type="text" 
                id="messageInput" 
                placeholder="Scrivi il tuo messaggio..." 
                autocomplete="off"
                autofocus
                onkeypress="if(event.key==='Enter') sendMessage()"
            >
            <button class="send-btn" onclick="sendMessage()">➤</button>
        </div>
    </div>

    <script>
        const responses = {
            default: "Sto elaborando la sua richiesta con la massima attenzione. Un momento di pazienza, per favore.",
            greeting: "È un piacere servirla. Come posso assisterla oggi?",
            help: "Sono qui per aiutarla con qualsiasi necessità. Desidera prenotazioni, raccomandazioni o assistenza personale?",
            thanks: "Il piacere è tutto mio. Sono a sua completa disposizione."
        };

        function addMessage(text, isUser = false) {
            const container = document.getElementById('messages');
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'bot');
            div.innerHTML = text.replace(/\\n/g, '<br>');
            container.appendChild(div);

            // Scroll smooth alla fine
            container.parentElement.scrollTo({
                top: container.parentElement.scrollHeight,
                behavior: 'smooth'
            });
        }

        function showTyping() {
            const typing = document.getElementById('typing');
            typing.classList.add('active');

            // Scroll quando appare il typing
            const container = document.getElementById('messages').parentElement;
            container.scrollTo({
                top: container.scrollHeight,
                behavior: 'smooth'
            });
        }

        function hideTyping() {
            document.getElementById('typing').classList.remove('active');
        }

        function getResponse(message) {
            const lowerMessage = message.toLowerCase();

            if (lowerMessage.includes('ciao') || lowerMessage.includes('buongiorno') || lowerMessage.includes('salve')) {
                return responses.greeting;
            } else if (lowerMessage.includes('aiuto') || lowerMessage.includes('aiutami') || lowerMessage.includes('serve')) {
                return responses.help;
            } else if (lowerMessage.includes('grazie') || lowerMessage.includes('grazie mille')) {
                return responses.thanks;
            }

            return responses.default;
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const text = input.value.trim();

            if (!text) return;

            // Effetto vibrazione se disponibile
            if (window.Telegram && Telegram.WebApp && Telegram.WebApp.HapticFeedback) {
                Telegram.WebApp.HapticFeedback.impactOccurred('medium');
            }

            addMessage(text, true);
            input.value = '';

            showTyping();

            // Risposta intelligente con delay realistico
            const response = getResponse(text);
            const delay = 1200 + Math.random() * 1200;

            setTimeout(() => {
                hideTyping();
                addMessage(response);
            }, delay);
        }

        // Auto-focus sull'input
        document.getElementById('messageInput').focus();

        // Fix 100vh su mobile e effetti iniziali
        const setVh = () => {
            document.documentElement.style.setProperty('--vh', window.innerHeight + 'px');
        };

        window.addEventListener('resize', setVh);
        setVh();

        // Animazione di entrata per i messaggi esistenti
        document.addEventListener('DOMContentLoaded', () => {
            const messages = document.querySelectorAll('.message');
            messages.forEach((msg, index) => {
                msg.style.animationDelay = `${index * 0.1}s`;
            });
        });

        // Miglioramento UX: focus sull'input quando si clicca anywhere
        document.addEventListener('click', (e) => {
            if (!e.target.matches('.send-btn') && !e.target.matches('#messageInput')) {
                document.getElementById('messageInput').focus();
            }
        });
    </script>
    """
    return get_base_template("Concierge Premium", content, "agent")
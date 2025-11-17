# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """Concierge AI • Ultra Luxury Premium • Deep Black & Gold Borders"""
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
            padding: 40px 20px 25px;
            position: relative;
            border-bottom: 1px solid rgba(212, 175, 55, 0.1);
            background: linear-gradient(to bottom, rgba(0,0,0,0.95) 0%, transparent 100%);
            backdrop-filter: blur(20px);
            z-index: 1000;
        }

        .logo-container {
            position: relative;
            width: 70px;
            height: 70px;
            margin: 0 auto 20px;
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
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            position: relative;
            z-index: 2;
            box-shadow: 
                0 0 20px rgba(212, 175, 55, 0.3),
                inset 0 1px 0 rgba(255,255,255,0.2),
                inset 0 -1px 0 rgba(0,0,0,0.5);
        }

        .title {
            font-family: 'Cinzel', serif;
            font-size: 2.2rem;
            font-weight: 600;
            background: linear-gradient(135deg, #F4E5B2 0%, var(--gold) 50%, #B8973A 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
            margin-bottom: 6px;
        }

        .subtitle {
            font-size: 0.8rem;
            color: rgba(212, 175, 55, 0.8);
            letter-spacing: 3px;
            text-transform: uppercase;
            font-weight: 400;
        }

        /* Chat container luxury - FIXED FOR NAVBAR */
        .chat {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px 20px 140px; /* Increased bottom padding for input bar */
            position: relative;
            height: calc(100vh - 180px);
            overflow-y: auto;
        }

        .messages {
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding-top: 10px;
        }

        /* ULTRA PREMIUM CHAT BUBBLES - Black with Gold Borders */
        .message {
            max-width: 78%;
            padding: 18px 22px;
            border-radius: 20px;
            font-size: 15px;
            line-height: 1.5;
            animation: messageAppear 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) backwards;
            word-wrap: break-word;
            position: relative;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            border: 1px solid rgba(212, 175, 55, 0.3);
        }

        .message::before {
            content: '';
            position: absolute;
            inset: -1px;
            border-radius: 20px;
            padding: 1px;
            background: linear-gradient(135deg, var(--gold), transparent 30%, var(--gold));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0.6;
        }

        .message:hover {
            transform: translateY(-1px);
            border-color: rgba(212, 175, 55, 0.5);
        }

        .message.user {
            align-self: flex-end;
            background: rgba(15, 15, 15, 0.95);
            color: #f0f0f0;
            border-bottom-right-radius: 6px;
            box-shadow: 
                0 4px 20px rgba(0, 0, 0, 0.4),
                0 2px 8px rgba(212, 175, 55, 0.2);
        }

        .message.user::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.3), transparent);
        }

        .message.bot {
            align-self: flex-start;
            background: rgba(12, 12, 12, 0.95);
            color: #f0f0f0;
            border-bottom-left-radius: 6px;
            box-shadow: 
                0 4px 20px rgba(0, 0, 0, 0.4),
                0 2px 8px rgba(212, 175, 55, 0.1);
        }

        /* Input bar ultra premium - FIXED POSITION */
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
            padding: 18px 70px 18px 24px;
            background: rgba(10, 10, 10, 0.95);
            border: 1.5px solid rgba(212, 175, 55, 0.3);
            border-radius: 25px;
            color: white;
            font-size: 16px;
            font-family: inherit;
            outline: none;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            backdrop-filter: blur(20px);
            box-shadow: 
                0 4px 20px rgba(0, 0, 0, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
        }

        #messageInput:focus {
            border-color: var(--gold);
            box-shadow: 
                0 0 30px rgba(212, 175, 55, 0.25),
                0 4px 20px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }

        #messageInput::placeholder {
            color: rgba(212, 175, 55, 0.5);
            font-weight: 300;
        }

        .send-btn {
            position: absolute;
            right: 6px;
            top: 6px;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
            border: none;
            color: #000;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 
                0 4px 15px rgba(212, 175, 55, 0.4),
                inset 0 1px 0 rgba(255,255,255,0.3),
                inset 0 -1px 0 rgba(0,0,0,0.2);
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            font-weight: bold;
            z-index: 1001;
        }

        .send-btn:hover {
            transform: scale(1.05);
            box-shadow: 
                0 6px 20px rgba(212, 175, 55, 0.6),
                inset 0 1px 0 rgba(255,255,255,0.4);
        }

        .send-btn:active {
            transform: scale(0.95);
        }

        /* Typing indicator luxury */
        .typing {
            display: none;
            align-self: flex-start;
            padding: 16px 22px;
            background: rgba(12, 12, 12, 0.95);
            border: 1px solid rgba(212, 175, 55, 0.2);
            border-radius: 20px;
            border-bottom-left-radius: 6px;
            gap: 8px;
            margin-bottom: 15px;
            backdrop-filter: blur(10px);
            position: relative;
        }

        .typing::before {
            content: '';
            position: absolute;
            inset: -1px;
            border-radius: 20px;
            padding: 1px;
            background: linear-gradient(135deg, var(--gold), transparent 30%, var(--gold));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            opacity: 0.4;
        }

        .typing.active { 
            display: flex; 
            animation: typingAppear 0.3s ease;
        }

        .typing span {
            width: 8px;
            height: 8px;
            background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
            border-radius: 50%;
            animation: typingBounce 1.4s ease-in-out infinite;
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
            50% { transform: translateY(-6px); opacity: 1; }
        }

        @keyframes messageAppear {
            from { 
                opacity: 0; 
                transform: translateY(15px) scale(0.95); 
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

        /* Scrollbar personalizzata */
        .chat::-webkit-scrollbar {
            width: 5px;
        }

        .chat::-webkit-scrollbar-track {
            background: rgba(20, 20, 20, 0.8);
        }

        .chat::-webkit-scrollbar-thumb {
            background: linear-gradient(to bottom, var(--gold), var(--gold-dark));
            border-radius: 3px;
        }

        .chat::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(to bottom, var(--gold-light), var(--gold));
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .header {
                padding: 30px 20px 20px;
            }

            .title {
                font-size: 1.8rem;
            }

            .message {
                max-width: 85%;
                padding: 16px 20px;
                font-size: 14px;
            }

            .logo-container {
                width: 60px;
                height: 60px;
            }

            .logo {
                width: 50px;
                height: 50px;
                font-size: 20px;
            }

            .chat {
                padding: 15px 15px 130px;
                height: calc(100vh - 150px);
            }

            .input-bar {
                padding: 15px 15px 25px;
            }

            #messageInput {
                padding: 16px 65px 16px 20px;
                font-size: 15px;
            }

            .send-btn {
                width: 44px;
                height: 44px;
                font-size: 16px;
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
    </div>

    <div class="chat" id="chatContainer">
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
            thanks: "Il piacere è tutto mio. Sono a sua completa disposizione.",
            menu: "Certamente. Posso mostrarle il nostro menu gourmet, prendere una prenotazione o consigliarle le specialità del giorno.",
            finance: "Per la gestione patrimoniale, posso metterla in contatto con i nostri esperti finanziari o mostrare gli strumenti disponibili.",
            wellness: "Per il suo benessere, possiamo programmare una sessione di consulenza o esplorare le risorse disponibili."
        };

        function addMessage(text, isUser = false) {
            const container = document.getElementById('messages');
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'bot');
            div.innerHTML = text.replace(/\\n/g, '<br>');
            container.appendChild(div);

            // Scroll smooth alla fine
            const chatContainer = document.getElementById('chatContainer');
            chatContainer.scrollTo({
                top: chatContainer.scrollHeight,
                behavior: 'smooth'
            });
        }

        function showTyping() {
            const typing = document.getElementById('typing');
            typing.classList.add('active');

            // Scroll quando appare il typing
            const chatContainer = document.getElementById('chatContainer');
            chatContainer.scrollTo({
                top: chatContainer.scrollHeight,
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
            } else if (lowerMessage.includes('grazie')) {
                return responses.thanks;
            } else if (lowerMessage.includes('menu') || lowerMessage.includes('cibo') || lowerMessage.includes('mangiare')) {
                return responses.menu;
            } else if (lowerMessage.includes('finanza') || lowerMessage.includes('soldi') || lowerMessage.includes('denaro')) {
                return responses.finance;
            } else if (lowerMessage.includes('benessere') || lowerMessage.includes('psicologia') || lowerMessage.includes('mente')) {
                return responses.wellness;
            }

            return responses.default;
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const text = input.value.trim();

            if (!text) return;

            // Effetto vibrazione se disponibile
            if (window.Telegram && Telegram.WebApp && Telegram.WebApp.HapticFeedback) {
                Telegram.WebApp.HapticFeedback.impactOccurred('light');
            }

            addMessage(text, true);
            input.value = '';

            showTyping();

            // Risposta intelligente con delay realistico
            const response = getResponse(text);
            const delay = 1000 + Math.random() * 1000;

            setTimeout(() => {
                hideTyping();
                addMessage(response);
            }, delay);
        }

        // Auto-focus sull'input e gestione navbar
        function setupInputFocus() {
            const input = document.getElementById('messageInput');
            const chatContainer = document.getElementById('chatContainer');

            input.addEventListener('focus', function() {
                // Scroll alla fine quando l'input è focalizzato
                setTimeout(() => {
                    chatContainer.scrollTo({
                        top: chatContainer.scrollHeight,
                        behavior: 'smooth'
                    });
                }, 300);
            });

            input.focus();
        }

        // Fix 100vh su mobile
        const setVh = () => {
            const vh = window.innerHeight * 0.01;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        };

        window.addEventListener('resize', setVh);
        setVh();

        // Inizializzazione
        document.addEventListener('DOMContentLoaded', function() {
            setupInputFocus();

            // Animazione di entrata per i messaggi esistenti
            const messages = document.querySelectorAll('.message');
            messages.forEach((msg, index) => {
                msg.style.animationDelay = `${index * 0.1}s`;
            });
        });

        // Click anywhere per focus sull'input
        document.addEventListener('click', function(e) {
            if (!e.target.matches('.send-btn') && !e.target.matches('#messageInput')) {
                document.getElementById('messageInput').focus();
            }
        });
    </script>
    """
    return get_base_template("Concierge Premium", content, "agent")
from web.templates.base import get_base_template


def generate_agent_page():
    """Pagina Agente AI - Ultra Premium - Nero & Oro"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;500;600&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-light: #F4E5B2;
            --gold-dark: #9B7F1B;
            --black: #0A0A0A;
            --black-light: #1A1A1A;
            --black-lighter: #2A2A2A;
            --white: #FFFFFF;
        }

        body {
            background: var(--black);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* Header Premium */
        .agent-header {
            text-align: center;
            padding: 50px 20px 30px;
            position: relative;
            flex-shrink: 0;
        }
        .agent-title {
            font-family: 'Playfair Display', serif;
            font-size: 38px;
            font-weight: 900;
            background: linear-gradient(135deg, var(--gold-light), var(--gold), var(--gold-dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -1px;
            margin: 16px 0 8px;
            animation: fadeInUp 0.9s ease;
        }
        .agent-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: var(--gold-light);
            letter-spacing: 3px;
            text-transform: uppercase;
            opacity: 0.9;
            animation: fadeInUp 0.9s ease 0.2s backwards;
        }

        /* Chat Container */
        .chat-container {
            flex: 1;
            max-width: 800px;
            width: 100%;
            margin: 0 auto;
            padding: 0 20px 20px;
            display: flex;
            flex-direction: column;
            position: relative;
        }

        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 20px 0;
            display: flex;
            flex-direction: column;
            gap: 20px;
            scrollbar-width: none;
            -ms-overflow-style: none;
        }
        .messages::-webkit-scrollbar {
            display: none;
        }

        .message {
            max-width: 85%;
            padding: 16px 20px;
            border-radius: 24px;
            animation: messageAppear 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            word-wrap: break-word;
        }
        @keyframes messageAppear {
            from { opacity: 0; transform: translateY(20px) scale(0.95); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        .message.user {
            align-self: flex-end;
            background: linear-gradient(135deg, rgba(212,175,55,0.2), rgba(212,175,55,0.1));
            border: 1px solid rgba(212,175,55,0.3);
            color: var(--gold-light);
            border-bottom-right-radius: 6px;
        }
        .message.assistant {
            align-self: flex-start;
            background: var(--black-light);
            border: 1px solid rgba(212,175,55,0.15);
            color: var(--white);
            border-bottom-left-radius: 6px;
        }
        .message.assistant::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            left: -1px;
            right: -1px;
            bottom: -1px;
            border-radius: 24px;
            background: linear-gradient(135deg, transparent 30%, var(--gold) 50%, transparent 70%);
            opacity: 0.1;
            pointer-events: none;
        }

        /* Input Area Premium */
        .input-area {
            background: var(--black-light);
            border: 1px solid rgba(212,175,55,0.25);
            border-radius: 30px;
            padding: 12px 20px;
            margin-top: 10px;
            display: flex;
            align-items: center;
            gap: 16px;
            backdrop-filter: blur(12px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            transition: all 0.4s;
        }
        .input-area:focus-within {
            border-color: var(--gold);
            box-shadow: 0 0 0 1px var(--gold), 0 12px 40px rgba(212,175,55,0.3);
        }

        #message-input {
            flex: 1;
            background: transparent;
            border: none;
            outline: none;
            color: var(--white);
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            padding: 8px 0;
        }
        #message-input::placeholder {
            color: rgba(212,175,55,0.5);
        }

        .send-button {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, var(--gold), var(--gold-dark));
            border: none;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 4px 16px rgba(212,175,55,0.4);
        }
        .send-button:active {
            transform: scale(0.9);
        }
        .send-button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        .send-icon {
            font-size: 20px;
            color: var(--black);
        }

        /* Particelle oro (stesse della home) */
        .gold-particle {
            position: fixed;
            width: 3px;
            height: 3px;
            background: var(--gold);
            border-radius: 50%;
            pointer-events: none;
            z-index: 0;
            opacity: 0;
            animation: particle-float linear infinite;
        }
        @keyframes particle-float {
            0% { opacity: 0; transform: translateY(100vh) scale(0); }
            10% { opacity: 0.8; }
            90% { opacity: 0.8; }
            100% { opacity: 0; transform: translateY(-20vh) scale(1); }
        }
    </style>

    <div class="agent-header">
        <div class="logo-icon" style="font-size: 64px; animation: float 6s ease-in-out infinite;">🤖</div>
        <h1 class="agent-title">Danison Assistant</h1>
        <div class="agent-subtitle">Il tuo assistente AI privato • Sempre attivo</div>
    </div>

    <div class="chat-container">
        <div class="messages" id="messages">
            <!-- I messaggi verranno inseriti qui via JS -->
            <div class="message assistant">
                Buongiorno. Sono Danison, il tuo assistente personale premium.<br><br>
                Posso aiutarti con qualsiasi cosa: strategia finanziaria, benessere mentale, consigli gourmet, programmazione, o semplicemente una conversazione profonda.<br><br>
                Dimmi pure, sono tutto orecchie.
            </div>
        </div>

        <div class="input-area">
            <input type="text" id="message-input" placeholder="Scrivi il tuo messaggio..." autocomplete="off">
            <button class="send-button" id="send-button">
                <span class="send-icon">↑</span>
            </button>
        </div>
    </div>

    <script>
        // Particelle dorate
        function createGoldParticles();
        function createGoldParticles() {
            for (let i = 0; i < 12; i++) {
                const p = document.createElement('div');
                p.className = 'gold-particle';
                p.style.left = Math.random() * 100 + '%';
                p.style.animationDuration = (Math.random() * 10 + 8) + 's';
                p.style.animationDelay = Math.random() * 6 + 's';
                document.body.appendChild(p);
            }
        }

        const messagesDiv = document.getElementById('messages');
        const input = document.getElementById('message-input');
        const sendBtn = document.getElementById('send-button');

        function addMessage(text, isUser = false) {
            const msg = document.createElement('div');
            msg.className = `message ${isUser ? 'user' : 'assistant'}`;
            msg.innerHTML = text;
            messagesDiv.appendChild(msg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;

            // Haptic leggero quando arriva risposta
            if (!isUser) {
                Telegram.WebApp.HapticFeedback.notificationOccurred('success');
            }
        }

        sendBtn.addEventListener('click', sendMessage);
        input.addEventListener('keypress', e => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });

        function sendMessage() {
            const text = input.value.trim();
            if (!text) return;

            addMessage(text, true);
            input.value = '';

            // Feedback aptico invio
            Telegram.WebApp.HapticFeedback.impactOccurred('medium');

            // Simulazione risposta (da sostituire con vera chiamata API)
            setTimeout(() => {
                addMessage(`Ho capito perfettamente. Ecco una risposta premium a "${text}".<br><br>Se desideri approfondire qualsiasi aspetto (analisi finanziaria, coaching psicologico, ricetta stellata o codice), fammi sapere — sono qui per servirti al massimo livello.`);
            }, 1200);
        }

        // Focus automatico sull'input
        input.focus();
    </script>
    """
    return get_base_template("Danison Assistant", content, "agent")
# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """Concierge AI • Ultra Minimal Premium • Black & 18K Gold"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-light: #E8C867;
            --black: #000000;
            --dark: #0A0A0A;
        }

        * { margin:0; padding:0; box-sizing:border-box; }
        body { 
            background: var(--black); 
            color: white; 
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
            min-height: calc(var(--vh, 1vh) * 100);
        }

        /* Header minimal ma potente */
        .header {
            text-align: center;
            padding: 60px 20px 40px;
        }

        .logo {
            width: 86px; height: 86px;
            margin: 0 auto 20px;
            background: radial-gradient(circle at 30% 30%, var(--gold) 0%, transparent 60%);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 36px;
            position: relative;
        }

        .logo::before {
            content: '';
            position: absolute;
            inset: -12px;
            border: 1px solid rgba(212,175,55,0.25);
            border-radius: 50%;
            animation: pulseRing 4s infinite;
        }

        @keyframes pulseRing {
            0%,100% { transform: scale(1); opacity: 0.4; }
            50% { transform: scale(1.15); opacity: 0.2; }
        }

        .title {
            font-family: 'Cinzel', serif;
            font-size: 32px;
            font-weight: 600;
            background: linear-gradient(90deg, #F4E5B2, var(--gold), #B8973A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .subtitle {
            margin-top: 8px;
            font-size: 13px;
            color: rgba(212,175,55,0.7);
            letter-spacing: 3px;
            text-transform: uppercase;
            font-weight: 500;
        }

        /* Chat container */
        .chat {
            max-width: 680px;
            margin: 0 auto;
            padding: 0 20px 100px;
        }

        .messages {
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding-top: 20px;
        }

        .message {
            max-width: 86%;
            padding: 16px 20px;
            border-radius: 22px;
            font-size: 15.8px;
            line-height: 1.56;
            animation: fadeUp 0.5s ease backwards;
            word-wrap: break-word;
        }

        .message.user {
            align-self: flex-end;
            background: linear-gradient(135deg, var(--gold), #B8973A);
            color: #000;
            font-weight: 500;
            border-bottom-right-radius: 6px;
            box-shadow: 0 8px 25px rgba(212,175,55,0.3);
        }

        .message.bot {
            align-self: flex-start;
            background: rgba(28,28,28,0.95);
            color: #eee;
            border: 1px solid rgba(212,175,55,0.15);
            border-bottom-left-radius: 6px;
            backdrop-filter: blur(10px);
        }

        .message.bot::before {
            content: '◇';
            position: absolute;
            top: -8px; left: 16px;
            font-size: 18px;
            color: var(--gold);
            filter: drop-shadow(0 2px 6px rgba(212,175,55,0.5));
        }

        /* Input bar fissa in basso - la parte più premium */
        .input-bar {
            position: fixed;
            bottom: 0; left: 0; right: 0;
            padding: 16px 20px 28px;
            background: linear-gradient(to top, var(--black) 60%, transparent);
            backdrop-filter: blur(12px);
        }

        .input-wrapper {
            max-width: 680px;
            margin: 0 auto;
            position: relative;
        }

        #messageInput {
            width: 100%;
            padding: 18px 68px 18px 24px;
            background: rgba(20,20,20,0.95);
            border: 1.5px solid rgba(212,175,55,0.25);
            border-radius: 30px;
            color: white;
            font-size: 16.5px;
            font-family: inherit;
            outline: none;
            transition: all 0.4s cubic-bezier(0.34,1.56,0.64,1);
            backdrop-filter: blur(12px);
        }

        #messageInput:focus {
            border-color: var(--gold);
            box-shadow: 0 0 40px rgba(212,175,55,0.25);
        }

        #messageInput::placeholder {
            color: rgba(212,175,55,0.4);
        }

        .send-btn {
            position: absolute;
            right: 8px; top: 8px;
            width: 50px; height: 50px;
            border-radius: 50%;
            background: var(--gold);
            border: none;
            color: #000;
            font-size: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 6px 20px rgba(212,175,55,0.4);
            transition: all 0.3s;
        }

        .send-btn:active {
            transform: scale(0.88);
        }

        /* Typing indicator minimal */
        .typing {
            display: none;
            align-self: flex-start;
            padding: 16px 20px;
            background: rgba(28,28,28,0.95);
            border: 1px solid rgba(212,175,55,0.15);
            border-radius: 22px;
            border-bottom-left-radius: 6px;
            gap: 8px;
            margin-bottom: 12px;
        }
        .typing.active { display: flex; }
        .typing span {
            width: 9px; height: 9px;
            background: var(--gold);
            border-radius: 50%;
            animation: typing 1.4s infinite;
        }
        .typing span:nth-child(2) { animation-delay: 0.2s; }
        .typing span:nth-child(3) { animation-delay: 0.4s; }

        @keyframes typing {
            0%,100% { transform: translateY(0); opacity: 0.6; }
            50% { transform: translateY(-10px); opacity: 1; }
        }
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: none; }
        }
    </style>

    <div class="header">
        <div class="logo">◇</div>
        <h1 class="title">Concierge</h1>
        <div class="subtitle">Il tuo assistente privato</div>
    </div>

    <div class="chat">
        <div class="messages" id="messages">
            <div class="message bot">
                Buongiorno.<br>
                Sono il tuo Concierge privato. Come posso esserti utile oggi?
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
                placeholder="Scrivi qui..." 
                autocomplete="off"
                onkeypress="if(event.key==='Enter') sendMessage()"
            >
            <button class="send-btn" onclick="sendMessage()">➤</button>
        </div>
    </div>

    <script>
        const responses = {
            default: "Un attimo, sto preparando la risposta perfetta per lei..."
        };

        function addMessage(text, isUser = false) {
            const container = document.getElementById('messages');
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'bot');
            div.innerHTML = text.replace(/\\n/g, '<br>');
            container.appendChild(div);
            container.parentElement.scrollTop = container.parentElement.scrollHeight;
        }

        function showTyping() {
            document.getElementById('typing').classList.add('active');
        }
        function hideTyping() {
            document.getElementById('typing').classList.remove('active');
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const text = input.value.trim();
            if (!text) return;

            Telegram.WebApp.HapticFeedback.impactOccurred('medium');
            addMessage(text, true);
            input.value = '';

            showTyping();
            setTimeout(() => {
                hideTyping();
                addMessage(responses.default || "Perfetto. Sto elaborando la sua richiesta con la massima cura.");
            }, 1200 + Math.random() * 1500);
        }

        // Fix 100vh su mobile
        const setVh = () => document.documentElement.style.setProperty('--vh', window.innerHeight + 'px');
        window.addEventListener('resize', setVh);
        setVh();
    </script>
    """
    return get_base_template("Concierge", content, "agent")
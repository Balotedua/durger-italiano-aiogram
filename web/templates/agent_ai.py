# web/templates/agent.py
from web.templates.base import get_base_template


def generate_agent_page():
    """Danison Assistant — Ultra Premium Black & Gold"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-subtle: rgba(212,175,55,0.4);
            --black: #0A0A0A;
            --black-light: #111111;
            --black-lighter: #1A1A1A;
            --text: #EAEAEA;
            --text-muted: #999999;
        }

        body { background: var(--black); color: var(--text); min-height: 100vh; display: flex; flex-direction: column; }

        /* Header minimal & elegante */
        .header {
            text-align: center;
            padding: 60px 20px 40px;
        }
        .logo {
            font-size: 68px;
            animation: float 7s ease-in-out infinite;
            filter: drop-shadow(0 8px 30px rgba(212,175,55,0.25));
        }
        @keyframes float {
            0%,100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        .title {
            font-family: 'Playfair Display', serif;
            font-size: 40px;
            font-weight: 900;
            letter-spacing: -1.2px;
            margin: 20px 0 8px;
            background: linear-gradient(135deg, #F4E5B2, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            font-weight: 400;
            letter-spacing: 4px;
            color: var(--text-muted);
            text-transform: uppercase;
        }

        /* Chat */
        .chat {
            flex: 1;
            max-width: 820px;
            margin: 0 auto;
            padding: 0 24px 24px;
            display: flex;
            flex-direction: column;
        }
        .messages {
            flex: 1;
            overflow-y: auto;
            padding: 10px 0 20px;
            display: flex;
            flex-direction: column;
            gap: 18px;
            scrollbar-width: none;
        }
        .messages::-webkit-scrollbar { display: none; }

        .message {
            max-width: 78%;
            padding: 16px 20px;
            border-radius: 22px;
            line-height: 1.65;
            font-family: 'Inter', sans-serif;
            font-size: 15.5px;
            animation: appear 0.5s ease outwards;
        }
        @keyframes appear {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: none; }
        }

        .user {
            align-self: flex-end;
            background: rgba(212,175,55,0.12);
            color: #F4E5B2;
            border-bottom-right-radius: 4px;
        }
        .assistant {
            align-self: flex-start;
            background: var(--black-lighter);
            color: var(--text);
            border-bottom-left-radius: 4px;
        }

        /* Input pulitissimo */
        .input-wrapper {
            margin-top: 8px;
            position: relative;
        }
        #message-input {
            width: 100%;
            background: var(--black-light);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 30px;
            padding: 16px 56px 16px 24px;
            color: white;
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            outline: none;
            transition: all 0.4s ease;
        }
        #message-input::placeholder {
            color: rgba(212,175,55,0.4);
        }
        #message-input:focus {
            border-color: var(--gold);
            box-shadow: 0 0 0 1px var(--gold), 0 12px 40px rgba(212,175,55,0.15);
        }

        .send-btn {
            position: absolute;
            right: 8px;
            top: 8px;
            width: 44px;
            height: 44px;
            background: var(--gold);
            border: none;
            border-radius: 50%;
            color: black;
            font-size: 18px;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .send-btn:hover { transform: scale(1.08); }
        .send-btn:active { transform: scale(0.94); }

        /* Particelle dorate sottilissime */
        .particle {
            position: fixed;
            width: 2px;
            height: 2px;
            background: var(--gold);
            border-radius: 50%;
            pointer-events: none;
            opacity: 0;
            animation: rise linear infinite;
        }
        @keyframes rise {
            0%   { opacity: 0; transform: translateY(100vh) scale(0); }
            8%   { opacity: 0.6; }
            92%  { opacity: 0.6; }
            100% { opacity: 0; transform: translateY(-50px) scale(1); }
        }
    </style>

    <div class="header">
        <div class="logo">🤖</div>
        <h1 class="title">Danison</h1>
        <div class="subtitle">Il tuo assistente personale</div>
    </div>

    <div class="chat">
        <div class="messages" id="messages">
            <div class="message assistant">
                Buongiorno.<br><br>
                Sono Danison, sempre a tua disposizione.<br><br>
                In cosa posso esserti utile oggi?
            </div>
        </div>

        <div class="input-wrapper">
            <input type="text" id="message-input" placeholder="Messaggio..." autocomplete="off">
            <button class="send-btn" id="send-btn">↑</button>
        </div>
    </div>

    <script>
        // Particelle sottili
        for(let i=0; i<11; i++){
            const p = document.createElement('div');
            p.className = 'particle';
            p.style.left = Math.random()*100 + '%';
            p.style.animationDuration = (Math.random()*12 + 12) + 's';
            p.style.animationDelay = Math.random()*8 + 's';
            document.body.appendChild(p);
        }

        const messages = document.getElementById('messages');
        const input = document.getElementById('message-input');
        const btn = document.getElementById('send-btn');

        function add(text, isUser=false){
            const div = document.createElement('div');
            div.className = `message ${isUser?'user':'assistant'}`;
            div.innerHTML = text.replace(/\\n/g, '<br>');
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
            if(!isUser) Telegram.WebApp.HapticFeedback.notificationOccurred('success');
        }

        async function send(){
            const text = input.value.trim();
            if(!text) return;
            add(text, true);
            input.value = '';
            btn.disabled = true;
            Telegram.WebApp.HapticFeedback.impactOccurred('medium');

            // Qui la tua vera API
            const res = await fetch('/api/agent/chat', {
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify({message: text})
            });
            const data = await res.json();
            add(data.reply || "Qualcosa è andato storto. Riprova.");
            btn.disabled = false;
            input.focus();
        }

        btn.onclick = send;
        input.onkeydown = e => { if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); send(); }};
        input.focus();
    </script>
    """
    return get_base_template("Danison", content, "agent")
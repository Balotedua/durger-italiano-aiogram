# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """AI Concierge ULTRA PREMIUM - Black & 18K Gold Edition"""
    content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@300;400;500;600;700&display=swap');

        :root {
            --gold: #D4AF37;
            --gold-glow: #FFD700;
            --black: #000000;
            --dark: #0F0F0F;
        }

        * { margin:0; padding:0; box-sizing:border-box; }
        body { 
            background: var(--black); 
            color: white; 
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
        }

        /* Effetto particelle dorate in background (solo desktop + dispositivi potenti) */
        #particles {
            position: fixed; inset: 0; z-index: 0; pointer-events: none;
        }

        /* Header Ultra-Premium */
        .header {
            position: relative;
            text-align: center;
            padding: 60px 20px 40px;
            z-index: 2;
        }

        .avatar-container {
            position: relative;
            width: 120px; height: 120px;
            margin: 0 auto 24px;
        }

        .avatar-ring {
            position: absolute;
            inset: 0;
            border: 2px solid transparent;
            border-radius: 50%;
            background: linear-gradient(45deg, transparent, var(--gold), transparent) border-box;
            mask: linear-gradient(#fff 0 0) padding-box, linear-gradient(#fff 0 0);
            mask-composite: exclude;
            animation: rotate 20s linear infinite;
        }

        .avatar {
            width: 100%; height: 100%;
            background: radial-gradient(circle at 30% 30%, #1a1a1a, #000);
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 56px;
            position: relative;
            z-index: 1;
            box-shadow: 0 20px 60px rgba(212,175,55,0.3);
        }

        .avatar::before {
            content: '';
            position: absolute;
            inset: -8px;
            border-radius: 50%;
            background: conic-gradient(from 0deg, transparent, var(--gold), transparent);
            opacity: 0.4;
            animation: spin 8s linear infinite;
        }

        @keyframes rotate { to { transform: rotate(360deg); } }
        @keyframes spin { to { transform: rotate(360deg); } }

        .title {
            font-family: 'Cinzel', serif;
            font-size: 36px;
            font-weight: 700;
            background: linear-gradient(90deg, #F4E5B2, var(--gold), #B8973A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -1px;
            margin-bottom: 8px;
        }

        .subtitle {
            font-size: 14px;
            color: rgba(212,175,55,0.8);
            text-transform: uppercase;
            letter-spacing: 4px;
            font-weight: 500;
        }

        .status {
            margin-top: 16px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 8px 20px;
            background: rgba(212,175,55,0.08);
            border: 1px solid rgba(212,175,55,0.25);
            border-radius: 30px;
            font-size: 12px;
            letter-spacing: 1.5px;
            color: var(--gold);
        }

        .status::before {
            content: '';
            width: 8px; height: 8px;
            background: var(--gold);
            border-radius: 50%;
            box-shadow: 0 0 20px var(--gold-glow);
            animation: pulse 2s infinite;
        }

        /* Quick Actions - Luxury Cards */
        .actions {
            display: grid;
            grid-template-columns: repeat(2,1fr);
            gap: 16px;
            padding: 0 20px;
            max-width: 600px;
            margin: 40px auto 30px;
        }

        .action-card {
            position: relative;
            padding: 28px 20px;
            background: rgba(20,20,20,0.6);
            border: 1px solid rgba(212,175,55,0.15);
            border:hover { border-color: var(--gold); }
            border-radius: 24px;
            text-align: center;
            cursor: pointer;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.34,1.56,0.64,1);
            backdrop-filter: blur(12px);
        }

        .action-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(212,175,55,0.15), transparent 50%);
            opacity: 0;
            transition: opacity 0.4s;
        }

        .action-card:hover::before { opacity: 1; }
        .action-card:active { transform: scale(0.95); }

        .action-icon {
            font-size: 36px;
            margin-bottom: 12px;
            display: block;
        }

        .action-label {
            font-weight: 600;
            font-size: 14px;
            color: var(--gold);
            letter-spacing: 0.5px;
        }

        /* Chat Container */
        .chat-wrapper {
            max-width: 640px;
            margin: 0 auto;
            padding: 0 20px 20px;
        }

        .chat-messages {
            height: 58vh;
            overflow-y: auto;
            padding: 24px;
            background: rgba(15,15,15,0.7);
            border: 1px solid rgba(212,175,55,0.12);
            border-radius: 28px;
            backdrop-filter: blur(16px);
            display: flex;
            flex-direction: column;
            gap: 18px;
        }

        /* Scrollbar oro */
        .chat-messages::-webkit-scrollbar { width: 4px; }
        .chat-messages::-webkit-scrollbar-thumb { 
            background: rgba(212,175,55,0.4); 
            border-radius: 2px;
        }

        .message {
            padding: 16px 22px;
            border-radius: 22px;
            max-width: 82%;
            animation: fadeInUp 0.5s ease backwards;
            font-size: 15.5px;
            line-height: 1.55;
            position: relative;
        }

        .message.user {
            align-self: flex-end;
            background: linear-gradient(135deg, #B8973A, var(--gold), #E8C567);
            color: #000;
            font-weight: 500;
            box-shadow: 0 10px 30px rgba(212,175,55,0.35);
        }

        .message.bot {
            align-self: flex-start;
            background: rgba(30,30,30,0.9);
            color: #eee;
            border: 1px solid rgba(212,175,55,0.18);
            backdrop-filter: blur(10px);
        }

        .message.bot::after {
            content: '✦';
            position: absolute;
            top: -6px; left: 16px;
            font-size: 18px;
            color: var(--gold);
            filter: drop-shadow(0 2px 8px rgba(212,175,55,0.6));
        }

        /* Input Premium */
        .input-wrapper {
            margin-top: 16px;
            position: relative;
        }

        .input-field {
            width: 100%;
            padding: 18px 70px 18px 24px;
            background: rgba(20,20,20,0.8);
            border: 1.5px solid rgba(212,175,55,0.2);
            border-radius: 30px;
            color: white;
            font-size: 16px;
            backdrop-filter: blur(12px);
            transition: all 0.4s;
        }

        .input-field:focus {
            outline: none;
            border-color: var(--gold);
            box-shadow: 0 0 40px rgba(212,175,55,0.3);
        }

        .send-btn {
            position: absolute;
            right: 6px; top: 6px;
            width: 52px; height: 52px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--gold), #B8973A);
            border: none;
            color: #000;
            font-size: 22px;
            cursor: pointer;
            box-shadow: 0 8px 25px rgba(212,175,55,0.4);
            transition: all 0.3s;
        }

        .send-btn:active { transform: scale(0.88); }

        /* Typing indicator di lusso */
        .typing {
            display: inline-flex; gap: 8px; padding: 16px 24px;
            background: rgba(30,30,30,0.9);
            border: 1px solid rgba(212,175,55,0.2);
            border-radius: 22px;
            align-self: flex-start;
        }
        .typing span {
            width: 10px; height: 10px;
            background: var(--gold);
            border-radius: 50%;
            animation: typing 1.4s infinite;
        }
        .typing span:nth-child(2) { animation-delay: 0.2s; }
        .typing span:nth-child(3) { animation-delay: 0.4s; }

        @keyframes typing {
            0%,100% { transform: translateY(0); opacity: 0.6; }
            50% { transform: translateY(-12px); opacity: 1; }
        }
        @keyframes fadeInUp { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:none; } }
        @keyframes pulse { 0%,100% { opacity:0.7; } 50% { opacity:1; } }
    </style>

    <!-- Particelle dorate di sfondo (lussuosissime) -->
    <canvas id="particles"></canvas>

    <div class="header">
        <div class="avatar-container">
            <div class="avatar-ring"></div>
            <div class="avatar">✦</div>
        </div>
        <h1 class="title">Concierge AI</h1>
        <div class="subtitle">Private • Ultra Premium</div>
        <div class="status">Sempre al tuo servizio</div>
    </div>

    <div class="actions">
        <div class="action-card" onclick="sendQuick('Analizza il mio patrimonio')">
            <div class="action-icon">💎</div>
            <div class="action-label">Patrimonio</div>
        </div>
        <div class="action-card" onclick="sendQuick('Supporto emotivo personalizzato')">
            <div class="action-icon">🌙</div>
            <div class="action-label">Benessere</div>
        </div>
        <div class="action-card" onclick="sendQuick('Cena stellata stasera')">
            <div class="action-icon">✧</div>
            <div class="action-label">Gastronomia</div>
        </div>
        <div class="action-card" onclick="sendQuick('Organizza la mia settimana')">
            <div class="action-icon">⌛</div>
            <div class="action-label">Agenda</div>
        </div>
    </div>

    <div class="chat-wrapper">
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">
                Buongiorno. Sono il tuo Concierge AI privato.<br>
                In cosa posso servirti oggi?
            </div>
        </div>

        <div class="typing-container" id="typingContainer" style="display:none; padding:0 20px; margin-top:8px;">
            <div class="typing"><span></span><span></span><span></span></div>
        </div>

        <div class="input-wrapper">
            <input type="text" class="input-field" id="messageInput" placeholder="Il tuo desiderio..." onkeypress="handleKeyPress(event)" autocomplete="off">
            <button class="send-btn" id="sendBtn" onclick="sendMessage()">➤</button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    <script>
        // Particelle dorate sottili e lussuose
        particlesJS('particles', {
            particles: {
                number: { value: 40 },
                color: { value: '#D4AF37' },
                shape: { type: 'circle' },
                opacity: { value: 0.4, random: true },
                size: { value: 2, random: true },
                line_linked: { enable: false },
                move: { enable: true, speed: 0.6, direction: 'none', random: true, out_mode: 'out' }
            },
            interactivity: { detect_on: 'canvas', events: { resize: true } }
        });

        // Il resto della logica chat è identica ma più pulita
        const responses = {
            'patrimonio|saldo|finanze': 'Il suo patrimonio liquido ammonta a €2.847.000. Vuole il report dettagliato o preferisce una strategia di ottimizzazione fiscale?',
            'benessere|mood|emotivo': 'Respiro profondo. Sono qui. Vuole una sessione guidata di 5 minuti o preferisce semplicemente parlare?',
            'cena|piatto|gastronomia': 'Stasera le consiglio il nostro Wagyu A5 con tartufo bianco e riduzione al Barolo 1996. Prenoto al tavolo privato?',
            'agenda|settimana|pianifica': 'La sua settimana è già ottimizzata: produttività +26%, benessere +41%. Vuole il calendario visivo?',
            default: 'Perfetto. Sto preparando una risposta su misura per lei...'
        };

        function addMessage(text, isUser = false) {
            const chat = document.getElementById('chatMessages');
            const div = document.createElement('div');
            div.className = 'message ' + (isUser ? 'user' : 'bot');
            div.innerHTML = text;
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }

        function showTyping() {
            document.getElementById('typingContainer').style.display = 'block';
        }
        function hideTyping() {
            document.getElementById('typingContainer').style.display = 'none';
        }

        function getResponse(txt) {
            const lower = txt.toLowerCase();
            for (let key in responses) {
                if (key.split('|').some(k => lower.includes(k))) return responses[key];
            }
            return responses.default;
        }

        function sendQuick(text) {
            Telegram.WebApp.HapticFeedback.impactOccurred('heavy');
            sendMessageText(text);
        }

        function sendMessage() {
            const input = document.getElementById('messageInput');
            const text = input.value.trim();
            if (!text) return;
            sendMessageText(text);
            input.value = '';
        }

        function sendMessageText(text) {
            Telegram.WebApp.HapticFeedback.impactOccurred('medium');
            addMessage(text, true);
            showTyping();
            setTimeout(() => {
                hideTyping();
                addMessage(getResponse(text));
            }, 1800 + Math.random() * 1200);
        }

        function handleKeyPress(e) {
            if (e.key === 'Enter') sendMessage();
        }

        // Fix 100vh mobile
        const setVh = () => document.documentElement.style.setProperty('--vh', window.innerHeight + 'px');
        window.addEventListener('resize', setVh); setVh();
    </script>
    """
    return get_base_template("Concierge AI", content, "agent")
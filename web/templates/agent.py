# web/templates/agent.py - AI Assistant PREMIUM
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template


def generate_agent_page():
    """Pagina AI Assistant PREMIUM - Oro & Nero"""

    content = """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap');

      :root {
        --gold: #D4AF37;
        --gold-light: #F4E5B2;
        --gold-dark: #9B7F1B;
      }

      /* Override base background */
      body { background: #0A0A0A !important; }
      .bg-gradient { opacity: 1 !important; }

      /* PREMIUM HEADER */
      .premium-agent-header {
        text-align: center;
        padding: 40px 20px 20px;
        border-bottom: 1px solid rgba(212,175,55,0.15);
        margin-bottom: 20px;
      }

      .agent-avatar {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, rgba(212,175,55,0.2), rgba(212,175,55,0.05));
        border: 2px solid rgba(212,175,55,0.4);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 42px;
        margin: 0 auto 16px;
        box-shadow: 0 8px 32px rgba(212,175,55,0.3);
        animation: float 4s ease-in-out infinite;
      }

      @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
      }

      .agent-title {
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        font-weight: 700;
        background: linear-gradient(135deg, var(--gold-light), var(--gold));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
        letter-spacing: -0.5px;
      }

      .agent-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 500;
        color: rgba(212,175,55,0.7);
        text-transform: uppercase;
        letter-spacing: 2px;
      }

      .status-indicator {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        margin-top: 12px;
        padding: 6px 14px;
        background: rgba(212,175,55,0.1);
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        color: var(--gold-light);
      }

      .status-dot {
        width: 6px;
        height: 6px;
        background: var(--gold);
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
      }

      @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(0.8); }
      }

      /* QUICK ACTIONS PREMIUM */
      .quick-actions {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        padding: 0 16px 20px;
        max-width: 600px;
        margin: 0 auto;
      }

      .quick-action {
        position: relative;
        padding: 20px 16px;
        background: #1A1A1A;
        border: 1px solid rgba(212,175,55,0.2);
        border-radius: 16px;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        overflow: hidden;
      }

      .quick-action::before {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(212,175,55,0.1), transparent);
        opacity: 0;
        transition: opacity 0.3s;
      }

      .quick-action:active {
        transform: scale(0.97);
        border-color: rgba(212,175,55,0.5);
      }

      .quick-action:active::before {
        opacity: 1;
      }

      .quick-action-icon {
        font-size: 28px;
        margin-bottom: 8px;
        display: block;
        filter: drop-shadow(0 4px 12px rgba(212,175,55,0.3));
      }

      .quick-action-text {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 600;
        color: var(--gold-light);
      }

      /* CHAT PREMIUM */
      .chat-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 0 16px;
      }

      .chat-messages {
        height: 55vh;
        overflow-y: auto;
        padding: 20px;
        background: rgba(26,26,26,0.5);
        border: 1px solid rgba(212,175,55,0.1);
        border-radius: 24px;
        margin-bottom: 16px;
        display: flex;
        flex-direction: column;
        gap: 16px;
        backdrop-filter: blur(10px);
      }

      /* Custom scrollbar */
      .chat-messages::-webkit-scrollbar {
        width: 6px;
      }

      .chat-messages::-webkit-scrollbar-track {
        background: rgba(212,175,55,0.05);
        border-radius: 3px;
      }

      .chat-messages::-webkit-scrollbar-thumb {
        background: rgba(212,175,55,0.3);
        border-radius: 3px;
      }

      .message {
        padding: 16px 20px;
        border-radius: 20px;
        max-width: 85%;
        animation: messageSlide 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        line-height: 1.5;
        position: relative;
      }

      @keyframes messageSlide {
        from { 
          opacity: 0; 
          transform: translateY(20px) scale(0.9);
        }
        to { 
          opacity: 1; 
          transform: translateY(0) scale(1);
        }
      }

      .message.user {
        background: linear-gradient(135deg, var(--gold-dark), var(--gold));
        align-self: flex-end;
        color: #0A0A0A;
        font-weight: 500;
        box-shadow: 0 8px 24px rgba(212,175,55,0.3);
        border: 1px solid rgba(212,175,55,0.3);
      }

      .message.bot {
        background: #1A1A1A;
        align-self: flex-start;
        color: rgba(255,255,255,0.9);
        border: 1px solid rgba(212,175,55,0.2);
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
      }

      .message.bot::before {
        content: '✨';
        position: absolute;
        top: -8px;
        left: 12px;
        font-size: 16px;
        filter: drop-shadow(0 2px 8px rgba(212,175,55,0.5));
      }

      /* TYPING INDICATOR PREMIUM */
      .typing-container {
        display: none;
        padding: 0 16px;
      }

      .typing-container.active {
        display: block;
      }

      .typing {
        display: inline-flex;
        padding: 16px 24px;
        background: #1A1A1A;
        border: 1px solid rgba(212,175,55,0.2);
        border-radius: 20px;
        gap: 6px;
        animation: messageSlide 0.3s ease;
      }

      .typing-dot {
        width: 8px;
        height: 8px;
        background: var(--gold);
        border-radius: 50%;
        animation: typingBounce 1.4s infinite ease-in-out;
      }

      .typing-dot:nth-child(1) { animation-delay: 0s; }
      .typing-dot:nth-child(2) { animation-delay: 0.2s; }
      .typing-dot:nth-child(3) { animation-delay: 0.4s; }

      @keyframes typingBounce {
        0%, 60%, 100% { transform: translateY(0); opacity: 0.7; }
        30% { transform: translateY(-10px); opacity: 1; }
      }

      /* INPUT PREMIUM */
      .input-container {
        max-width: 600px;
        margin: 0 auto;
        padding: 0 16px 16px;
      }

      .input-area {
        display: flex;
        gap: 12px;
        align-items: center;
        background: #1A1A1A;
        border: 2px solid rgba(212,175,55,0.2);
        border-radius: 24px;
        padding: 8px 8px 8px 20px;
        transition: all 0.3s ease;
      }

      .input-area:focus-within {
        border-color: rgba(212,175,55,0.5);
        box-shadow: 0 8px 32px rgba(212,175,55,0.2);
      }

      .input-field {
        flex: 1;
        background: transparent;
        border: none;
        color: var(--gold-light);
        font-size: 15px;
        font-family: 'Inter', sans-serif;
        outline: none;
        padding: 8px 0;
      }

      .input-field::placeholder {
        color: rgba(212,175,55,0.4);
      }

      .send-btn {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--gold), var(--gold-dark));
        border: none;
        color: #0A0A0A;
        font-size: 20px;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 16px rgba(212,175,55,0.4);
      }

      .send-btn:active {
        transform: scale(0.9);
        box-shadow: 0 2px 8px rgba(212,175,55,0.6);
      }

      .send-btn:disabled {
        opacity: 0.4;
        cursor: not-allowed;
      }

      /* SUGGESTIONS */
      .suggestions {
        display: flex;
        gap: 8px;
        padding: 0 16px 16px;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
      }

      .suggestions::-webkit-scrollbar {
        display: none;
      }

      .suggestion-chip {
        flex-shrink: 0;
        padding: 10px 16px;
        background: rgba(212,175,55,0.1);
        border: 1px solid rgba(212,175,55,0.3);
        border-radius: 16px;
        color: var(--gold-light);
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        white-space: nowrap;
      }

      .suggestion-chip:active {
        transform: scale(0.95);
        background: rgba(212,175,55,0.2);
        border-color: rgba(212,175,55,0.5);
      }
    </style>

    <div class="premium-agent-header">
      <div class="agent-avatar">🤖</div>
      <h1 class="agent-title">AI Concierge</h1>
      <div class="agent-subtitle">Premium Assistant</div>
      <div class="status-indicator">
        <span class="status-dot"></span>
        Online 24/7
      </div>
    </div>

    <!-- Quick Actions -->
    <div class="quick-actions">
      <div class="quick-action" onclick="sendQuick('💰 Analizza le mie finanze')">
        <span class="quick-action-icon">💰</span>
        <div class="quick-action-text">Finanza</div>
      </div>
      <div class="quick-action" onclick="sendQuick('🧠 Ho bisogno di supporto mentale')">
        <span class="quick-action-icon">🧠</span>
        <div class="quick-action-text">Benessere</div>
      </div>
      <div class="quick-action" onclick="sendQuick('🍕 Consigliami un piatto')">
        <span class="quick-action-icon">🍕</span>
        <div class="quick-action-text">Gastronomia</div>
      </div>
      <div class="quick-action" onclick="sendQuick('📅 Organizza la mia giornata')">
        <span class="quick-action-icon">📅</span>
        <div class="quick-action-text">Pianifica</div>
      </div>
    </div>

    <!-- Chat -->
    <div class="chat-container">
      <div class="chat-messages" id="chatMessages">
        <div class="message bot">
          Benvenuto. Sono il tuo assistente personale premium. Come posso esserti utile oggi?
        </div>
      </div>
    </div>

    <div class="typing-container" id="typingContainer">
      <div class="typing">
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
      </div>
    </div>

    <!-- Suggestions -->
    <div class="suggestions" id="suggestions">
      <div class="suggestion-chip" onclick="sendQuick('Qual è il mio saldo?')">💳 Saldo</div>
      <div class="suggestion-chip" onclick="sendQuick('Come mi sento oggi?')">😊 Mood</div>
      <div class="suggestion-chip" onclick="sendQuick('Cosa mangio stasera?')">🍽️ Cena</div>
      <div class="suggestion-chip" onclick="sendQuick('Aiutami a risparmiare')">💎 Risparmio</div>
    </div>

    <!-- Input -->
    <div class="input-container">
      <div class="input-area">
        <input 
          type="text" 
          class="input-field" 
          id="messageInput" 
          placeholder="Scrivi un messaggio..."
          onkeypress="handleKeyPress(event)"
        />
        <button class="send-btn" id="sendBtn" onclick="sendMessage()">
          <span>→</span>
        </button>
      </div>
    </div>

    <script>
      const responses = {
        'finanz': 'Sto analizzando il tuo portfolio... Il tuo saldo attuale è di €1.250. Posso aiutarti a ottimizzare i tuoi investimenti.',
        'supporto': 'Capisco che stai cercando supporto. Sono qui per te. Vuoi parlare di come ti senti o preferisci un esercizio di respirazione guidato?',
        'piatto': 'Basandomi sulle tue preferenze, ti consiglio il nostro PizzaBurger premium con mozzarella di bufala. È una delle specialità più apprezzate.',
        'giornata': 'Perfetto! Ho organizzato la tua giornata ottimizzando produttività e benessere. Vuoi vedere il programma dettagliato?',
        'saldo': 'Il tuo saldo corrente è di €1.250,00. Hai speso €327,50 questo mese.',
        'mood': 'Come ti senti oggi? Posso suggerirti esercizi personalizzati per il tuo benessere emotivo.',
        'cena': 'Per cena ti consiglio il nostro Arancino Durger accompagnato da un Tiramisù Shake.',
        'risparmio': 'Analizzando le tue spese, posso aiutarti a risparmiare circa €450/mese. Vuoi vedere i dettagli?',
        'default': 'Ho capito la tua richiesta. Sto elaborando una risposta personalizzata per te...'
      };

      function addMessage(text, isUser) {
        const container = document.getElementById('chatMessages');
        const msg = document.createElement('div');
        msg.className = 'message ' + (isUser ? 'user' : 'bot');
        msg.textContent = text;
        container.appendChild(msg);
        container.scrollTop = container.scrollHeight;
      }

      function showTyping() {
        document.getElementById('typingContainer').classList.add('active');
      }

      function hideTyping() {
        document.getElementById('typingContainer').classList.remove('active');
      }

      function getResponse(text) {
        const lower = text.toLowerCase();
        for (let key in responses) {
          if (lower.includes(key)) {
            return responses[key];
          }
        }
        return responses['default'];
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

        document.getElementById('suggestions').style.display = 'none';

        showTyping();
        setTimeout(() => {
          hideTyping();
          addMessage(getResponse(text), false);
        }, 1500 + Math.random() * 1000);
      }

      function handleKeyPress(event) {
        if (event.key === 'Enter') {
          sendMessage();
        }
      }

      // Auto-resize chat on mobile
      function adjustChatHeight() {
        const vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
      }

      window.addEventListener('resize', adjustChatHeight);
      adjustChatHeight();
    </script>
    """

    return get_base_template("AI Concierge", content, "agent")
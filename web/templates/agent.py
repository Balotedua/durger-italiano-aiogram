# web/templates/agent.py - Pagina Assistente AI H24
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from web.templates.base import get_base_template

def generate_agent_page():
    """Genera pagina Assistente AI"""
    
    content = """
    <div class="page-header">
      <h1>🤖 Assistente AI</h1>
      <p>Il tuo supporto intelligente H24</p>
    </div>
    
    <style>
      .chat-container {
        max-width: 600px;
        margin: 0 auto;
      }
      
      .chat-messages {
        height: 60vh;
        overflow-y: auto;
        padding: 20px;
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        gap: 16px;
      }
      
      .message {
        padding: 16px 20px;
        border-radius: 20px;
        max-width: 80%;
        animation: messageIn 0.3s ease;
      }
      
      @keyframes messageIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
      }
      
      .message.user {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        align-self: flex-end;
        color: white;
      }
      
      .message.bot {
        background: rgba(255,255,255,0.1);
        align-self: flex-start;
        border: 1px solid rgba(255,255,255,0.1);
      }
      
      .quick-actions {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        margin-bottom: 20px;
      }
      
      .quick-btn {
        padding: 16px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
      }
      
      .quick-btn:active {
        transform: scale(0.95);
        background: rgba(99,102,241,0.2);
      }
      
      .quick-btn-icon {
        font-size: 32px;
        margin-bottom: 8px;
      }
      
      .quick-btn-text {
        font-size: 14px;
        font-weight: 600;
      }
      
      .input-area {
        display: flex;
        gap: 12px;
        align-items: center;
      }
      
      .input-field {
        flex: 1;
        padding: 16px 20px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        color: white;
        font-size: 16px;
        outline: none;
      }
      
      .send-btn {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        border: none;
        color: white;
        font-size: 24px;
        cursor: pointer;
        transition: all 0.3s ease;
      }
      
      .send-btn:active {
        transform: scale(0.9);
      }
      
      .typing {
        display: none;
        padding: 16px 20px;
        background: rgba(255,255,255,0.1);
        border-radius: 20px;
        max-width: 80px;
        align-self: flex-start;
      }
      
      .typing.active {
        display: block;
      }
      
      .typing-dots {
        display: flex;
        gap: 4px;
      }
      
      .typing-dots span {
        width: 8px;
        height: 8px;
        background: var(--text-muted);
        border-radius: 50%;
        animation: typingBounce 1.4s infinite ease-in-out;
      }
      
      .typing-dots span:nth-child(1) { animation-delay: 0s; }
      .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
      .typing-dots span:nth-child(3) { animation-delay: 0.4s; }
      
      @keyframes typingBounce {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-10px); }
      }
    </style>
    
    <div class="chat-container">
      <!-- Quick Actions -->
      <div class="quick-actions">
        <div class="quick-btn" onclick="sendQuickMessage('Aiutami con la finanza')">
          <div class="quick-btn-icon">💰</div>
          <div class="quick-btn-text">Finanza</div>
        </div>
        <div class="quick-btn" onclick="sendQuickMessage('Ho bisogno di supporto')">
          <div class="quick-btn-icon">🧠</div>
          <div class="quick-btn-text">Supporto</div>
        </div>
        <div class="quick-btn" onclick="sendQuickMessage('Consigliami un menu')">
          <div class="quick-btn-icon">🍕</div>
          <div class="quick-btn-text">Cibo</div>
        </div>
        <div class="quick-btn" onclick="sendQuickMessage('Organizza la mia giornata')">
          <div class="quick-btn-icon">📅</div>
          <div class="quick-btn-text">Pianifica</div>
        </div>
      </div>
      
      <!-- Chat Messages -->
      <div class="chat-messages" id="chatMessages">
        <div class="message bot">
          Ciao! Sono il tuo assistente personale H24. Come posso aiutarti oggi? 🤖
        </div>
      </div>
      
      <div class="typing" id="typing">
        <div class="typing-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
      
      <!-- Input Area -->
      <div class="input-area">
        <input 
          type="text" 
          class="input-field" 
          id="messageInput" 
          placeholder="Scrivi un messaggio..."
          onkeypress="handleKeyPress(event)"
        />
        <button class="send-btn" onclick="sendMessage()">➤</button>
      </div>
    </div>
    
    <script>
      function addMessage(text, isUser) {
        const messagesDiv = document.getElementById('chatMessages');
        const message = document.createElement('div');
        message.className = 'message ' + (isUser ? 'user' : 'bot');
        message.textContent = text;
        messagesDiv.appendChild(message);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
      }
      
      function showTyping() {
        document.getElementById('typing').classList.add('active');
      }
      
      function hideTyping() {
        document.getElementById('typing').classList.remove('active');
      }
      
      function sendQuickMessage(text) {
        Telegram.WebApp.HapticFeedback.impactOccurred('medium');
        addMessage(text, true);
        
        showTyping();
        setTimeout(() => {
          hideTyping();
          addMessage('Ho capito! Sto elaborando la tua richiesta... 🤔', false);
        }, 1500);
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
          addMessage('Risposta simulata: ' + text, false);
        }, 2000);
      }
      
      function handleKeyPress(event) {
        if (event.key === 'Enter') {
          sendMessage();
        }
      }
    </script>
    """
    
    return get_base_template("Assistente AI", content, "agent")
from config import Config

def generate_home_page():
    return """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Life Assistant</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        /* Stili comuni con Durger King */
        :root {
            --primary: #6366f1;
            --bg: #0a0a0f;
            --text: #ffffff;
        }
        
        .app-container {
            min-height: 100vh;
            background: var(--bg);
            color: var(--text);
        }
        
        .global-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px;
            background: rgba(255,255,255,0.1);
        }
        
        .module-nav {
            display: flex;
            justify-content: center;
            padding: 16px;
            gap: 8px;
        }
        
        .tab {
            padding: 12px;
            border-radius: 12px;
            background: rgba(255,255,255,0.1);
            cursor: pointer;
        }
        
        .tab.active {
            background: var(--primary);
        }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="global-header">
            <div></div> <!-- Spazio vuoto per allineamento -->
            <h1>🤖 Life Assistant</h1>
            <button class="global-cart-btn" onclick="openGlobalCart()">🛒</button>
        </div>

        <div class="module-nav">
            <div class="tab active">🤖</div>
            <div class="tab" onclick="navigateToModule('finance')">💰</div>
            <div class="tab" onclick="navigateToModule('psychology')">🧠</div>
            <div class="tab" onclick="navigateToModule('fitness')">💪</div>
            <div class="tab" onclick="navigateToModule('durger_king')">🍔</div>
        </div>

        <div class="home-content">
            <div class="chat-interface">
                <div class="messages" id="messages">
                    <div class="message bot-message">
                        Ciao! Sono il tuo assistente AI. Come posso aiutarti oggi?
                    </div>
                </div>
                <div class="input-area">
                    <input type="text" id="userInput" placeholder="Scrivi il tuo messaggio...">
                    <button onclick="sendMessage()">Invia</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        function navigateToModule(module) {
            window.location.href = `/${module}`;
        }
        
        function sendMessage() {
            // Implementa chat GPT
            console.log('Messaggio inviato');
        }
        
        function openGlobalCart() {
            alert('Carrello globale');
        }
        
        // Inizializzazione Telegram
        document.addEventListener('DOMContentLoaded', function() {
            Telegram.WebApp.ready();
            Telegram.WebApp.expand();
        });
    </script>
</body>
</html>
"""
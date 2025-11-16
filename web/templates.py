# web/templates.py - Template HTML ULTRA MODERNO
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


def generate_menu_html():
    """Genera HTML menu dinamico SUPER MODERNO"""

    # Genera items HTML
    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<span class="badge">{item["badge"]}</span>' if item["badge"] else ""
        # Delay animazione per effetto cascata
        delay = idx * 0.1
        items_html += f'''
  <div class="item" onclick="add('{item['name']}', {item['price']}, this)" style="animation-delay: {delay}s">
    <div class="item-glow"></div>
    <div class="item-content">
      <div class="emoji-container">
        <span class="emoji">{item['emoji']}</span>
      </div>
      <div class="item-info">
        <h3>{item['name']} {badge}</h3>
        <p>{item['description']}</p>
        <div class="price-container">
          <span class="price">{item['price']:.2f}€</span>
          <button class="add-btn" onclick="event.stopPropagation(); add('{item['name']}', {item['price']}, this.parentElement.parentElement.parentElement.parentElement)">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M10 4V16M4 10H16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
'''

    return f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Durger King Italiano</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

    * {{ 
      margin: 0; 
      padding: 0; 
      box-sizing: border-box; 
    }}

    :root {{
      --primary: #667eea;
      --secondary: #764ba2;
      --accent: #f093fb;
      --text: #2d3748;
      --text-light: #718096;
      --success: #48bb78;
    }}

    body {{
      font-family: 'Poppins', -apple-system, sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
      min-height: 100vh;
      padding: 24px 16px 140px;
      overflow-x: hidden;
      position: relative;
    }}

    /* PARTICLES BACKGROUND */
    .particles {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }}

    .particle {{
      position: absolute;
      background: rgba(255, 255, 255, 0.3);
      border-radius: 50%;
      animation: float-particle 20s infinite ease-in-out;
    }}

    @keyframes float-particle {{
      0%, 100% {{ 
        transform: translate(0, 0) rotate(0deg);
        opacity: 0;
      }}
      10% {{ opacity: 1; }}
      90% {{ opacity: 1; }}
      100% {{ 
        transform: translate(100vw, -100vh) rotate(720deg);
        opacity: 0;
      }}
    }}

    /* HEADER ANIMATIONS */
    @keyframes fadeInUp {{
      from {{ 
        opacity: 0; 
        transform: translateY(40px) scale(0.9);
      }}
      to {{ 
        opacity: 1; 
        transform: translateY(0) scale(1);
      }}
    }}

    @keyframes float {{
      0%, 100% {{ transform: translateY(0px) rotate(-2deg); }}
      50% {{ transform: translateY(-15px) rotate(2deg); }}
    }}

    @keyframes glow {{
      0%, 100% {{ text-shadow: 0 0 20px rgba(255,255,255,0.5); }}
      50% {{ text-shadow: 0 0 40px rgba(255,255,255,0.8), 0 0 60px rgba(102,126,234,0.6); }}
    }}

    .header-container {{
      position: relative;
      z-index: 1;
      text-align: center;
      margin-bottom: 32px;
    }}

    h1 {{
      color: white;
      font-size: 36px;
      font-weight: 800;
      text-shadow: 0 4px 30px rgba(0,0,0,0.4);
      animation: fadeInUp 0.8s ease, float 4s ease-in-out infinite, glow 3s ease-in-out infinite;
      letter-spacing: -1px;
      line-height: 1.2;
    }}

    .subtitle {{
      color: rgba(255,255,255,0.9);
      font-size: 14px;
      font-weight: 600;
      margin-top: 8px;
      animation: fadeInUp 1s ease;
      text-transform: uppercase;
      letter-spacing: 2px;
    }}

    /* ITEMS ULTRA MODERNI */
    .item {{
      position: relative;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(20px);
      border-radius: 28px;
      padding: 0;
      margin: 20px 0;
      box-shadow: 0 10px 40px rgba(0,0,0,0.15);
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      border: 2px solid transparent;
      overflow: hidden;
      animation: fadeInUp 0.6s ease backwards;
      z-index: 1;
    }}

    /* GLOW EFFECT */
    .item-glow {{
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(102,126,234,0.3) 0%, transparent 70%);
      opacity: 0;
      transition: opacity 0.4s;
      pointer-events: none;
    }}

    .item:hover .item-glow {{
      opacity: 1;
      animation: rotate 3s linear infinite;
    }}

    @keyframes rotate {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}

    .item::before {{
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
      transition: left 0.6s;
      pointer-events: none;
    }}

    .item:hover::before {{
      left: 100%;
    }}

    .item:hover {{
      transform: translateY(-8px) scale(1.03);
      box-shadow: 0 20px 60px rgba(102,126,234,0.4);
      border-color: var(--primary);
    }}

    .item:active {{
      transform: scale(0.98);
    }}

    .item-content {{
      display: flex;
      gap: 16px;
      padding: 20px;
      position: relative;
      z-index: 2;
    }}

    /* EMOJI 3D */
    .emoji-container {{
      flex-shrink: 0;
      width: 80px;
      height: 80px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      border-radius: 20px;
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      position: relative;
    }}

    .emoji-container::before {{
      content: '';
      position: absolute;
      inset: -2px;
      background: linear-gradient(135deg, var(--accent), var(--primary));
      border-radius: 20px;
      opacity: 0;
      transition: opacity 0.4s;
      z-index: -1;
    }}

    .item:hover .emoji-container {{
      transform: rotateY(180deg) scale(1.1);
    }}

    .item:hover .emoji-container::before {{
      opacity: 1;
    }}

    .emoji {{
      font-size: 48px;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
      animation: bounce 2s ease-in-out infinite;
    }}

    @keyframes bounce {{
      0%, 100% {{ transform: translateY(0) scale(1); }}
      50% {{ transform: translateY(-5px) scale(1.05); }}
    }}

    .item-info {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 8px;
    }}

    .item h3 {{
      color: var(--text);
      font-size: 20px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      line-height: 1.3;
    }}

    .item p {{
      color: var(--text-light);
      font-size: 13px;
      line-height: 1.5;
      font-weight: 500;
    }}

    .price-container {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 4px;
    }}

    .price {{
      font-weight: 800;
      font-size: 24px;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}

    /* ADD BUTTON */
    .add-btn {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      border: none;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      box-shadow: 0 4px 12px rgba(102,126,234,0.4);
    }}

    .add-btn:hover {{
      transform: rotate(90deg) scale(1.1);
      box-shadow: 0 6px 20px rgba(102,126,234,0.6);
    }}

    .add-btn:active {{
      transform: rotate(90deg) scale(0.95);
    }}

    /* BADGES */
    .badge {{
      display: inline-block;
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      box-shadow: 0 2px 8px rgba(245,87,108,0.4);
      animation: pulse-badge 2s ease-in-out infinite;
    }}

    @keyframes pulse-badge {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
    }}

    /* CART GLASSMORPHISM */
    .cart-container {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 20px 16px;
      background: rgba(255,255,255,0.95);
      backdrop-filter: blur(30px) saturate(180%);
      box-shadow: 0 -8px 32px rgba(0,0,0,0.2);
      z-index: 100;
      border-top: 1px solid rgba(255,255,255,0.3);
      animation: slideUp 0.5s ease;
    }}

    @keyframes slideUp {{
      from {{ transform: translateY(100%); }}
      to {{ transform: translateY(0); }}
    }}

    .cart-info {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      color: var(--text);
      font-weight: 600;
    }}

    .cart-count {{
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      color: white;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 700;
      animation: fadeInUp 0.3s ease;
      box-shadow: 0 4px 12px rgba(102,126,234,0.3);
    }}

    .cart-total {{
      font-size: 24px;
      font-weight: 800;
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}

    /* BUTTON ULTRA MODERNO */
    button#orderBtn {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 50%, var(--accent) 100%);
      background-size: 200% 200%;
      color: white;
      border: none;
      padding: 18px;
      font-size: 18px;
      border-radius: 20px;
      width: 100%;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
      text-transform: uppercase;
      letter-spacing: 1.5px;
      position: relative;
      overflow: hidden;
      animation: gradient 3s ease infinite;
    }}

    @keyframes gradient {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    button#orderBtn::before {{
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      width: 0;
      height: 0;
      border-radius: 50%;
      background: rgba(255,255,255,0.3);
      transform: translate(-50%, -50%);
      transition: width 0.6s, height 0.6s;
    }}

    button#orderBtn:hover {{
      transform: translateY(-4px) scale(1.02);
      box-shadow: 0 15px 40px rgba(102, 126, 234, 0.7);
    }}

    button#orderBtn:hover::before {{
      width: 300px;
      height: 300px;
    }}

    button#orderBtn:active {{
      transform: scale(0.98);
    }}

    button#orderBtn:disabled {{
      opacity: 0.5;
      cursor: not-allowed;
      transform: none;
    }}

    /* ADDED ANIMATION */
    @keyframes explode {{
      0% {{ transform: scale(1); }}
      50% {{ transform: scale(1.15); }}
      100% {{ transform: scale(1); }}
    }}

    .added {{
      animation: explode 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    /* SUCCESS RIPPLE */
    @keyframes ripple {{
      0% {{
        transform: scale(0);
        opacity: 1;
      }}
      100% {{
        transform: scale(2);
        opacity: 0;
      }}
    }}

    .ripple {{
      position: absolute;
      border-radius: 50%;
      background: rgba(72, 187, 120, 0.6);
      width: 100px;
      height: 100px;
      animation: ripple 0.6s ease-out;
      pointer-events: none;
    }}
  </style>
</head>
<body>
  <!-- PARTICLES -->
  <div class="particles" id="particles"></div>

  <div class="header-container">
    <h1>🍕 DURGER KING 🍔<br>ITALIANO</h1>
    <div class="subtitle">Autentico • Delizioso • Italiano</div>
  </div>

  {items_html}

  <div class="cart-container">
    <div class="cart-info">
      <span>🛒 <span class="cart-count" id="cartCount">0 articoli</span></span>
      <span class="cart-total" id="cartTotal">0,00 €</span>
    </div>
    <button id="orderBtn" onclick="sendOrder()">✨ Ordina Ora ✨</button>
  </div>

  <script>
    // PARTICLES SYSTEM
    function createParticles() {{
      const container = document.getElementById('particles');
      for (let i = 0; i < 15; i++) {{
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.width = Math.random() * 10 + 5 + 'px';
        particle.style.height = particle.style.width;
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 20 + 's';
        particle.style.animationDuration = (Math.random() * 10 + 15) + 's';
        container.appendChild(particle);
      }}
    }}

    let cart = [];

    function updateCart() {{
      const count = cart.length;
      const total = cart.reduce((sum, item) => sum + item.price, 0);
      document.getElementById('cartCount').textContent = count + (count === 1 ? ' articolo' : ' articoli');
      document.getElementById('cartTotal').textContent = total.toFixed(2).replace('.', ',') + ' €';
      document.getElementById('orderBtn').disabled = count === 0;
    }}

    function createRipple(x, y) {{
      const ripple = document.createElement('div');
      ripple.className = 'ripple';
      ripple.style.left = x - 50 + 'px';
      ripple.style.top = y - 50 + 'px';
      document.body.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    }}

    function add(name, price, element) {{
      cart.push({{name, price}});
      Telegram.WebApp.HapticFeedback.impactOccurred('heavy');

      // Animazione elemento
      element.classList.add('added');
      setTimeout(() => element.classList.remove('added'), 400);

      // Ripple effect
      const rect = element.getBoundingClientRect();
      createRipple(rect.left + rect.width / 2, rect.top + rect.height / 2);

      updateCart();
    }}

    function sendOrder() {{
      if (cart.length === 0) {{
        Telegram.WebApp.showAlert('🍕 Carrello vuoto! Aggiungi almeno un prodotto.');
        return;
      }}
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      Telegram.WebApp.sendData(JSON.stringify(cart));
      Telegram.WebApp.close();
    }}

    // Init
    createParticles();
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
    updateCart();
  </script>
</body>
</html>
"""
    WebApp.expand();
    updateCart();

"""WebApp.expand();
    updateCart();
  </script>
</body>
</html>
"""
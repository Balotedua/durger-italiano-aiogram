# web/templates.py - Template HTML ULTRA MODERNO MAX POWER
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


def generate_menu_html():
    """Genera HTML menu dinamico SUPER MODERNO MAX EDITION"""

    # Genera items HTML
    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<span class="badge">{item["badge"]}</span>' if item["badge"] else ""
        delay = idx * 0.15
        items_html += f'''
  <div class="item" data-name="{item['name']}" data-price="{item['price']}" style="animation-delay: {delay}s">
    <div class="item-glow"></div>
    <div class="item-shine"></div>
    <div class="item-content">
      <div class="emoji-container">
        <div class="emoji-glow"></div>
        <span class="emoji">{item['emoji']}</span>
      </div>
      <div class="item-info">
        <h3>{item['name']} {badge}</h3>
        <p>{item['description']}</p>
        <div class="price-container">
          <span class="price">{item['price']:.2f}€</span>
          <button class="add-btn" onclick="event.stopPropagation(); addToCart('{item['name']}', {item['price']}, this)">
            <svg class="plus-icon" width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M10 4V16M4 10H16" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
            </svg>
            <svg class="check-icon" width="20" height="20" viewBox="0 0 20 20" fill="none" style="display:none;">
              <path d="M4 10L8 14L16 6" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
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
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');

    * {{ 
      margin: 0; 
      padding: 0; 
      box-sizing: border-box; 
    }}

    :root {{
      --primary: #667eea;
      --secondary: #764ba2;
      --accent: #f093fb;
      --success: #48bb78;
      --warning: #ed8936;
    }}

    body {{
      font-family: 'Poppins', sans-serif;
      background: #0f0f23;
      min-height: 100vh;
      padding: 24px 16px 160px;
      overflow-x: hidden;
      position: relative;
    }}

    /* ANIMATED GRADIENT BACKGROUND */
    body::before {{
      content: '';
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #667eea 75%, #764ba2 100%);
      background-size: 400% 400%;
      animation: gradientShift 15s ease infinite;
      z-index: 0;
    }}

    @keyframes gradientShift {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    /* GEOMETRIC SHAPES FLOATING */
    .shapes {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
      overflow: hidden;
    }}

    .shape {{
      position: absolute;
      opacity: 0.1;
      animation: floatShape 20s infinite ease-in-out;
    }}

    @keyframes floatShape {{
      0%, 100% {{ transform: translate(0, 0) rotate(0deg); }}
      25% {{ transform: translate(50vw, 30vh) rotate(90deg); }}
      50% {{ transform: translate(-20vw, 60vh) rotate(180deg); }}
      75% {{ transform: translate(30vw, -20vh) rotate(270deg); }}
    }}

    /* PARTICLES */
    .particles {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }}

    .particle {{
      position: absolute;
      background: rgba(255, 255, 255, 0.4);
      border-radius: 50%;
      animation: floatParticle 15s infinite ease-in-out;
    }}

    @keyframes floatParticle {{
      0% {{ transform: translate(0, 100vh) scale(0); opacity: 0; }}
      10% {{ opacity: 1; }}
      90% {{ opacity: 1; }}
      100% {{ transform: translate(100vw, -100vh) scale(1); opacity: 0; }}
    }}

    /* HEADER MEGA ANIMATIONS */
    .header-container {{
      position: relative;
      z-index: 2;
      text-align: center;
      margin-bottom: 40px;
      perspective: 1000px;
    }}

    @keyframes float3D {{
      0%, 100% {{ transform: translateY(0) rotateX(0deg) rotateY(0deg); }}
      25% {{ transform: translateY(-20px) rotateX(5deg) rotateY(-5deg); }}
      50% {{ transform: translateY(0) rotateX(0deg) rotateY(5deg); }}
      75% {{ transform: translateY(-10px) rotateX(-5deg) rotateY(0deg); }}
    }}

    @keyframes textGlow {{
      0%, 100% {{ 
        text-shadow: 
          0 0 10px rgba(255,255,255,0.8),
          0 0 20px rgba(255,255,255,0.6),
          0 0 30px rgba(102,126,234,0.4);
      }}
      50% {{ 
        text-shadow: 
          0 0 20px rgba(255,255,255,1),
          0 0 40px rgba(255,255,255,0.8),
          0 0 60px rgba(102,126,234,0.6),
          0 0 80px rgba(118,75,162,0.4);
      }}
    }}

    h1 {{
      color: white;
      font-size: 38px;
      font-weight: 900;
      animation: float3D 6s ease-in-out infinite, textGlow 3s ease-in-out infinite;
      letter-spacing: -1px;
      line-height: 1.2;
      filter: drop-shadow(0 10px 30px rgba(0,0,0,0.5));
    }}

    .subtitle {{
      color: rgba(255,255,255,0.95);
      font-size: 13px;
      font-weight: 700;
      margin-top: 12px;
      text-transform: uppercase;
      letter-spacing: 4px;
      animation: fadeInUp 1.2s ease 0.3s backwards;
    }}

    /* THEME TOGGLE */
    .theme-toggle {{
      position: fixed;
      top: 20px;
      right: 20px;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(10px);
      border: 2px solid rgba(255,255,255,0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 100;
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }}

    .theme-toggle:hover {{
      transform: rotate(180deg) scale(1.1);
      background: rgba(255,255,255,0.3);
    }}

    /* ITEMS ULTRA PREMIUM */
    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(60px) scale(0.9); }}
      to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    .item {{
      position: relative;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(30px) saturate(180%);
      border-radius: 32px;
      margin: 24px 0;
      box-shadow: 
        0 20px 60px rgba(0,0,0,0.3),
        inset 0 1px 0 rgba(255,255,255,0.2);
      cursor: pointer;
      transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      border: 2px solid rgba(255,255,255,0.2);
      overflow: hidden;
      animation: fadeInUp 0.8s ease backwards;
      z-index: 2;
    }}

    /* ROTATING GLOW */
    .item-glow {{
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: conic-gradient(
        from 0deg,
        transparent 0deg,
        rgba(102,126,234,0.4) 90deg,
        rgba(118,75,162,0.4) 180deg,
        rgba(240,147,251,0.4) 270deg,
        transparent 360deg
      );
      opacity: 0;
      transition: opacity 0.5s;
      pointer-events: none;
    }}

    .item:hover .item-glow {{
      opacity: 1;
      animation: rotateGlow 4s linear infinite;
    }}

    @keyframes rotateGlow {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}

    /* SHIMMER EFFECT */
    .item-shine {{
      position: absolute;
      top: 0;
      left: -100%;
      width: 50%;
      height: 100%;
      background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,0.6),
        transparent
      );
      transition: left 0.8s;
      pointer-events: none;
    }}

    .item:hover .item-shine {{
      left: 150%;
    }}

    .item:hover {{
      transform: translateY(-12px) scale(1.03);
      box-shadow: 
        0 30px 80px rgba(102,126,234,0.5),
        inset 0 1px 0 rgba(255,255,255,0.3);
      border-color: rgba(255,255,255,0.4);
    }}

    .item:active {{
      transform: scale(0.97);
    }}

    .item-content {{
      display: flex;
      gap: 20px;
      padding: 24px;
      position: relative;
      z-index: 2;
    }}

    /* EMOJI 3D DELUXE */
    .emoji-container {{
      flex-shrink: 0;
      width: 90px;
      height: 90px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, rgba(102,126,234,0.3), rgba(118,75,162,0.3));
      border-radius: 24px;
      transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
      position: relative;
      box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }}

    .emoji-glow {{
      position: absolute;
      inset: -4px;
      background: linear-gradient(135deg, var(--accent), var(--primary));
      border-radius: 24px;
      opacity: 0;
      filter: blur(10px);
      transition: opacity 0.6s;
      z-index: -1;
    }}

    .item:hover .emoji-container {{
      transform: rotateY(360deg) scale(1.15);
      box-shadow: 0 15px 60px rgba(102,126,234,0.6);
    }}

    .item:hover .emoji-glow {{
      opacity: 1;
    }}

    .emoji {{
      font-size: 52px;
      filter: drop-shadow(0 6px 12px rgba(0,0,0,0.3));
      animation: bounceEmoji 3s ease-in-out infinite;
    }}

    @keyframes bounceEmoji {{
      0%, 100% {{ transform: translateY(0) scale(1) rotate(0deg); }}
      50% {{ transform: translateY(-8px) scale(1.1) rotate(5deg); }}
    }}

    .item-info {{
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 10px;
    }}

    .item h3 {{
      color: white;
      font-size: 21px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
      line-height: 1.3;
      text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }}

    .item p {{
      color: rgba(255,255,255,0.85);
      font-size: 13px;
      line-height: 1.6;
      font-weight: 500;
    }}

    .price-container {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 6px;
    }}

    .price {{
      font-weight: 900;
      font-size: 26px;
      color: white;
      text-shadow: 0 4px 20px rgba(102,126,234,0.8);
      animation: priceGlow 2s ease-in-out infinite;
    }}

    @keyframes priceGlow {{
      0%, 100% {{ 
        text-shadow: 0 4px 20px rgba(102,126,234,0.8);
      }}
      50% {{ 
        text-shadow: 0 4px 30px rgba(240,147,251,1);
      }}
    }}

    /* ADD BUTTON DELUXE */
    .add-btn {{
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: none;
      background: linear-gradient(135deg, var(--success), #38a169);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      box-shadow: 0 8px 24px rgba(72,187,120,0.5);
      position: relative;
    }}

    .add-btn::before {{
      content: '';
      position: absolute;
      inset: -2px;
      background: linear-gradient(135deg, var(--success), #38a169);
      border-radius: 50%;
      opacity: 0;
      filter: blur(8px);
      transition: opacity 0.4s;
      z-index: -1;
    }}

    .add-btn:hover {{
      transform: rotate(90deg) scale(1.2);
      box-shadow: 0 12px 40px rgba(72,187,120,0.8);
    }}

    .add-btn:hover::before {{
      opacity: 1;
    }}

    .add-btn.added {{
      background: linear-gradient(135deg, var(--success), #2f855a);
      animation: successPulse 0.6s ease;
    }}

    @keyframes successPulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.3); }}
    }}

    .add-btn .check-icon {{
      animation: checkBounce 0.5s ease;
    }}

    @keyframes checkBounce {{
      0% {{ transform: scale(0) rotate(-180deg); }}
      50% {{ transform: scale(1.2) rotate(10deg); }}
      100% {{ transform: scale(1) rotate(0deg); }}
    }}

    /* BADGES */
    .badge {{
      display: inline-block;
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      padding: 5px 14px;
      border-radius: 14px;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      box-shadow: 0 4px 16px rgba(245,87,108,0.5);
      animation: badgePulse 2.5s ease-in-out infinite;
    }}

    @keyframes badgePulse {{
      0%, 100% {{ transform: scale(1); box-shadow: 0 4px 16px rgba(245,87,108,0.5); }}
      50% {{ transform: scale(1.08); box-shadow: 0 6px 24px rgba(245,87,108,0.8); }}
    }}

    /* CART MEGA PREMIUM */
    .cart-container {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 24px 16px;
      background: rgba(15,15,35,0.95);
      backdrop-filter: blur(40px) saturate(200%);
      box-shadow: 0 -10px 40px rgba(0,0,0,0.5);
      z-index: 100;
      border-top: 2px solid rgba(255,255,255,0.1);
      animation: slideUpCart 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    @keyframes slideUpCart {{
      from {{ transform: translateY(100%); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    .cart-info {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      color: white;
      font-weight: 700;
    }}

    .cart-count {{
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      color: white;
      padding: 8px 18px;
      border-radius: 24px;
      font-size: 14px;
      font-weight: 800;
      animation: fadeInUp 0.4s ease;
      box-shadow: 0 6px 20px rgba(102,126,234,0.5);
    }}

    .cart-total {{
      font-size: 28px;
      font-weight: 900;
      color: white;
      text-shadow: 0 4px 20px rgba(240,147,251,0.8);
      animation: totalPulse 1.5s ease-in-out infinite;
    }}

    @keyframes totalPulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
    }}

    /* BUTTON ULTIMATE */
    button#orderBtn {{
      background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
      background-size: 300% 300%;
      color: white;
      border: none;
      padding: 20px;
      font-size: 19px;
      border-radius: 24px;
      width: 100%;
      font-weight: 900;
      cursor: pointer;
      transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
      box-shadow: 0 15px 50px rgba(102,126,234,0.6);
      text-transform: uppercase;
      letter-spacing: 2px;
      position: relative;
      overflow: hidden;
      animation: gradientMove 4s ease infinite;
    }}

    @keyframes gradientMove {{
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
      background: rgba(255,255,255,0.4);
      transform: translate(-50%, -50%);
      transition: width 0.8s, height 0.8s;
    }}

    button#orderBtn:hover {{
      transform: translateY(-6px) scale(1.03);
      box-shadow: 0 20px 60px rgba(102,126,234,0.9);
    }}

    button#orderBtn:hover::before {{
      width: 400px;
      height: 400px;
    }}

    button#orderBtn:active {{
      transform: scale(0.96);
    }}

    button#orderBtn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }}

    /* CONFETTI */
    .confetti {{
      position: fixed;
      width: 10px;
      height: 10px;
      background: var(--accent);
      pointer-events: none;
      z-index: 1000;
      animation: confettiFall 3s ease-out forwards;
    }}

    @keyframes confettiFall {{
      to {{
        transform: translateY(100vh) rotate(720deg);
        opacity: 0;
      }}
    }}

    /* RIPPLE EFFECT */
    .ripple {{
      position: absolute;
      border-radius: 50%;
      background: rgba(72,187,120,0.6);
      animation: rippleExpand 0.8s ease-out;
      pointer-events: none;
    }}

    @keyframes rippleExpand {{
      0% {{ width: 0; height: 0; opacity: 1; }}
      100% {{ width: 200px; height: 200px; opacity: 0; }}
    }}

    /* LIGHTNING EFFECT */
    @keyframes lightning {{
      0%, 100% {{ opacity: 0; }}
      10%, 30%, 50% {{ opacity: 1; }}
      20%, 40% {{ opacity: 0; }}
    }}

    .lightning {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(255,255,255,0.3);
      pointer-events: none;
      z-index: 9999;
      animation: lightning 0.5s ease-out;
    }}
  </style>
</head>
<body>
  <!-- SHAPES -->
  <div class="shapes" id="shapes"></div>

  <!-- PARTICLES -->
  <div class="particles" id="particles"></div>

  <!-- THEME TOGGLE -->
  <div class="theme-toggle" onclick="toggleTheme()">
    <span style="font-size: 24px;">🌙</span>
  </div>

  <div class="header-container">
    <h1>🍕 DURGER KING 🍔<br>ITALIANO</h1>
    <div class="subtitle">✨ AUTENTICO • DELIZIOSO • ITALIANO ✨</div>
  </div>

  {items_html}

  <div class="cart-container">
    <div class="cart-info">
      <span>🛒 <span class="cart-count" id="cartCount">0 articoli</span></span>
      <span class="cart-total" id="cartTotal">0,00 €</span>
    </div>
    <button id="orderBtn" onclick="sendOrder()">⚡ ORDINA ORA ⚡</button>
  </div>

  <script>
    // PARTICLES SYSTEM ADVANCED
    function createParticles() {{
      const container = document.getElementById('particles');
      for (let i = 0; i < 25; i++) {{
        const particle = document.createElement('div');
        particle.className = 'particle';
        const size = Math.random() * 8 + 4;
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 15 + 's';
        particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
        container.appendChild(particle);
      }}
    }}

    // GEOMETRIC SHAPES
    function createShapes() {{
      const container = document.getElementById('shapes');
      const shapes = ['◆', '●', '■', '▲', '★'];
      for (let i = 0; i < 10; i++) {{
        const shape = document.createElement('div');
        shape.className = 'shape';
        shape.textContent = shapes[Math.floor(Math.random() * shapes.length)];
        shape.style.fontSize = (Math.random() * 60 + 40) + 'px';
        shape.style.left = Math.random() * 100 + '%';
        shape.style.top = Math.random() * 100 + '%';
        shape.style.animationDelay = Math.random() * 20 + 's';
        shape.style.animationDuration = (Math.random() * 15 + 15) + 's';
        container.appendChild(shape);
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

    // CONFETTI EXPLOSION
    function createConfetti(x, y) {{
      const colors = ['#667eea', '#764ba2', '#f093fb', '#48bb78', '#ed8936'];
      for (let i = 0; i < 20; i++) {{
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = x + 'px';
        confetti.style.top = y + 'px';
        confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.transform = `rotate(${{Math.random() * 360}}deg)`;
        confetti.style.animationDelay = (Math.random() * 0.2) + 's';
        document.body.appendChild(confetti);
        setTimeout(() => confetti.remove(), 3000);
      }}
    }}

    // RIPPLE EFFECT
    function createRipple(x, y) {{
      const ripple = document.createElement('div');
      ripple.className = 'ripple';
      ripple.style.left = (x - 100) + 'px';
      ripple.style.top = (y - 100) + 'px';
      document.body.appendChild(ripple);
      setTimeout(() => ripple.remove(), 800);
    }}

    // LIGHTNING EFFECT
    function createLightning() {{
      const lightning = document.createElement('div');
      lightning.className = 'lightning';
      document.body.appendChild(lightning);
      setTimeout(() => lightning.remove(), 500);
    }}

    // ADD TO CART WITH EFFECTS
    function addToCart(name, price, button) {{
      cart.push({{name, price}});

      // Haptic feedback
      Telegram.WebApp.HapticFeedback.impactOccurred('heavy');

      // Button animation
      const plusIcon = button.querySelector('.plus-icon');
      const checkIcon = button.querySelector('.check-icon');
      plusIcon.style.display = 'none';
      checkIcon.style.display = 'block';
      button.classList.add('added');

      setTimeout(() => {{
        plusIcon.style.display = 'block';
        checkIcon.style.display = 'none';
        button.classList.remove('added');
      }}, 1000);

      // Visual effects
      const rect = button.getBoundingClientRect();
      const x = rect.left + rect.width / 2;
      const y = rect.top + rect.height / 2;

      createConfetti(x, y);
      createRipple(x, y);

      updateCart();
    }}

    // THEME TOGGLE
    let isDark = true;
    function toggleTheme() {{
      isDark = !isDark;
      const toggle = document.querySelector('.theme-toggle span');
      toggle.textContent = isDark ? '🌙' : '☀️';

      if (!isDark) {{
        document.body.style.filter = 'none';
      }}
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    // SEND ORDER WITH LIGHTNING
    function sendOrder() {{
      if (cart.length === 0) {{
        Telegram.WebApp.showAlert('🍕 Carrello vuoto! Aggiungi almeno un prodotto.');
        return;
      }}

      // Lightning effect
      createLightning();

      // Massive confetti
      for (let i = 0; i < 5; i++) {{
        setTimeout(() => {{
          createConfetti(window.innerWidth / 2, window.innerHeight / 2);
        }}, i * 100);
      }}

      // Haptic success
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');

      // Send data
      setTimeout(() => {{
        Telegram.WebApp.sendData(JSON.stringify(cart));
        Telegram.WebApp.close();
      }}, 800);
    }}

    // INIT
    createParticles();
    createShapes();
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
    updateCart();

    // PARALLAX SCROLL EFFECT
    let lastScroll = 0;
    window.addEventListener('scroll', () => {{
      const currentScroll = window.pageYOffset;
      const items = document.querySelectorAll('.item');

      items.forEach((item, index) => {{
        const speed = (index % 2 === 0) ? 0.3 : -0.3;
        const yPos = -(currentScroll * speed);
        item.style.transform = `translateY(${{yPos}}px)`;
      }});

      lastScroll = currentScroll;
    }});

    // ITEM CLICK ANIMATIONS
    document.querySelectorAll('.item').forEach(item => {{
      item.addEventListener('click', function(e) {{
        if (e.target.closest('.add-btn')) return;

        const name = this.dataset.name;
        const price = parseFloat(this.dataset.price);
        const btn = this.querySelector('.add-btn');

        addToCart(name, price, btn);

        // Item explosion effect
        this.style.animation = 'none';
        setTimeout(() => {{
          this.style.animation = '';
        }}, 10);
      }});
    }});

    // EASTER EGG: Triple tap header for disco mode
    let tapCount = 0;
    let tapTimer;
    document.querySelector('.header-container').addEventListener('click', () => {{
      tapCount++;
      clearTimeout(tapTimer);

      if (tapCount === 3) {{
        discoMode();
        tapCount = 0;
      }}

      tapTimer = setTimeout(() => {{
        tapCount = 0;
      }}, 500);
    }});

    function discoMode() {{
      let colors = ['#667eea', '#764ba2', '#f093fb', '#48bb78', '#ed8936', '#f56565'];
      let colorIndex = 0;

      const interval = setInterval(() => {{
        document.body.style.setProperty('--primary', colors[colorIndex % colors.length]);
        document.body.style.setProperty('--secondary', colors[(colorIndex + 1) % colors.length]);
        document.body.style.setProperty('--accent', colors[(colorIndex + 2) % colors.length]);
        colorIndex++;
      }}, 200);

      Telegram.WebApp.HapticFeedback.impactOccurred('heavy');

      setTimeout(() => {{
        clearInterval(interval);
        document.body.style.setProperty('--primary', '#667eea');
        document.body.style.setProperty('--secondary', '#764ba2');
        document.body.style.setProperty('--accent', '#f093fb');
      }}, 3000);
    }}

    // AUTO-ANIMATE ITEMS ON SCROLL INTO VIEW
    const observerOptions = {{
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    }};

    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          entry.target.style.animation = 'fadeInUp 0.8s ease backwards';
        }}
      }});
    }}, observerOptions);

    document.querySelectorAll('.item').forEach(item => {{
      observer.observe(item);
    }});
  </script>
</body>
</html>
"""




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
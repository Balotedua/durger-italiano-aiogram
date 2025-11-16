# web/templates.py - ULTRA MAX POWER EVOLUTION EDITION
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


def generate_menu_html():
    """Genera HTML menu ULTRA MODERNO MAX POWER EVOLUTION"""

    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<span class="badge">{item["badge"]}</span>' if item["badge"] else ""
        delay = idx * 0.12
        items_html += f'''
  <div class="menu-item" data-name="{item['name']}" data-price="{item['price']}" style="animation-delay: {delay}s">
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
        <div class="price-controls">
          <span class="price">{item['price']:.2f}€</span>
          <div class="quantity-controls">
            <button class="qty-btn minus" onclick="event.stopPropagation(); updateQuantity(this, -1)">−</button>
            <span class="quantity">0</span>
            <button class="qty-btn plus" onclick="event.stopPropagation(); updateQuantity(this, 1)">+</button>
          </div>
        </div>
      </div>
    </div>
  </div>
'''

    return f"""
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Durger King Italiano</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&family=Orbitron:wght@700;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #667eea;
      --secondary: #764ba2;
      --accent: #f093fb;
      --success: #48bb78;
      --warning: #ed8936;
      --danger: #f56565;
      --light: #f7fafc;
      --dark: #0f0f23;
      --text: #ffffff;
      --text-muted: rgba(255,255,255,0.75);
      --radius: 28px;
      --transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      --shadow-sm: 0 4px 20px rgba(0,0,0,0.2);
      --shadow-md: 0 15px 50px rgba(0,0,0,0.4);
      --shadow-lg: 0 25px 80px rgba(102,126,234,0.6);
    }}

    [data-theme="light"] {{
      --primary: #5a67d8;
      --secondary: #6b46c1;
      --accent: #e53e9d;
      --text: #1a202c;
      --text-muted: #718096;
      --light: #ffffff;
      --dark: #f7fafc;
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: 'Poppins', sans-serif;
      background: var(--dark);
      color: var(--text);
      min-height: 100vh;
      padding: 20px 16px 170px;
      overflow-x: hidden;
      position: relative;
      transition: var(--transition);
    }}

    /* ANIMATED GRADIENT BACKGROUND */
    .bg-gradient {{
      position: fixed;
      inset: 0;
      background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 35%, var(--accent) 70%, var(--primary) 100%);
      background-size: 400% 400%;
      animation: gradientShift 18s ease infinite;
      z-index: -3;
      filter: blur(80px);
      opacity: 0.7;
    }}

    @keyframes gradientShift {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    /* NEON GRID */
    .grid {{
      position: fixed;
      inset: 0;
      background: 
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(0deg, rgba(255,255,255,0.03) 1px, transparent 1px);
      background-size: 50px 50px;
      z-index: -2;
      animation: gridMove 40s linear infinite;
    }}

    @keyframes gridMove {{
      0% {{ transform: translate(0, 0); }}
      100% {{ transform: translate(50px, 50px); }}
    }}

    /* PARTICLES */
    .particles {{
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: -1;
    }}

    .particle {{
      position: absolute;
      background: var(--accent);
      border-radius: 50%;
      filter: blur(1px);
      animation: floatParticle linear infinite;
    }}

    @keyframes floatParticle {{
      0% {{ transform: translateY(100vh) scale(0); opacity: 0; }}
      10% {{ opacity: 1; }}
      90% {{ opacity: 1; }}
      100% {{ transform: translateY(-100px) scale(1); opacity: 0; }}
    }}

    /* HEADER */
    .header {{
      text-align: center;
      margin-bottom: 32px;
      position: relative;
      z-index: 2;
    }}

    h1 {{
      font-family: 'Orbitron', sans-serif;
      font-size: 42px;
      font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 30px rgba(240,147,251,0.5);
      animation: titleGlow 3s ease-in-out infinite;
      letter-spacing: -1px;
    }}

    @keyframes titleGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 20px rgba(240,147,251,0.6)); }}
      50% {{ filter: drop-shadow(0 0 40px rgba(240,147,251,1)); }}
    }}

    .subtitle {{
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 5px;
      color: var(--text-muted);
      margin-top: 8px;
      animation: fadeInUp 1s ease 0.4s backwards;
    }}

    /* THEME TOGGLE */
    .theme-toggle {{
      position: fixed;
      top: 16px;
      right: 16px;
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(16px);
      border: 2px solid rgba(255,255,255,0.2);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 100;
      transition: var(--transition);
      box-shadow: var(--shadow-sm);
    }}

    .theme-toggle:hover {{
      transform: scale(1.1) rotate(180deg);
      background: rgba(255,255,255,0.25);
    }}

    /* MENU ITEM */
    .menu-item {{
      position: relative;
      background: rgba(255,255,255,0.12);
      backdrop-filter: blur(32px) saturate(180%);
      border-radius: var(--radius);
      margin: 20px 0;
      overflow: hidden;
      cursor: pointer;
      transition: var(--transition);
      border: 1.5px solid rgba(255,255,255,0.15);
      animation: fadeInUp 0.8s ease backwards;
      box-shadow: var(--shadow-sm);
    }}

    .menu-item:hover {{
      transform: translateY(-10px) scale(1.02);
      box-shadow: var(--shadow-lg);
      border-color: var(--accent);
    }}

    .item-glow {{
      position: absolute;
      inset: -50%;
      background: conic-gradient(from 0deg, transparent, var(--primary), var(--accent), transparent);
      opacity: 0;
      transition: opacity 0.5s;
      animation: rotateGlow 6s linear infinite paused;
    }}

    .menu-item:hover .item-glow {{
      opacity: 0.6;
      animation-play-state: running;
    }}

    @keyframes rotateGlow {{
      to {{ transform: rotate(360deg); }}
    }}

    .item-shine {{
      position: absolute;
      top: 0;
      left: -150%;
      width: 50%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
      transition: left 1s;
    }}

    .menu-item:hover .item-shine {{
      left: 150%;
    }}

    .item-content {{
      display: flex;
      gap: 20px;
      padding: 24px;
      position: relative;
      z-index: 2;
    }}

    .emoji-container {{
      flex-shrink: 0;
      width: 84px;
      height: 84px;
      background: linear-gradient(135deg, rgba(102,126,234,0.3), rgba(240,147,251,0.3));
      border-radius: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      transition: var(--transition);
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}

    .emoji-glow {{
      position: absolute;
      inset: -6px;
      background: linear-gradient(135deg, var(--accent), var(--primary));
      border-radius: 24px;
      opacity: 0;
      filter: blur(12px);
      transition: opacity 0.6s;
      z-index: -1;
    }}

    .menu-item:hover .emoji-glow {{
      opacity: 1;
    }}

    .menu-item:hover .emoji-container {{
      transform: scale(1.1) rotate(5deg);
    }}

    .emoji {{
      font-size: 48px;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
    }}

    .item-info h3 {{
      font-size: 20px;
      font-weight: 800;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 8px;
      text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }}

    .item-info p {{
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.5;
      margin: 6px 0;
    }}

    .price-controls {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 8px;
    }}

    .price {{
      font-size: 24px;
      font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .quantity-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255,255,255,0.1);
      border-radius: 20px;
      padding: 4px;
      backdrop-filter: blur(10px);
    }}

    .qty-btn {{
      width: 36px;
      height: 36px;
      border: none;
      border-radius: 50%;
      background: var(--success);
      color: white;
      font-size: 20px;
      font-weight: 900;
      cursor: pointer;
      transition: var(--transition);
      box-shadow: 0 4px 12px rgba(72,187,120,0.4);
    }}

    .qty-btn:hover {{
      transform: scale(1.15);
      box-shadow: 0 6px 20px rgba(72,187,120,0.6);
    }}

    .qty-btn.minus {{
      background: var(--danger);
    }}

    .quantity {{
      min-width: 32px;
      text-align: center;
      font-weight: 700;
      font-size: 16px;
      color: var(--text);
    }}

    .badge {{
      background: linear-gradient(135deg, #f093fb, #f5576c);
      color: white;
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      animation: badgePulse 2s ease-in-out infinite;
    }}

    @keyframes badgePulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.1); }}
    }}

    /* CART */
    .cart-container {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 20px 16px;
      background: rgba(15,15,35,0.97);
      backdrop-filter: blur(40px) saturate(200%);
      border-top: 1.5px solid rgba(255,255,255,0.1);
      box-shadow: 0 -15px 50px rgba(0,0,0,0.5);
      z-index: 100;
      animation: slideUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
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
    }}

    .cart-count {{
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white;
      padding: 8px 16px;
      border-radius: 20px;
      font-weight: 800;
      font-size: 14px;
      box-shadow: var(--shadow-sm);
    }}

    .cart-total {{
      font-size: 28px;
      font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--success));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: pulse 1.8s ease-in-out infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
    }}

    #orderBtn {{
      background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
      background-size: 300% 300%;
      color: white;
      border: none;
      padding: 18px;
      font-size: 18px;
      font-weight: 900;
      border-radius: 24px;
      width: 100%;
      cursor: pointer;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
      animation: gradientMove 5s ease infinite;
      transition: var(--transition);
    }}

    #orderBtn:disabled {{
      opacity: 0.5;
      cursor: not-allowed;
      transform: none !important;
    }}

    #orderBtn::before {{
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at center, rgba(255,255,255,0.3), transparent);
      opacity: 0;
      transition: opacity 0.6s;
    }}

    #orderBtn:hover:not(:disabled)::before {{
      opacity: 1;
    }}

    #orderBtn:hover:not(:disabled) {{
      transform: translateY(-4px) scale(1.02);
      box-shadow: var(--shadow-lg);
    }}

    /* MODAL */
    .modal {{
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.8);
      backdrop-filter: blur(12px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 20px;
      animation: fadeIn 0.4s ease;
    }}

    .modal.active {{
      display: flex;
    }}

    .modal-content {{
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(32px);
      border-radius: var(--radius);
      padding: 24px;
      width: 100%;
      max-width: 400px;
      border: 1.5px solid rgba(255,255,255,0.2);
      box-shadow: var(--shadow-lg);
      animation: modalPop 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    @keyframes modalPop {{
      from {{ transform: scale(0.8); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}

    .order-item {{
      display: flex;
      justify-content: space-between;
      padding: 12px 0;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }}

    .order-total {{
      font-size: 24px;
      font-weight: 900;
      text-align: center;
      margin: 16px 0;
      color: var(--success);
    }}

    .modal-buttons {{
      display: flex;
      gap: 12px;
      margin-top: 20px;
    }}

    .btn {{
      flex: 1;
      padding: 14px;
      border: none;
      border-radius: 20px;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
    }}

    .btn-confirm {{
      background: var(--success);
      color: white;
    }}

    .btn-cancel {{
      background: rgba(255,255,255,0.1);
      color: var(--text);
    }}

    /* CONFETTI */
    .confetti {{
      position: fixed;
      width: 10px;
      height: 10px;
      pointer-events: none;
      z-index: 9999;
      animation: confettiFall linear forwards;
    }}

    @keyframes confettiFall {{
      to {{
        transform: translateY(100vh) rotate(720deg);
        opacity: 0;
      }}
    }}

    /* RIPPLE */
    .ripple {{
      position: absolute;
      border-radius: 50%;
      background: rgba(255,255,255,0.4);
      transform: scale(0);
      animation: ripple 0.6s ease-out;
      pointer-events: none;
    }}

    @keyframes ripple {{
      to {{ transform: scale(4); opacity: 0; }}
    }}

    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(40px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>
</head>
<body>
  <div class="bg-gradient"></div>
  <div class="grid"></div>
  <div class="particles" id="particles"></div>

  <div class="theme-toggle" onclick="toggleTheme()">
    <span id="themeIcon">🌙</span>
  </div>

  <div class="header">
    <h1>🍕 DURGER KING 🍔<br>ITALIANO</h1>
    <div class="subtitle">✨ AUTENTICO • VELOCE • GOURMET ✨</div>
  </div>

  <div id="menu">
    {items_html}
  </div>

  <div class="cart-container">
    <div class="cart-info">
      <div class="cart-count" id="cartCount">0 articoli</div>
      <div class="cart-total" id="cartTotal">0,00 €</div>
    </div>
    <button id="orderBtn" onclick="openOrderModal()" disabled>⚡ ORDINA ORA ⚡</button>
  </div>

  <!-- ORDER MODAL -->
  <div class="modal" id="orderModal">
    <div class="modal-content">
      <h2>Conferma Ordine</h2>
      <div id="orderItems"></div>
      <div class="order-total" id="modalTotal">Totale: 0,00 €</div>
      <div class="modal-buttons">
        <button class="btn btn-cancel" onclick="closeOrderModal()">Annulla</button>
        <button class="btn btn-confirm" onclick="confirmOrder()">Conferma</button>
      </div>
    </div>
  </div>

  <script>
    // === STATE ===
    const cart = [];
    let isDark = true;

    // === UTILS ===
    const $ = (s) => document.querySelector(s);
    const $$ = (s) => document.querySelectorAll(s);

    function formatPrice(price) {{
      return price.toFixed(2).replace('.', ',') + ' €';
    }}

    // === PARTICLES ===
    function createParticles() {{
      const container = $('#particles');
      for (let i = 0; i < 30; i++) {{
        const p = document.createElement('div');
        p.className = 'particle';
        const size = Math.random() * 6 + 3;
        p.style.width = p.style.height = size + 'px';
        p.style.left = Math.random() * 100 + '%';
        p.style.animationDelay = Math.random() * 20 + 's';
        p.style.animationDuration = (Math.random() * 15 + 15) + 's';
        container.appendChild(p);
      }}
    }}

    // === CART LOGIC ===
    function updateQuantity(btn, change) {{
      const item = btn.closest('.menu-item');
      const name = item.dataset.name;
      const price = parseFloat(item.dataset.price);
      const qtySpan = item.querySelector('.quantity');
      let qty = parseInt(qtySpan.textContent) + change;

      if (qty < 0) qty = 0;
      qtySpan.textContent = qty;

      // Update cart
      const existing = cart.find(c => c.name === name);
      if (existing) {{
        existing.quantity = qty;
        if (qty === 0) cart.splice(cart.indexOf(existing), 1);
      }} else if (qty > 0) {{
        cart.push({{ name, price, quantity: qty }});
      }}

      updateCartUI();
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
    }}

    function updateCartUI() {{
      const totalItems = cart.reduce((sum, i) => sum + i.quantity, 0);
      const totalPrice = cart.reduce((sum, i) => sum + i.price * i.quantity, 0);

      $('#cartCount').textContent = totalItems + (totalItems === 1 ? ' articolo' : ' articoli');
      $('#cartTotal').textContent = formatPrice(totalPrice);
      $('#orderBtn').disabled = totalItems === 0;
    }}

    // === MODAL ===
    function openOrderModal() {{
      const itemsDiv = $('#orderItems');
      itemsDiv.innerHTML = '';
      let total = 0;

      cart.forEach(item => {{
        const div = document.createElement('div');
        div.className = 'order-item';
        div.innerHTML = `<span>${{item.name}} × ${{item.quantity}}</span><span>${{formatPrice(item.price * item.quantity)}}</span>`;
        itemsDiv.appendChild(div);
        total += item.price * item.quantity;
      }});

      $('#modalTotal').textContent = 'Totale: ' + formatPrice(total);
      $('#orderModal').classList.add('active');
    }}

    function closeOrderModal() {{
      $('#orderModal').classList.remove('active');
    }}

    function confirmOrder() {{
      closeOrderModal();
      createLightning();
      explodeConfetti();
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      setTimeout(() => {{
        Telegram.WebApp.sendData(JSON.stringify(cart));
        Telegram.WebApp.close();
      }}, 1000);
    }}

    // === EFFECTS ===
    function createConfetti(x, y) {{
      const colors = ['#667eea', '#764ba2', '#f093fb', '#48bb78', '#ed8936'];
      for (let i = 0; i < 25; i++) {{
        const c = document.createElement('div');
        c.className = 'confetti';
        c.style.left = (x + Math.random() * 100 - 50) + 'px';
        c.style.top = (y + Math.random() * 100 - 50) + 'px';
        c.style.background = colors[Math.floor(Math.random() * colors.length)];
        c.style.animationDuration = (Math.random() * 2 + 2) + 's';
        c.style.animationDelay = Math.random() * 0.3 + 's';
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 4000);
      }}
    }}

    function explodeConfetti() {{
      for (let i = 0; i < 6; i++) {{
        setTimeout(() => createConfetti(innerWidth / 2, innerHeight / 2), i * 150);
      }}
    }}

    function createLightning() {{
      const l = document.createElement('div');
      l.style.position = 'fixed';
      l.style.inset = '0';
      l.style.background = 'rgba(255,255,255,0.8)';
      l.style.pointerEvents = 'none';
      l.style.zIndex = '9999';
      l.style.animation = 'lightning 0.6s ease-out';
      document.body.appendChild(l);
      setTimeout(() => l.remove(), 600);
    }}

    // === THEME ===
    function toggleTheme() {{
      isDark = !isDark;
      document.body.setAttribute('data-theme', isDark ? 'dark' : 'light');
      $('#themeIcon').textContent = isDark ? '🌙' : '☀️';
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    // === INIT ===
    document.addEventListener('DOMContentLoaded', () => {{
      createParticles();
      Telegram.WebApp.ready();
      Telegram.WebApp.expand();
      updateCartUI();

      // Tap on item to add 1
      $$('.menu-item').forEach(item => {{
        item.addEventListener('click', function(e) {{
          if (e.target.closest('.qty-btn')) return;
          const plusBtn = this.querySelector('.qty-btn.plus');
          plusBtn.click();
        }});
      }});

      // Easter Egg: 5 tap su header = God Mode
      let taps = 0;
      $('.header').addEventListener('click', () => {{
        taps++;
        if (taps === 5) {{
          godMode();
          taps = 0;
        }}
        setTimeout(() => taps = 0, 1000);
      }});
    }});

    function godMode() {{
      document.body.style.animation = 'rainbow 3s linear infinite';
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      setTimeout(() => document.body.style.animation = '', 5000);
    }}

    // Rainbow animation
    const style = document.createElement('style');
    style.textContent = `
      @keyframes rainbow {{
        0% {{ filter: hue-rotate(0deg); }}
        100% {{ filter: hue-rotate(360deg); }}
      }}
      @keyframes lightning {{
        0%, 100% {{ opacity: 0; }}
        10%, 30% {{ opacity: 1; }}
        20%, 40% {{ opacity: 0; }}
      }}
    `;
    document.head.appendChild(style);
  </script>
</body>
</html>
"""
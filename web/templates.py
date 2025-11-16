import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


def generate_menu_html():
    """IL MENU CHE VINCE IL WEBBY AWARD 2026"""

    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<div class="badge">{item["badge"]}</div>' if item["badge"] else ""
        delay = idx * 0.08
        items_html += f'''
  <div class="menu-card" data-name="{item['name']}" data-price="{item['price']}" style="--delay: {delay}s">
    <div class="card-inner">
      <div class="card-glow"></div>
      <div class="card-shine"></div>
      <div class="card-content">
        <div class="emoji-box">
          <div class="emoji-glow"></div>
          <span class="emoji">{item['emoji']}</span>
        </div>
        <div class="info">
          <h3>{item['name']}</h3>
          {badge}
          <p>{item['description']}</p>
          <div class="price-row">
            <span class="price">{item['price']:.2f}€</span>
            <div class="add-circle" onclick="addToCart(this)">
              <svg class="plus" viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
              <svg class="check" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
'''

    return f"""
<!DOCTYPE html>
<html lang="it" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Durger King Italiano</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700;900&family=Space+Grotesk:wght@700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #6366f1;
      --secondary: #8b5cf6;
      --accent: #ec4899;
      --success: #10b981;
      --danger: #ef4444;
      --bg: #0a0a0f;
      --card: rgba(255,255,255,0.06);
      --text: #ffffff;
      --text-muted: rgba(255,255,255,0.7);
      --radius: 32px;
      --shadow: 0 20px 60px rgba(0,0,0,0.4);
      --transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    [data-theme="light"] {{
      --bg: #f8fafc;
      --card: rgba(255,255,255,0.8);
      --text: #0f172a;
      --text-muted: #64748b;
      --primary: #4f46e5;
      --secondary: #7c3aed;
      --accent: #ec4899;
    }}

    * {{
      margin: 0; padding: 0; box-sizing: border-box;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      tap-highlight-color: transparent;
    }}

    body {{
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100dvh;
      padding: 16px 12px 180px;
      overflow-x: hidden;
      position: relative;
      transition: background 0.5s ease;
    }}

    /* BACKGROUND MAGIC */
    .bg-canvas {{
      position: fixed; inset: 0; z-index: -3;
      background: radial-gradient(circle at 20% 80%, #6366f1 0%, transparent 50%),
                  radial-gradient(circle at 80% 20%, #ec4899 0%, transparent 50%),
                  radial-gradient(circle at 50% 50%, #8b5cf6 0%, transparent 50%);
      background-size: 200% 200%;
      animation: bgFlow 20s ease infinite;
      filter: blur(80px); opacity: 0.6;
    }}

    @keyframes bgFlow {{
      0%, 100% {{ background-position: 0% 50%, 100% 50%, 50% 50%; }}
      50% {{ background-position: 100% 50%, 0% 50%, 50% 50%; }}
    }}

    /* NEON GRID */
    .grid {{
      position: fixed; inset: 0; z-index: -2;
      background: 
        linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px),
        linear-gradient(0deg, rgba(255,255,255,0.02) 1px, transparent 1px);
      background-size: 60px 60px;
      animation: gridDrift 60s linear infinite;
    }}

    @keyframes gridDrift {{
      0% {{ transform: translate(0, 0); }}
      100% {{ transform: translate(60px, 60px); }}
    }}

    /* HEADER */
    .header {{
      text-align: center; margin-bottom: 32px; position: relative; z-index: 10;
    }}

    h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 44px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent), #fff);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-size: 200% 200%;
      animation: titleShine 4s ease infinite;
      letter-spacing: -1.5px;
      filter: drop-shadow(0 8px 30px rgba(236,72,153,0.4));
    }}

    @keyframes titleShine {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    .tagline {{
      font-size: 14px; font-weight: 600; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: 6px; margin-top: 8px;
      animation: fadeIn 1s ease 0.5s backwards;
    }}

    /* THEME TOGGLE */
    .theme-toggle {{
      position: fixed; top: 16px; right: 16px; z-index: 100;
      width: 60px; height: 60px; border-radius: 50%;
      background: rgba(255,255,255,0.1); backdrop-filter: blur(16px);
      border: 2px solid rgba(255,255,255,0.15);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: var(--transition);
      box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}

    .theme-toggle:hover {{
      transform: scale(1.15) rotate(360deg);
      background: rgba(255,255,255,0.2);
    }}

    /* MENU CARD – GOD LEVEL */
    .menu-card {{
      margin: 20px 0; animation: floatIn var(--delay, 0s) 0.8s ease backwards;
      transform: translateZ(0); perspective: 1000px;
    }}

    @keyframes floatIn {{
      from {{ opacity: 0; transform: translateY(60px) scale(0.9) rotateX(-15deg); }}
      to {{ opacity: 1; transform: translateY(0) scale(1) rotateX(0deg); }}
    }}

    .card-inner {{
      position: relative; border-radius: var(--radius);
      background: var(--card); backdrop-filter: blur(32px) saturate(180%);
      overflow: hidden; cursor: pointer;
      border: 1.5px solid rgba(255,255,255,0.1);
      transition: var(--transition);
      box-shadow: var(--shadow);
    }}

    .menu-card:hover .card-inner {{
      transform: translateY(-16px) scale(1.04);
      box-shadow: 0 40px 100px rgba(99,102,241,0.6);
      border-color: var(--accent);
    }}

    .card-glow {{
      position: absolute; inset: -100%;
      background: conic-gradient(from 0deg at 50% 50%, 
        transparent, var(--primary), var(--accent), var(--secondary), transparent);
      opacity: 0; transition: opacity 0.6s;
      animation: spinGlow 8s linear infinite paused;
    }}

    .menu-card:hover .card-glow {{
      opacity: 0.7; animation-play-state: running;
    }}

    @keyframes spinGlow {{
      to {{ transform: rotate(360deg); }}
    }}

    .card-shine {{
      position: absolute; top: 0; left: -150%; width: 60%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.8), transparent);
      transition: left 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .menu-card:hover .card-shine {{
      left: 150%;
    }}

    .card-content {{
      display: flex; gap: 20px; padding: 28px; position: relative; z-index: 2;
    }}

    .emoji-box {{
      flex-shrink: 0; width: 88px; height: 88px;
      background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(236,72,153,0.2));
      border-radius: 28px; display: flex; align-items: center; justify-content: center;
      position: relative; transition: var(--transition);
      box-shadow: 0 12px 40px rgba(0,0,0,0.3);
    }}

    .emoji-glow {{
      position: absolute; inset: -8px; border-radius: 28px;
      background: linear-gradient(135deg, var(--accent), var(--primary));
      opacity: 0; filter: blur(16px); transition: opacity 0.6s; z-index: -1;
    }}

    .menu-card:hover .emoji-glow {{
      opacity: 1;
    }}

    .menu-card:hover .emoji-box {{
      transform: scale(1.2) rotate(8deg);
    }}

    .emoji {{
      font-size: 52px; filter: drop-shadow(0 6px 16px rgba(0,0,0,0.4));
      animation: floatEmoji 3s ease-in-out infinite;
    }}

    @keyframes floatEmoji {{
      0%, 100% {{ transform: translateY(0) scale(1); }}
      50% {{ transform: translateY(-10px) scale(1.1); }}
    }}

    .info h3 {{
      font-size: 22px; font-weight: 900; color: var(--text);
      margin-bottom: 6px; text-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }}

    .info p {{
      font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 8px 0 12px;
    }}

    .price-row {{
      display: flex; justify-content: space-between; align-items: center;
    }}

    .price {{
      font-size: 28px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .add-circle {{
      width: 56px; height: 56px; border-radius: 50%;
      background: var(--success); color: white;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: var(--transition);
      box-shadow: 0 8px 32px rgba(16,185,129,0.5);
      position: relative; overflow: hidden;
    }}

    .add-circle:hover {{
      transform: scale(1.2) rotate(90deg);
      box-shadow: 0 12px 50px rgba(16,185,129,0.8);
    }}

    .add-circle.added {{
      background: var(--success);
      animation: pulseSuccess 0.6s ease;
    }}

    @keyframes pulseSuccess {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.4); }}
    }}

    .add-circle svg {{
      width: 28px; height: 28px; fill: currentColor;
    }}

    .add-circle .check {{ display: none; }}
    .add-circle.added .plus {{ display: none; }}
    .add-circle.added .check {{ display: block; animation: checkPop 0.5s ease; }}

    @keyframes checkPop {{
      0% {{ transform: scale(0) rotate(-180deg); }}
      60% {{ transform: scale(1.3) rotate(10deg); }}
      100% {{ transform: scale(1) rotate(0deg); }}
    }}

    .badge {{
      background: linear-gradient(135deg, #f43f5e, #ec4899);
      color: white; padding: 6px 16px; border-radius: 16px;
      font-size: 11px; font-weight: 800; text-transform: uppercase;
      letter-spacing: 1px; margin-top: 8px; display: inline-block;
      animation: badgeFloat 2.5s ease-in-out infinite;
      box-shadow: 0 6px 20px rgba(244,63,94,0.5);
    }}

    @keyframes badgeFloat {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-4px); }}
    }}

    /* CART – MINIMAL GOD */
    .cart-bar {{
      position: fixed; bottom: 0; left: 0; right: 0;
      padding: 20px 16px; background: rgba(10,10,15,0.97);
      backdrop-filter: blur(40px); border-top: 1.5px solid rgba(255,255,255,0.1);
      box-shadow: 0 -20px 60px rgba(0,0,0,0.6); z-index: 100;
      animation: riseUp 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    @keyframes riseUp {{
      from {{ transform: translateY(100%); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    .cart-summary {{
      display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;
    }}

    .cart-badge {{
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white; padding: 10px 20px; border-radius: 24px;
      font-weight: 800; font-size: 15px; box-shadow: 0 8px 32px rgba(99,102,241,0.5);
    }}

    .cart-total {{
      font-size: 32px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--success));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      animation: totalGlow 2s ease-in-out infinite;
    }}

    @keyframes totalGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 20px rgba(16,185,129,0.6)); }}
      50% {{ filter: drop-shadow(0 0 40px rgba(16,185,129,1)); }}
    }}

    #orderBtn {{
      background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
      background-size: 300% 300%; color: white; border: none;
      padding: 20px; font-size: 19px; font-weight: 900; border-radius: 28px;
      width: 100%; cursor: pointer; text-transform: uppercase;
      letter-spacing: 2px; position: relative; overflow: hidden;
      box-shadow: 0 20px 60px rgba(99,102,241,0.6);
      animation: gradientPulse 5s ease infinite;
      transition: var(--transition);
    }}

    @keyframes gradientPulse {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    #orderBtn:disabled {{
      opacity: 0.4; cursor: not-allowed; transform: none !important;
    }}

    #orderBtn::before {{
      content: ''; position: absolute; inset: 0;
      background: radial-gradient(circle at center, rgba(255,255,255,0.4), transparent);
      opacity: 0; transition: opacity 0.6s;
    }}

    #orderBtn:hover:not(:disabled)::before {{
      opacity: 1;
    }}

    #orderBtn:hover:not(:disabled) {{
      transform: translateY(-6px) scale(1.03);
      box-shadow: 0 30px 80px rgba(99,102,241,0.9);
    }}

    /* MODAL – PURE ELEGANCE */
    .modal {{
      position: fixed; inset: 0; background: rgba(0,0,0,0.85);
      backdrop-filter: blur(16px); display: none; align-items: center;
      justify-content: center; z-index: 1000; padding: 20px;
    }}

    .modal.active {{ display: flex; }}

    .modal-card {{
      background: var(--card); backdrop-filter: blur(40px);
      border-radius: var(--radius); padding: 32px; width: 100%;
      max-width: 420px; border: 1.5px solid rgba(255,255,255,0.15);
      box-shadow: var(--shadow); animation: modalRise 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    @keyframes modalRise {{
      from {{ transform: scale(0.7) translateY(100px); opacity: 0; }}
      to {{ transform: scale(1) translateY(0); opacity: 1; }}
    }}

    .order-list {{ margin: 20px 0; max-height: 40vh; overflow-y: auto; }}
    .order-item {{ display: flex; justify-content: space-between; padding: 14px 0;
      border-bottom: 1px solid rgba(255,255,255,0.1); font-size: 16px; }}
    .order-total {{ font-size: 28px; font-weight: 900; text-align: center; margin: 20px 0;
      color: var(--success); }}

    .modal-actions {{ display: flex; gap: 16px; margin-top: 24px; }}
    .btn {{ flex: 1; padding: 16px; border: none; border-radius: 24px;
      font-weight: 700; cursor: pointer; transition: var(--transition); }}
    .btn-cancel {{ background: rgba(255,255,255,0.1); color: var(--text); }}
    .btn-confirm {{ background: var(--success); color: white; }}

    /* EFFECTS */
    .confetti {{
      position: fixed; width: 12px; height: 12px; pointer-events: none;
      z-index: 9999; animation: confettiDrop linear forwards;
    }}

    @keyframes confettiDrop {{
      to {{ transform: translateY(120dvh) rotate(900deg); opacity: 0; }}
    }}

    .ripple {{
      position: absolute; border-radius: 50%; background: rgba(255,255,255,0.5);
      transform: scale(0); animation: ripplePop 0.7s ease-out; pointer-events: none;
    }}

    @keyframes ripplePop {{
      to {{ transform: scale(4); opacity: 0; }}
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; }} to {{ opacity: 1; }}
    }}
  </style>
</head>
<body>
  <div class="bg-canvas"></div>
  <div class="grid"></div>

  <div class="theme-toggle" onclick="toggleTheme()">
    <span id="themeIcon">🌙</span>
  </div>

  <div class="header">
    <h1>DURGER KING<br>ITALIANO</h1>
    <div class="tagline">PIÙ BUONO DELL'ORIGINALE</div>
  </div>

  <div id="menu">{items_html}</div>

  <div class="cart-bar">
    <div class="cart-summary">
      <div class="cart-badge" id="cartBadge">0 articoli</div>
      <div class="cart-total" id="cartTotal">0,00 €</div>
    </div>
    <button id="orderBtn" onclick="openModal()" disabled>ORDINA ORA</button>
  </div>

  <!-- MODAL -->
  <div class="modal" id="modal">
    <div class="modal-card">
      <h2>Conferma Ordine</h2>
      <div class="order-list" id="orderList"></div>
      <div class="order-total" id="modalTotal">Totale: 0,00 €</div>
      <div class="modal-actions">
        <button class="btn btn-cancel" onclick="closeModal()">Annulla</button>
        <button class="btn btn-confirm" onclick="sendOrder()">Conferma</button>
      </div>
    </div>
  </div>

  <script>
    // STATE
    const cart = [];
    let isDark = true;

    // DOM
    const $ = s => document.querySelector(s);
    const $$ = s => document.querySelectorAll(s);

    // FORMAT
    const fmt = p => p.toFixed(2).replace('.', ',') + ' €';

    // ADD TO CART
    function addToCart(btn) {{
      const card = btn.closest('.menu-card');
      const name = card.dataset.name;
      const price = parseFloat(card.dataset.price);

      const existing = cart.find(i => i.name === name);
      if (existing) {{
        existing.qty++;
      }} else {{
        cart.push({{ name, price, qty: 1 }});
      }}

      btn.classList.add('added');
      createRipple(btn);
      createConfetti(btn.getBoundingClientRect());
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');

      setTimeout(() => btn.classList.remove('added'), 800);
      updateCart();
    }}

    // UPDATE CART
    function updateCart() {{
      const totalItems = cart.reduce((s, i) => s + i.qty, 0);
      const totalPrice = cart.reduce((s, i) => s + i.price * i.qty, 0);

      $('#cartBadge').textContent = totalItems + (totalItems === 1 ? ' articolo' : ' articoli');
      $('#cartTotal').textContent = fmt(totalPrice);
      $('#orderBtn').disabled = totalItems === 0;
    }}

    // MODAL
    function openModal() {{
      const list = $('#orderList');
      list.innerHTML = '';
      let total = 0;

      cart.forEach(item => {{
        const div = document.createElement('div');
        div.className = 'order-item';
        div.innerHTML = `<span>${{item.name}} × ${{item.qty}}</span><span>${{fmt(item.price * item.qty)}}</span>`;
        list.appendChild(div);
        total += item.price * item.qty;
      }});

      $('#modalTotal').textContent = 'Totale: ' + fmt(total);
      $('#modal').classList.add('active');
    }}

    function closeModal() {{
      $('#modal').classList.remove('active');
    }}

    function sendOrder() {{
      closeModal();
      explodeConfetti();
      createLightning();
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      setTimeout(() => {{
        Telegram.WebApp.sendData(JSON.stringify(cart));
        Telegram.WebApp.close();
      }}, 1200);
    }}

    // EFFECTS
    function createRipple(el) {{
      const rect = el.getBoundingClientRect();
      const ripple = document.createElement('div');
      ripple.className = 'ripple';
      ripple.style.left = (rect.width / 2) + 'px';
      ripple.style.top = (rect.height / 2) + 'px';
      el.appendChild(ripple);
      setTimeout(() => ripple.remove(), 700);
    }}

    function createConfetti(rect) {{
      const colors = ['#6366f1', '#8b5cf6', '#ec4899', '#10b981'];
      for (let i = 0; i < 30; i++) {{
        const c = document.createElement('div');
        c.className = 'confetti';
        c.style.left = (rect.left + rect.width / 2 + (Math.random() - 0.5) * 100) + 'px';
        c.style.top = (rect.top + rect.height / 2 + (Math.random() - 0.5) * 100) + 'px';
        c.style.background = colors[Math.floor(Math.random() * colors.length)];
        c.style.animationDuration = (Math.random() * 2 + 2) + 's';
        c.style.animationDelay = Math.random() * 0.3 + 's';
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 4000);
      }}
    }}

    function explodeConfetti() {{
      for (let i = 0; i < 8; i++) {{
        setTimeout(() => createConfetti({{ left: innerWidth/2, top: innerHeight/2, width: 0, height: 0 }}), i * 120);
      }}
    }}

    function createLightning() {{
      const l = document.createElement('div');
      l.style.cssText = 'position:fixed;inset:0;background:rgba(255,255,255,0.9);pointer-events:none;z-index:9999;animation:flash 0.8s ease-out';
      document.body.appendChild(l);
      setTimeout(() => l.remove(), 800);
    }}

    // THEME
    function toggleTheme() {{
      isDark = !isDark;
      document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
      $('#themeIcon').textContent = isDark ? '🌙' : '☀️';
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
    }}

    // INIT
    document.addEventListener('DOMContentLoaded', () => {{
      Telegram.WebApp.ready(); Telegram.WebApp.expand();
      updateCart();

      // GOD MODE EASTER EGG: 7 tap su header
      let taps = 0;
      $('.header').addEventListener('click', () => {{
        if (++taps === 7) {{
          document.body.style.filter = 'hue-rotate(360deg) brightness(1.5)';
          setTimeout(() => document.body.style.filter = '', 3000);
          Telegram.WebApp.HapticFeedback.notificationOccurred('success');
          taps = 0;
        }}
        setTimeout(() => taps = 0, 1500);
      }});

      // Add flash style
      const style = document.createElement('style');
      style.textContent = `@keyframes flash {{ 0%,100% {{opacity:0}} 10%,30% {{opacity:1}} 20%,40% {{opacity:0}} }}`;
      document.head.appendChild(style);
    }});
  </script>
</body>
</html>
"""
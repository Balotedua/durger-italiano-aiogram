# web/templates.py - 3D ZEN WOW+ ULTIMATE EDITION
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


def generate_menu_html():
    """IL MENU CHE TI FA DIRE "MA È UN GIOCO O UN RISTORANTE?" """

    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<div class="badge">{item["badge"]}</div>' if item["badge"] else ""
        items_html += f'''
  <div class="card" data-name="{item['name']}" data-price="{item['price']}" data-emoji="{item['emoji']}" onclick="openPreview(this)">
    <div class="card-inner">
      <div class="emoji-glow"></div>
      <div class="emoji">{item['emoji']}</div>
      <div class="info">
        <h3>{item['name']}</h3>
        {badge}
        <p>{item['description']}</p>
      </div>
      <div class="price">{item['price']:.2f}€</div>
      <div class="add-btn" onclick="event.stopPropagation(); addToCart(this.closest('.card'))">
        <svg class="plus" viewBox="0 0 24 24"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>
        <svg class="check" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
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
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;700;900&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js" type="module"></script>
  <style>
    :root {{
      --bg: #0f0f1a;
      --card: rgba(255,255,255,0.08);
      --text: #ffffff;
      --text-muted: rgba(255,255,255,0.75);
      --accent: #ff2e63;
      --success: #06ffa5;
      --radius: 36px;
      --shadow: 0 30px 80px rgba(0,0,0,0.5);
      --transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    [data-theme="light"] {{
      --bg: #fafafa;
      --card: rgba(255,255,255,0.85);
      --text: #0f172a;
      --text-muted: #64748b;
      --accent: #e11d48;
      --success: #059669;
      --shadow: 0 20px 60px rgba(0,0,0,0.15);
    }}

    * {{
      margin: 0; padding: 0; box-sizing: border-box;
      font-family: 'Inter', sans-serif;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      background: var(--bg);
      color: var(--text);
      min-height: 100dvh;
      padding: 20px 16px 180px;
      overflow-x: hidden;
      transition: background 0.6s ease;
    }}

    /* AURA BACKGROUND */
    .aura {{
      position: fixed; inset: 0; z-index: -2;
      background: 
        radial-gradient(circle at 25% 75%, var(--accent) 0%, transparent 50%),
        radial-gradient(circle at 75% 25%, #8b5cf6 0%, transparent 50%);
      filter: blur(100px); opacity: 0.7;
      animation: pulse 10s ease infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); opacity: 0.7; }}
      50% {{ transform: scale(1.4); opacity: 0.9; }}
    }}

    /* HEADER */
    .header {{
      text-align: center; margin-bottom: 40px; position: relative; z-index: 10;
    }}

    h1 {{
      font-size: 52px; font-weight: 900; letter-spacing: -2.5px;
      background: linear-gradient(135deg, #fff, var(--accent), #8b5cf6);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 12px 40px rgba(255,46,99,0.4));
      animation: glow 3s ease infinite;
    }}

    @keyframes glow {{
      0%, 100% {{ filter: drop-shadow(0 12px 40px rgba(255,46,99,0.4)); }}
      50% {{ filter: drop-shadow(0 16px 60px rgba(255,46,99,0.7)); }}
    }}

    .tagline {{
      font-size: 15px; color: var(--text-muted); margin-top: 10px;
      letter-spacing: 5px; text-transform: uppercase; font-weight: 600;
    }}

    /* THEME TOGGLE */
    .theme-toggle {{
      position: fixed; top: 16px; right: 16px; z-index: 100;
      width: 60px; height: 60px; border-radius: 50%;
      background: rgba(255,255,255,0.12); backdrop-filter: blur(16px);
      border: 2px solid rgba(255,255,255,0.15);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: var(--transition);
      box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }}

    .theme-toggle:hover {{
      transform: scale(1.15) rotate(360deg);
      background: rgba(255,255,255,0.2);
    }}

    /* CARD */
    .card {{
      margin: 28px 0; animation: rise 0.9s ease backwards;
      animation-delay: calc(var(--i, 0) * 0.12s);
      transform-style: preserve-3d;
    }}

    @keyframes rise {{
      from {{ opacity: 0; transform: translateY(50px) scale(0.94); }}
      to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    .card-inner {{
      background: var(--card); backdrop-filter: blur(36px);
      border-radius: var(--radius); padding: 32px;
      display: flex; align-items: center; gap: 24px;
      position: relative; overflow: hidden;
      border: 1.5px solid rgba(255,255,255,0.12);
      box-shadow: var(--shadow);
      transition: var(--transition);
      cursor: pointer;
    }}

    .card:hover .card-inner {{
      transform: translateY(-14px) scale(1.04) rotateX(2deg);
      border-color: var(--accent);
      box-shadow: 0 50px 120px rgba(255,46,99,0.4);
    }}

    .emoji-glow {{
      position: absolute; inset: -10px; border-radius: 28px;
      background: linear-gradient(135deg, var(--accent), #8b5cf6);
      opacity: 0; filter: blur(20px); transition: opacity 0.6s;
      z-index: -1;
    }}

    .card:hover .emoji-glow {{
      opacity: 0.8;
    }}

    .emoji {{
      font-size: 64px; width: 96px; height: 96px;
      display: flex; align-items: center; justify-content: center;
      background: rgba(255,46,99,0.15);
      border-radius: 28px;
      transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .card:hover .emoji {{
      transform: scale(1.25) rotate(15deg);
    }}

    .info h3 {{
      font-size: 24px; font-weight: 900; margin-bottom: 6px;
    }}

    .info p {{
      font-size: 15px; color: var(--text-muted); line-height: 1.5;
    }}

    .price {{
      font-size: 30px; font-weight: 900; margin-left: auto;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .add-btn {{
      width: 60px; height: 60px; border-radius: 50%;
      background: var(--success); color: white;
      display: flex; align-items: center; justify-content: center;
      margin-left: 16px; cursor: pointer;
      transition: var(--transition);
      box-shadow: 0 10px 40px rgba(6,255,165,0.5);
      position: relative; overflow: hidden;
    }}

    .add-btn svg {{
      width: 30px; height: 30px; fill: currentColor;
    }}

    .add-btn .check {{ display: none; }}
    .add-btn.added .plus {{ display: none; }}
    .add-btn.added .check {{ display: block; animation: check 0.5s ease; }}

    @keyframes check {{
      0% {{ transform: scale(0) rotate(-180deg); }}
      60% {{ transform: scale(1.3); }}
      100% {{ transform: scale(1); }}
    }}

    .add-btn.added {{
      animation: pulse 0.6s ease;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.5); }}
    }}

    .badge {{
      background: linear-gradient(135deg, var(--accent), #8b5cf6);
      color: white; padding: 8px 16px; border-radius: 18px;
      font-size: 12px; font-weight: 800; margin-top: 8px;
      display: inline-block; animation: float 2.5s ease infinite;
      box-shadow: 0 6px 24px rgba(255,46,99,0.4);
    }}

    @keyframes float {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-6px); }}
    }}

    /* CART */
    .cart {{
      position: fixed; bottom: 0; left: 0; right: 0;
      padding: 24px 20px; background: rgba(15,15,25,0.96);
      backdrop-filter: blur(40px); border-top: 1.5px solid rgba(255,255,255,0.12);
      box-shadow: 0 -25px 80px rgba(0,0,0,0.6); z-index: 100;
    }}

    .cart-summary {{
      display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;
    }}

    .cart-badge {{
      background: linear-gradient(135deg, var(--accent), #8b5cf6);
      color: white; padding: 10px 20px; border-radius: 24px;
      font-weight: 800; font-size: 16px;
      box-shadow: 0 8px 32px rgba(255,46,99,0.4);
    }}

    .cart-total {{
      font-size: 34px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--success));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    #orderBtn {{
      background: linear-gradient(135deg, var(--accent), #8b5cf6);
      color: white; border: none; padding: 22px;
      font-size: 19px; font-weight: 900; border-radius: 30px;
      width: 100%; cursor: pointer; text-transform: uppercase;
      letter-spacing: 2px; position: relative; overflow: hidden;
      box-shadow: 0 25px 70px rgba(255,46,99,0.5);
      transition: var(--transition);
    }}

    #orderBtn:disabled {{
      opacity: 0.4; cursor: not-allowed;
    }}

    #orderBtn:hover:not(:disabled) {{
      transform: translateY(-6px) scale(1.02);
      box-shadow: 0 35px 90px rgba(255,46,99,0.8);
    }}

    /* 3D PREVIEW MODAL */
    .preview-modal {{
      position: fixed; inset: 0; background: rgba(0,0,0,0.9);
      backdrop-filter: blur(16px); display: none; align-items: center;
      justify-content: center; z-index: 1000; padding: 20px;
    }}

    .preview-modal.active {{ display: flex; }}

    .preview-card {{
      background: var(--card); backdrop-filter: blur(40px);
      border-radius: var(--radius); width: 100%; max-width: 420px;
      padding: 32px; text-align: center;
      border: 1.5px solid rgba(255,255,255,0.15);
      box-shadow: var(--shadow);
      animation: pop 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    @keyframes pop {{
      from {{ transform: scale(0.7); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}

    model-viewer {{
      width: 100%; height: 280px; border-radius: 24px;
      margin: 20px 0; background: #111;
      --poster-color: transparent;
    }}

    .preview-title {{
      font-size: 26px; font-weight: 900; margin-bottom: 12px;
    }}

    .preview-desc {{
      color: var(--text-muted); margin-bottom: 20px; line-height: 1.6;
    }}

    .preview-actions {{
      display: flex; gap: 16px;
    }}

    .btn {{
      flex: 1; padding: 16px; border: none; border-radius: 24px;
      font-weight: 700; cursor: pointer; transition: var(--transition);
    }}

    .btn-close {{ background: rgba(255,255,255,0.1); color: var(--text); }}
    .btn-add {{ background: var(--success); color: white; }}

    /* ORDER SUMMARY MODAL */
    .order-modal {{
      position: fixed; inset: 0; background: rgba(0,0,0,0.85);
      backdrop-filter: blur(16px); display: none; align-items: center;
      justify-content: center; z-index: 1000; padding: 20px;
    }}

    .order-modal.active {{ display: flex; }}

    .order-card {{
      background: var(--card); backdrop-filter: blur(40px);
      border-radius: var(--radius); width: 100%; max-width: 420px;
      padding: 32px; border: 1.5px solid rgba(255,255,255,0.15);
      box-shadow: var(--shadow);
    }}

    .order-item {{
      display: flex; justify-content: space-between; padding: 16px 0;
      border-bottom: 1px solid rgba(255,255,255,0.1); font-size: 17px;
    }}

    .order-total {{
      font-size: 28px; font-weight: 900; text-align: center; margin: 24px 0;
      color: var(--success);
    }}

    /* EFFECTS */
    .ripple {{
      position: absolute; border-radius: 50%; background: rgba(255,255,255,0.6);
      transform: scale(0); animation: ripple 0.7s ease-out; pointer-events: none;
    }}

    @keyframes ripple {{
      to {{ transform: scale(4); opacity: 0; }}
    }}

    .confetti {{
      position: fixed; width: 12px; height: 12px; pointer-events: none;
      z-index: 9999; animation: fall linear forwards;
    }}

    @keyframes fall {{
      to {{ transform: translateY(120dvh) rotate(900deg); opacity: 0; }}
    }}
  </style>
</head>
<body>
  <div class="aura"></div>

  <div class="theme-toggle" onclick="toggleTheme()">
    <span id="themeIcon">🌙</span>
  </div>

  <div class="header">
    <h1>DURGER KING</h1>
    <div class="tagline">ITALIANO • 3D • GOURMET</div>
  </div>

  <div id="menu">
    {items_html}
  </div>

  <div class="cart">
    <div class="cart-summary">
      <div class="cart-badge" id="cartBadge">0 articoli</div>
      <div class="cart-total" id="cartTotal">0,00 €</div>
    </div>
    <button id="orderBtn" onclick="openOrderModal()" disabled>ORDINA ORA</button>
  </div>

  <!-- 3D PREVIEW MODAL -->
  <div class="preview-modal" id="previewModal">
    <div class="preview-card">
      <model-viewer id="burger3d" src="https://modelviewer.dev/shared-assets/models/Hamburger.glb" 
        auto-rotate camera-controls ar ios-src="https://modelviewer.dev/shared-assets/models/Hamburger.usdz"
        shadow-intensity="1" exposure="0.8" environment-image="neutral">
      </model-viewer>
      <div class="preview-title" id="previewName"></div>
      <div class="preview-desc" id="previewDesc"></div>
      <div class="preview-actions">
        <button class="btn btn-close" onclick="closePreview()">Chiudi</button>
        <button class="btn btn-add" onclick="addFromPreview()">Aggiungi</button>
      </div>
    </div>
  </div>

  <!-- ORDER SUMMARY MODAL -->
  <div class="order-modal" id="orderModal">
    <div class="order-card">
      <h2>Il tuo ordine</h2>
      <div id="orderList"></div>
      <div class="order-total" id="modalTotal">Totale: 0,00 €</div>
      <div class="preview-actions">
        <button class="btn btn-close" onclick="closeOrderModal()">Modifica</button>
        <button class="btn btn-add" onclick="confirmOrder()">Conferma</button>
      </div>
    </div>
  </div>

  <script>
    const cart = [];
    let currentItem = null;

    // DOM
    const $ = s => document.querySelector(s);
    const $$ = s => document.querySelectorAll(s);

    // FORMAT
    const fmt = p => p.toFixed(2).replace('.', ',') + ' €';

    // THEME AUTO + TOGGLE
    function initTheme() {{
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const saved = localStorage.getItem('theme');
      const isDark = saved ? saved === 'dark' : prefersDark;
      document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
      $('#themeIcon').textContent = isDark ? '🌙' : '☀️';
    }}

    function toggleTheme() {{
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const newTheme = isDark ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      $('#themeIcon').textContent = newTheme === 'dark' ? '🌙' : '☀️';
      localStorage.setItem('theme', newTheme);
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
    }}

    // 3D PREVIEW
    function openPreview(card) {{
      currentItem = card;
      $('#previewName').textContent = card.dataset.name;
      $('#previewDesc').textContent = card.querySelector('p').textContent;
      $('#previewModal').classList.add('active');
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    function closePreview() {{
      $('#previewModal').classList.remove('active');
    }}

    function addFromPreview() {{
      addToCart(currentItem);
      closePreview();
    }}

    // CART
    function addToCart(card) {{
      const name = card.dataset.name;
      const price = parseFloat(card.dataset.price);
      const btn = card.querySelector('.add-btn');

      const existing = cart.find(i => i.name === name);
      if (existing) {{
        existing.qty++;
      }} else {{
        cart.push({{ name, price, qty: 1 }});
      }}

      btn.classList.add('added');
      createRipple(btn);
      createConfetti(btn);
      Telegram.WebApp.HapticFeedback.impactOccurred('rigid');

      setTimeout(() => btn.classList.remove('added'), 800);
      updateCart();
    }}

    function updateCart() {{
      const items = cart.reduce((s, i) => s + i.qty, 0);
      const total = cart.reduce((s, i) => s + i.price * i.qty, 0);

      $('#cartBadge').textContent = items + (items === 1 ? ' articolo' : ' articoli');
      $('#cartTotal').textContent = fmt(total);
      $('#orderBtn').disabled = items === 0;
    }}

    // ORDER MODAL
    function openOrderModal() {{
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
      $('#orderModal').classList.add('active');
    }}

    function closeOrderModal() {{
      $('#orderModal').classList.remove('active');
    }}

    function confirmOrder() {{
      closeOrderModal();
      explodeConfetti();
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      setTimeout(() => {{
        Telegram.WebApp.sendData(JSON.stringify(cart));
        Telegram.WebApp.close();
      }}, 1000);
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

    function createConfetti(el) {{
      const rect = el.getBoundingClientRect();
      const colors = ['#ff2e63', '#8b5cf6', '#06ffa5'];
      for (let i = 0; i < 25; i++) {{
        const c = document.createElement('div');
        c.className = 'confetti';
        c.style.left = (rect.left + rect.width/2 + (Math.random()-0.5)*100) + 'px';
        c.style.top = (rect.top + rect.height/2 + (Math.random()-0.5)*100) + 'px';
        c.style.background = colors[Math.floor(Math.random()*colors.length)];
        c.style.animationDuration = (Math.random()*2 + 2) + 's';
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 4000);
      }}
    }}

    function explodeConfetti() {{
      for (let i = 0; i < 8; i++) {{
        setTimeout(() => createConfetti({{ getBoundingClientRect: () => ({{left: innerWidth/2, top: innerHeight/2, width:0, height:0}}) }}), i * 120);
      }}
    }}

    // INIT
    document.addEventListener('DOMContentLoaded', () => {{
      initTheme();
      Telegram.WebApp.ready(); Telegram.WebApp.expand();

      // Auto index
      $$('.card').forEach((c, i) => c.style.setProperty('--i', i));

      // Listen to system theme change
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', initTheme);
    }});
  </script>
</body>
</html>
"""
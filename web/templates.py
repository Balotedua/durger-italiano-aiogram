import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config


def generate_menu_html():
    """DURGER KING ITALIANO – 60 FPS EDITION (Webby 2026)"""

    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<div class="badge">{item["badge"]}</div>' if item["badge"] else ""
        delay = idx * 0.08
        items_html += f'''
  <div class="menu-card" 
       data-name="{item['name']}" 
       data-price="{item['price']}" 
       data-emoji="{item['emoji']}" 
       data-desc="{item['description']}"
       style="--delay: {delay}s"
       onclick="previewItem(this)">
    <div class="card-inner">
      <div class="card-glow"></div>
      <div class="card-shine"></div>
      <div class="card-content">
        <div class="emoji-box">
          <span class="emoji">{item['emoji']}</span>
        </div>
        <div class="info">
          <h3>{item['name']}</h3>
          {badge}
          <p>{item['description']}</p>
          <div class="price-row">
            <span class="price">{item['price']:.2f}€</span>
            <div class="add-circle">+<span class="check">✓</span></div>
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
      --card: rgba(255,255,255,0.08);
      --text: #ffffff;
      --text-muted: rgba(255,255,255,0.7);
      --radius: 28px;
      --transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    [data-theme="light"] {{
      --bg: #f8fafc;
      --card: rgba(255,255,255,0.9);
      --text: #0f172a;
      --text-muted: #64748b;
    }}

    *, *::before, *::after {{ margin:0; padding:0; box-sizing:border-box; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: var(--bg); color: var(--text);
      min-height: 100dvh; padding: 16px 12px 180px;
      overflow-y: scroll; -webkit-overflow-scrolling: touch;
      position: relative;
      transition: background 0.5s ease;
    }}

    /* BACKGROUND – SVG BLUR (GPU FRIENDLY) */
    .bg-blur {{
      position: fixed; inset: 0; z-index: -2; pointer-events: none;
      background: 
        radial-gradient(circle at 20% 80%, #6366f1 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, #ec4899 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, #8b5cf6 0%, transparent 50%);
      background-size: 150% 150%;
      animation: bgFlow 25s ease infinite;
      opacity: 0.4;
      mask-image: radial-gradient(circle, black 70%, transparent 100%);
    }}

    @keyframes bgFlow {{
      0%,100% {{ background-position: 0% 50%, 100% 50%, 50% 50%; }}
      50% {{ background-position: 100% 50%, 0% 50%, 50% 50%; }}
    }}

    .grid {{
      position: fixed; inset: 0; z-index: -1;
      background: 
        linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px),
        linear-gradient(0deg, rgba(255,255,255,0.02) 1px, transparent 1px);
      background-size: 60px 60px;
      opacity: 0.6;
    }}

    /* HEADER */
    .header {{
      text-align: center; margin-bottom: 32px; z-index: 10;
    }}

    h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 44px; font-weight: 900; line-height: 1;
      background: linear-gradient(135deg, #fff, var(--accent), #fff);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-size: 200% 200%;
      animation: titleShine 4s ease infinite;
    }}

    @keyframes titleShine {{
      0%,100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    .tagline {{
      font-size: 14px; font-weight: 600; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: 6px; margin-top: 8px;
    }}

    /* THEME TOGGLE */
    .theme-toggle {{
      position: fixed; top: 16px; right: 16px; z-index: 100;
      width: 56px; height: 56px; border-radius: 50%;
      background: rgba(255,255,255,0.15); border: 2px solid rgba(255,255,255,0.2);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: var(--transition);
      will-change: transform;
    }}

    .theme-toggle:active {{ transform: scale(0.9); }}

    /* MENU CARD – ULTRA FLUID */
    .menu-card {{
      margin: 16px 0;
      animation: floatIn var(--delay, 0s) 0.6s ease backwards;
      will-change: transform;
    }}

    @keyframes floatIn {{
      from {{ opacity: 0; transform: translateY(40px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .card-inner {{
      position: relative; border-radius: var(--radius);
      background: var(--card);
      overflow: hidden; cursor: pointer;
      border: 1.5px solid rgba(255,255,255,0.1);
      transition: var(--transition);
      box-shadow: 0 12px 40px rgba(0,0,0,0.3);
      will-change: transform, box-shadow;
    }}

    .menu-card:active .card-inner {{
      transform: translateY(-8px) scale(1.02);
      box-shadow: 0 24px 60px rgba(99,102,241,0.5);
    }}

    .card-glow {{
      position: absolute; inset: -100%;
      background: conic-gradient(from 0deg at 50% 50%, 
        transparent, var(--primary), var(--accent), var(--secondary), transparent);
      opacity: 0; transition: opacity 0.5s;
      animation: spinGlow 8s linear infinite paused;
    }}

    .menu-card:active .card-glow {{
      opacity: 0.6; animation-play-state: running;
    }}

    @keyframes spinGlow {{ to {{ transform: rotate(360deg); }} }}

    .card-shine {{
      position: absolute; top: 0; left: -150%; width: 60%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.7), transparent);
      transition: left 0.8s ease;
    }}

    .menu-card:active .card-shine {{ left: 150%; }}

    .card-content {{ display: flex; gap: 20px; padding: 24px; }}

    .emoji-box {{
      flex-shrink: 0; width: 80px; height: 80px;
      background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(236,72,153,0.2));
      border-radius: 24px; display: flex; align-items: center; justify-content: center;
      transition: var(--transition);
    }}

    .menu-card:active .emoji-box {{ transform: scale(1.15); }}

    .emoji {{ font-size: 48px; }}

    .info h3 {{ font-size: 20px; font-weight: 900; margin-bottom: 4px; }}
    .info p {{ font-size: 14px; color: var(--text-muted); line-height: 1.5; margin: 6px 0 10px; }}
    .price {{ font-size: 26px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .add-circle {{
      width: 52px; height: 52px; border-radius: 50%;
      background: var(--success); color: white;
      display: flex; align-items: center; justify-content: center;
      font-size: 24px; font-weight: 900;
      cursor: pointer; transition: var(--transition);
      position: relative; overflow: hidden;
    }}

    .add-circle .check {{ display: none; font-size: 28px; }}
    .add-circle.added .check {{ display: block; animation: checkPop 0.4s ease; }}
    .add-circle.added {{ background: #059669; animation: pulse 0.5s ease; }}

    @keyframes pulse {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.3); }} }}
    @keyframes checkPop {{ 0% {{ transform: scale(0); }} 100% {{ transform: scale(1); }} }}

    .badge {{
      background: linear-gradient(135deg, #f43f5e, #ec4899);
      color: white; padding: 4px 12px; border-radius: 12px;
      font-size: 10px; font-weight: 800; text-transform: uppercase;
      margin-top: 6px; display: inline-block;
    }}

    /* CART BAR */
    .cart-bar {{
      position: fixed; bottom: 0; left: 0; right: 0;
      padding: 16px; background: rgba(10,10,15,0.95);
      border-top: 1px solid rgba(255,255,255,0.1);
      box-shadow: 0 -16px 40px rgba(0,0,0,0.5); z-index: 100;
    }}

    .cart-summary {{
      display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;
    }}

    .cart-badge {{
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white; padding: 8px 16px; border-radius: 20px;
      font-weight: 800; font-size: 14px;
    }}

    .cart-total {{ font-size: 28px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--success));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    #orderBtn {{
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white; border: none; padding: 16px;
      font-size: 18px; font-weight: 900; border-radius: 24px;
      width: 100%; cursor: pointer; text-transform: uppercase;
      letter-spacing: 1.5px; transition: var(--transition);
    }}

    #orderBtn:disabled {{ opacity: 0.5; }}

    /* PREVIEW MODAL – 3D ONLY HERE */
    .preview-modal {{
      position: fixed; inset: 0; background: rgba(0,0,0,0.9);
      display: none; align-items: center; justify-content: center;
      z-index: 1000; padding: 20px;
    }}

    .preview-modal.active {{ display: flex; }}

    .preview-stage {{
      perspective: 1000px; width: 100%; max-width: 380px;
    }}

    .preview-item {{
      background: var(--card); border-radius: var(--radius);
      padding: 32px; text-align: center;
      transform-style: preserve-3d;
      animation: itemEnter 0.7s cubic-bezier(0.34, 1.56, 0.64, 1);
      border: 2px solid rgba(255,255,255,0.15);
      box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }}

    @keyframes itemEnter {{
      from {{ transform: scale(0.6) rotateY(-120deg); opacity: 0; }}
      to {{ transform: scale(1) rotateY(0); opacity: 1; }}
    }}

    .preview-emoji {{ font-size: 100px; margin-bottom: 16px; }}
    .preview-info h2 {{ font-size: 28px; font-weight: 900; margin-bottom: 8px; }}
    .preview-info p {{ font-size: 16px; color: var(--text-muted); margin-bottom: 20px; }}
    .preview-price {{ font-size: 40px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent), var(--success));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .preview-actions {{ display: flex; gap: 12px; margin-top: 24px; }}
    .btn {{ flex: 1; padding: 14px; border: none; border-radius: 20px;
      font-weight: 700; cursor: pointer; }}
    .btn-secondary {{ background: rgba(255,255,255,0.1); color: var(--text); }}
    .btn-primary {{ background: var(--accent); color: white; }}

    /* CONFIRM MODAL */
    .modal {{
      position: fixed; inset: 0; background: rgba(0,0,0,0.85);
      display: none; align-items: center; justify-content: center;
      z-index: 1000; padding: 20px;
    }}

    .modal.active {{ display: flex; }}

    .modal-card {{
      background: var(--card); border-radius: var(--radius);
      padding: 28px; width: 100%; max-width: 380px;
      border: 1.5px solid rgba(255,255,255,0.15);
      box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }}

    .order-list {{ max-height: 40vh; overflow-y: auto; margin: 16px 0; }}
    .order-item {{ display: flex; justify-content: space-between; padding: 12px 0;
      border-bottom: 1px solid rgba(255,255,255,0.1); }}
    .order-total {{ font-size: 24px; font-weight: 900; text-align: center; margin: 16px 0;
      color: var(--success); }}

    /* EFFECTS – GPU FRIENDLY */
    .confetti {{
      position: fixed; width: 10px; height: 10px; pointer-events: none;
      z-index: 9999; border-radius: 2px;
      animation: confettiFall linear forwards;
    }}

    @keyframes confettiFall {{
      to {{ transform: translateY(100dvh) rotate(720deg); opacity: 0; }}
    }}
  </style>
</head>
<body>
  <div class="bg-blur"></div>
  <div class="grid"></div>

  <div class="theme-toggle" onclick="toggleTheme()">
    <span id="themeIcon">Moon</span>
  </div>

  <div class="header">
    <h1>DURGER KING<br>ITALIANO</h1>
    <div class="tagline">IL RE DEL GUSTO</div>
  </div>

  <div id="menu">{items_html}</div>

  <div class="cart-bar">
    <div class="cart-summary">
      <div class="cart-badge" id="cartBadge">0 articoli</div>
      <div class="cart-total" id="cartTotal">0,00 €</div>
    </div>
    <button id="orderBtn" onclick="openConfirmModal()" disabled>ORDINA ORA</button>
  </div>

  <!-- PREVIEW MODAL -->
  <div class="preview-modal" id="previewModal">
    <div class="preview-stage">
      <div class="preview-item">
        <div class="preview-emoji" id="previewEmoji"></div>
        <div class="preview-info">
          <h2 id="previewName"></h2>
          <p id="previewDesc"></p>
          <div class="preview-price" id="previewPrice"></div>
        </div>
        <div class="preview-actions">
          <button class="btn btn-secondary" onclick="closePreview()">Annulla</button>
          <button class="btn btn-primary" onclick="addFromPreview()">Aggiungi</button>
        </div>
      </div>
    </div>
  </div>

  <!-- CONFIRM MODAL -->
  <div class="modal" id="confirmModal">
    <div class="modal-card">
      <h2>Conferma Ordine</h2>
      <div class="order-list" id="orderList"></div>
      <div class="order-total" id="modalTotal">Totale: 0,00 €</div>
      <div style="display:flex; gap:12px; margin-top:20px;">
        <button class="btn btn-secondary" style="flex:1" onclick="closeConfirm()">Annulla</button>
        <button class="btn btn-primary" style="flex:1" onclick="sendOrder()">Conferma</button>
      </div>
    </div>
  </div>

  <script>
    const cart = [];
    let currentPreview = null;
    const $ = s => document.querySelector(s);

    const fmt = p => p.toFixed(2).replace('.', ',') + ' €';

    function previewItem(card) {{
      currentPreview = {{
        name: card.dataset.name,
        price: parseFloat(card.dataset.price),
        emoji: card.dataset.emoji,
        desc: card.dataset.desc
      }};
      $('#previewEmoji').textContent = currentPreview.emoji;
      $('#previewName').textContent = currentPreview.name;
      $('#previewDesc').textContent = currentPreview.desc;
      $('#previewPrice').textContent = fmt(currentPreview.price);
      $('#previewModal').classList.add('active');
      Telegram.WebApp.HapticFeedback.impactOccurred('rigid');
    }}

    function closePreview() {{
      $('#previewModal').classList.remove('active');
    }}

    function addFromPreview() {{
      addToCart(currentPreview.name, currentPreview.price);
      closePreview();
      explodeConfetti();
    }}

    function addToCart(name, price) {{
      const existing = cart.find(i => i.name === name);
      if (existing) existing.qty++;
      else cart.push({{ name, price, qty: 1 }});
      const btn = event.target.closest('.add-circle') || $('.add-circle');
      btn.classList.add('added');
      setTimeout(() => btn.classList.remove('added'), 600);
      updateCart();
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    function updateCart() {{
      const totalItems = cart.reduce((s, i) => s + i.qty, 0);
      const totalPrice = cart.reduce((s, i) => s + i.price * i.qty, 0);
      $('#cartBadge').textContent = totalItems + (totalItems === 1 ? ' articolo' : ' articoli');
      $('#cartTotal').textContent = fmt(totalPrice);
      $('#orderBtn').disabled = totalItems === 0;
    }}

    function openConfirmModal() {{
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
      $('#confirmModal').classList.add('active');
    }}

    function closeConfirm() {{
      $('#confirmModal').classList.remove('active');
    }}

    function sendOrder() {{
      closeConfirm();
      explodeConfetti();
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      setTimeout(() => {{
        Telegram.WebApp.sendData(JSON.stringify(cart));
        Telegram.WebApp.close();
      }}, 1000);
    }}

    function explodeConfetti() {{
      const colors = ['#6366f1', '#8b5cf6', '#ec4899', '#10b981'];
      for (let i = 0; i < 30; i++) {{
        const c = document.createElement('div');
        c.className = 'confetti';
        c.style.left = (innerWidth/2 + (Math.random() - 0.5) * 200) + 'px';
        c.style.top = (innerHeight/2 + (Math.random() - 0.5) * 200) + 'px';
        c.style.background = colors[Math.floor(Math.random() * colors.length)];
        c.style.animationDuration = (Math.random() * 2 + 1.5) + 's';
        c.style.animationDelay = (i * 0.05) + 's';
        c.style.transform = `rotate({{Math.random() * 360}}deg)`;
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 3000);
      }}
    }}

    function toggleTheme() {{
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      document.documentElement.setAttribute('data-theme', isDark ? 'light' : 'dark');
      $('#themeIcon').textContent = isDark ? 'Sun' : 'Moon';
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      Telegram.WebApp.ready(); Telegram.WebApp.expand();
      updateCart();
    }});
  </script>
</body>
</html>
"""
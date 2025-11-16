import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


def generate_menu_html():
    """DURGER KING ITALIANO – WEBBY AWARD 2026 WINNER EDITION"""

    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<div class="badge">{item["badge"]}</div>' if item["badge"] else ""
        delay = idx * 0.1
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
          <div class="emoji-glow"></div>
          <span class="emoji">{item['emoji']}</span>
        </div>
        <div class="info">
          <h3>{item['name']}</h3>
          {badge}
          <p>{item['description']}</p>
          <div class="price-row">
            <span class="price">{item['price']:.2f}€</span>
            <div class="add-circle">
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
      --transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    [data-theme="light"] {{
      --bg: #f8fafc;
      --card: rgba(255,255,255,0.85);
      --text: #0f172a;
      --text-muted: #64748b;
      --primary: #4f46e5;
      --secondary: #7c3aed;
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ 
      font-family: 'Inter', sans-serif;
      background: var(--bg); color: var(--text);
      min-height: 100dvh; padding: 16px 12px 200px;
      overflow-x: hidden; position: relative;
      transition: background 0.6s ease;
    }}

    /* BACKGROUND MAGIC UPGRADED */
    .bg-canvas {{
      position: fixed; inset: 0; z-index: -3;
      background: 
        radial-gradient(circle at 20% 80%, var(--primary) 0%, transparent 40%),
        radial-gradient(circle at 80% 20%, var(--accent) 0%, transparent 40%),
        radial-gradient(circle at 50% 50%, var(--secondary) 0%, transparent 40%);
      background-size: 180% 180%;
      animation: bgFlow 18s ease infinite;
      filter: blur(90px); opacity: 0.7;
    }}

    @keyframes bgFlow {{
      0%, 100% {{ background-position: 0% 50%, 100% 50%, 50% 50%; }}
      50% {{ background-position: 100% 50%, 0% 50%, 50% 50%; }}
    }}

    .grid {{
      position: fixed; inset: 0; z-index: -2;
      background: 
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(0deg, rgba(255,255,255,0.03) 1px, transparent 1px);
      background-size: 50px 50px;
      animation: gridDrift 50s linear infinite;
      opacity: 0.8;
    }}

    @keyframes gridDrift {{
      0% {{ transform: translate(0, 0); }}
      100% {{ transform: translate(50px, 50px); }}
    }}

    /* HEADER */
    .header {{
      text-align: center; margin-bottom: 36px; position: relative; z-index: 10;
      padding: 8px; border-radius: 32px;
      background: rgba(255,255,255,0.05); backdrop-filter: blur(16px);
    }}

    h1 {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 48px; font-weight: 900; line-height: 1;
      background: linear-gradient(135deg, #fff, var(--accent), #fff, var(--primary));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-size: 300% 300%;
      animation: titleShine 5s ease infinite;
      filter: drop-shadow(0 8px 30px rgba(236,72,153,0.5));
    }}

    @keyframes titleShine {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    .tagline {{
      font-size: 15px; font-weight: 700; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: 7px; margin-top: 12px;
      animation: fadeIn 1s ease 0.7s backwards;
    }}

    /* THEME TOGGLE */
    .theme-toggle {{
      position: fixed; top: 16px; right: 16px; z-index: 100;
      width: 64px; height: 64px; border-radius: 50%;
      background: rgba(255,255,255,0.12); backdrop-filter: blur(20px);
      border: 2px solid rgba(255,255,255,0.2);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: var(--transition);
      box-shadow: 0 12px 40px rgba(0,0,0,0.4);
    }}

    .theme-toggle:hover {{
      transform: scale(1.2) rotate(360deg);
      background: rgba(255,255,255,0.25);
      box-shadow: 0 0 40px rgba(99,102,241,0.6);
    }}

    /* MENU CARD – 3D READY */
    .menu-card {{
      margin: 24px 0; animation: floatIn var(--delay, 0s) 0.9s ease backwards;
      transform-style: preserve-3d; perspective: 1200px;
      cursor: pointer;
    }}

    @keyframes floatIn {{
      from {{ opacity: 0; transform: translateY(80px) scale(0.85) rotateX(-20deg); }}
      to {{ opacity: 1; transform: translateY(0) scale(1) rotateX(0); }}
    }}

    .card-inner {{
      position: relative; border-radius: var(--radius);
      background: var(--card); backdrop-filter: blur(32px) saturate(180%);
      overflow: hidden; border: 1.5px solid rgba(255,255,255,0.12);
      transition: var(--transition); box-shadow: var(--shadow);
      transform-style: preserve-3d;
    }}

    .menu-card:hover .card-inner {{
      transform: translateY(-20px) translateZ(40px) scale(1.05);
      box-shadow: 0 50px 120px rgba(99,102,241,0.7);
      border-color: var(--accent);
    }}

    .card-glow {{
      position: absolute; inset: -120%;
      background: conic-gradient(from 0deg at 50% 50%, 
        transparent, var(--primary), var(--accent), var(--secondary), transparent);
      opacity: 0; transition: opacity 0.7s;
      animation: spinGlow 10s linear infinite paused;
    }}

    .menu-card:hover .card-glow {{
      opacity: 0.8; animation-play-state: running;
    }}

    @keyframes spinGlow {{
      to {{ transform: rotate(360deg); }}
    }}

    .card-shine {{
      position: absolute; top: 0; left: -200%; width: 70%; height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent);
      transition: left 1.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .menu-card:hover .card-shine {{
      left: 200%;
    }}

    .card-content {{ display: flex; gap: 24px; padding: 32px; position: relative; z-index: 2; }}

    .emoji-box {{
      flex-shrink: 0; width: 96px; height: 96px;
      background: linear-gradient(135deg, rgba(99,102,241,0.25), rgba(236,72,153,0.25));
      border-radius: 32px; display: flex; align-items: center; justify-content: center;
      position: relative; transition: var(--transition);
      box-shadow: 0 16px 50px rgba(0,0,0,0.35);
      transform-style: preserve-3d;
    }}

    .emoji-glow {{
      position: absolute; inset: -12px; border-radius: 32px;
      background: linear-gradient(135deg, var(--accent), var(--primary));
      opacity: 0; filter: blur(20px); transition: opacity 0.7s; z-index: -1;
    }}

    .menu-card:hover .emoji-glow {{ opacity: 1; }}
    .menu-card:hover .emoji-box {{ transform: scale(1.25) rotate(12deg) translateZ(30px); }}

    .emoji {{
      font-size: 58px; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.5));
      animation: floatEmoji 3.2s ease-in-out infinite;
    }}

    @keyframes floatEmoji {{
      0%, 100% {{ transform: translateY(0) scale(1); }}
      50% {{ transform: translateY(-12px) scale(1.12); }}
    }}

    .info h3 {{ font-size: 24px; font-weight: 900; margin-bottom: 8px; }}
    .info p {{ font-size: 15px; color: var(--text-muted); line-height: 1.6; margin: 10px 0 16px; }}
    .price {{ font-size: 30px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .add-circle {{
      width: 60px; height: 60px; border-radius: 50%;
      background: var(--success); color: white;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: var(--transition);
      box-shadow: 0 10px 40px rgba(16,185,129,0.6);
      position: relative; overflow: hidden;
    }}

    .add-circle.added {{ animation: pulseSuccess 0.7s ease; }}

    /* 3D PREVIEW MODAL */
    .preview-modal {{
      position: fixed; inset: 0; background: rgba(0,0,0,0.92);
      backdrop-filter: blur(20px); display: none; align-items: center;
      justify-content: center; z-index: 1000; padding: 20px;
      animation: fadeIn 0.5s ease;
    }}

    .preview-modal.active {{ display: flex; }}

    .preview-stage {{
      perspective: 1200px; width: 100%; max-width: 420px;
    }}

    .preview-item {{
      width: 100%; padding: 40px; border-radius: var(--radius);
      background: var(--card); backdrop-filter: blur(40px);
      border: 2px solid rgba(255,255,255,0.15);
      box-shadow: 0 30px 100px rgba(0,0,0,0.6);
      transform-style: preserve-3d;
      animation: itemEnter 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
      position: relative; overflow: hidden;
    }}

    @keyframes itemEnter {{
      from {{ transform: scale(0.5) rotateY(-180deg) translateZ(-200px); opacity: 0; }}
      to {{ transform: scale(1) rotateY(0) translateZ(0); opacity: 1; }}
    }}

    .preview-emoji {{
      font-size: 120px; text-align: center; margin-bottom: 24px;
      filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));
      animation: floatEmoji 3s ease-in-out infinite;
    }}

    .preview-info h2 {{ font-size: 32px; font-weight: 900; text-align: center; margin-bottom: 12px; }}
    .preview-info p {{ font-size: 17px; color: var(--text-muted); text-align: center; margin-bottom: 24px; line-height: 1.6; }}
    .preview-price {{ font-size: 48px; font-weight: 900; text-align: center;
      background: linear-gradient(135deg, #fff, var(--accent), var(--success));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .preview-actions {{
      display: flex; gap: 16px; margin-top: 32px;
    }}

    .btn {{
      flex: 1; padding: 18px; border: none; border-radius: 28px;
      font-weight: 800; cursor: pointer; transition: var(--transition);
      text-transform: uppercase; letter-spacing: 1.5px;
    }}

    .btn-secondary {{ background: rgba(255,255,255,0.1); color: var(--text); }}
    .btn-primary {{ background: linear-gradient(135deg, var(--primary), var(--accent)); color: white; }}

    /* CART BAR – EXPANDABLE */
    .cart-bar {{
      position: fixed; bottom: 0; left: 0; right: 0;
      background: rgba(10,10,15,0.98); backdrop-filter: blur(40px);
      border-top: 1.5px solid rgba(255,255,255,0.12);
      box-shadow: 0 -20px 80px rgba(0,0,0,0.7); z-index: 100;
      transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .cart-header {{
      padding: 20px 16px; display: flex; justify-content: space-between; align-items: center;
      cursor: pointer;
    }}

    .cart-badge {{ background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white; padding: 12px 24px; border-radius: 28px; font-weight: 800; font-size: 16px;
      box-shadow: 0 10px 40px rgba(99,102,241,0.6);
    }}

    .cart-total {{ font-size: 36px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--success));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .cart-items {{
      max-height: 0; overflow: hidden; transition: max-height 0.6s ease;
      background: rgba(255,255,255,0.05); border-radius: 24px 24px 0 0;
      margin: 0 16px; padding: 0 16px;
    }}

    .cart-bar.expanded .cart-items {{ max-height: 50vh; padding: 16px; }}

    .cart-item {{
      display: flex; justify-content: space-between; align-items: center;
      padding: 16px 0; border-bottom: 1px solid rgba(255,255,255,0.1);
      animation: slideIn 0.4s ease;
    }}

    .cart-item-name {{ font-weight: 600; }}
    .cart-item-price {{ font-weight: 700; color: var(--success); }}

    .remove-item {{
      width: 32px; height: 32px; border-radius: 50%;
      background: var(--danger); color: white; display: flex;
      align-items: center; justify-content: center; cursor: pointer;
      font-size: 18px; margin-left: 12px;
    }}

    #orderBtn {{
      margin: 20px 16px; background: linear-gradient(135deg, var(--primary), var(--secondary), var(--accent));
      background-size: 300% 300%; color: white; border: none;
      padding: 22px; font-size: 20px; font-weight: 900; border-radius: 32px;
      width: calc(100% - 32px); cursor: pointer; text-transform: uppercase;
      letter-spacing: 2.5px; box-shadow: 0 20px 60px rgba(99,102,241,0.7);
      animation: gradientPulse 6s ease infinite; transition: var(--transition);
    }}

    @keyframes gradientPulse {{
      0%, 100% {{ background-position: 0% 50%; }}
      50% {{ background-position: 100% 50%; }}
    }}

    /* EFFECTS */
    .confetti, .ripple, .sparkle {{ position: fixed; pointer-events: none; z-index: 9999; }}
    @keyframes confettiDrop {{ to {{ transform: translateY(120dvh) rotate(720deg); opacity: 0; }} }}
    @keyframes ripplePop {{ to {{ transform: scale(5); opacity: 0; }} }}
    @keyframes sparkleSpin {{ to {{ transform: rotate(360deg); }} }}

    .sparkle {{
      width: 6px; height: 6px; background: white; border-radius: 50%;
      animation: sparkleSpin 1s linear infinite;
      filter: blur(1px);
    }}

    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  </style>
</head>
<body>
  <div class="bg-canvas"></div>
  <div class="grid"></div>

  <div class="theme-toggle" onclick="toggleTheme()">
    <span id="themeIcon">🌙</span>
  </div>

  <div class="header" id="godHeader">
    <h1>DURGER KING<br>ITALIANO</h1>
    <div class="tagline">IL RE DEL GUSTO</div>
  </div>

  <div id="menu">{items_html}</div>

  <!-- CART BAR -->
  <div class="cart-bar" id="cartBar" onclick="toggleCart()">
    <div class="cart-header">
      <div class="cart-badge" id="cartBadge">0 articoli</div>
      <div class="cart-total" id="cartTotal">0,00 €</div>
    </div>
    <div class="cart-items" id="cartItems"></div>
    <button id="orderBtn" onclick="event.stopPropagation(); openConfirmModal()" disabled>ORDINA ORA</button>
  </div>

  <!-- 3D PREVIEW MODAL -->
  <div class="preview-modal" id="previewModal">
    <div class="preview-stage">
      <div class="preview-item" id="previewItem">
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
      <div class="modal-actions">
        <button class="btn btn-cancel" onclick="closeConfirm()">Annulla</button>
        <button class="btn btn-confirm" onclick="sendOrder()">Conferma</button>
      </div>
    </div>
  </div>

  <script>
    // STATE
    const cart = [];
    let isDark = true;
    let currentPreview = null;

    // DOM
    const $ = s => document.querySelector(s);
    const $$ = s => document.querySelectorAll(s);

    // FORMAT
    const fmt = p => p.toFixed(2).replace('.', ',') + ' €';

    // PREVIEW ITEM
    function previewItem(card) {{
      const name = card.dataset.name;
      const price = parseFloat(card.dataset.price);
      const emoji = card.dataset.emoji;
      const desc = card.dataset.desc;

      currentPreview = {{ name, price, emoji, desc }};

      $('#previewEmoji').textContent = emoji;
      $('#previewName').textContent = name;
      $('#previewDesc').textContent = desc;
      $('#previewPrice').textContent = fmt(price);

      $('#previewModal').classList.add('active');
      createSparkles(card.getBoundingClientRect());
      Telegram.WebApp.HapticFeedback.impactOccurred('rigid');
    }}

    function closePreview() {{
      $('#previewModal').classList.remove('active');
      currentPreview = null;
    }}

    function addFromPreview() {{
      if (!currentPreview) return;
      addToCartLogic(currentPreview.name, currentPreview.price);
      closePreview();
      explodeConfetti();
    }}

    // ADD TO CART LOGIC
    function addToCartLogic(name, price) {{
      const existing = cart.find(i => i.name === name);
      if (existing) existing.qty++;
      else cart.push({{ name, price, qty: 1 }});

      updateCart();
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');
    }}

    // UPDATE CART
    function updateCart() {{
      const totalItems = cart.reduce((s, i) => s + i.qty, 0);
      const totalPrice = cart.reduce((s, i) => s + i.price * i.qty, 0);

      $('#cartBadge').textContent = totalItems + (totalItems === 1 ? ' articolo' : ' articoli');
      $('#cartTotal').textContent = fmt(totalPrice);
      $('#orderBtn').disabled = totalItems === 0;

      const itemsEl = $('#cartItems');
      itemsEl.innerHTML = '';
      cart.forEach((item, idx) => {{
        const div = document.createElement('div');
        div.className = 'cart-item';
        div.innerHTML = `
          <div>
            <div class="cart-item-name">${{item.name}} × ${{item.qty}}</div>
          </div>
          <div style="display:flex; align-items:center; gap:8px">
            <div class="cart-item-price">${{fmt(item.price * item.qty)}}</div>
            <div class="remove-item" onclick="event.stopPropagation(); removeFromCart(${idx})">×</div>
          </div>
        `;
        itemsEl.appendChild(div);
      }});
    }}

    function removeFromCart(idx) {{
      cart.splice(idx, 1);
      updateCart();
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
    }}

    function toggleCart() {{
      $('#cartBar').classList.toggle('expanded');
    }}

    // CONFIRM MODAL
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
      createLightning();
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      setTimeout(() => {{
        Telegram.WebApp.sendData(JSON.stringify(cart));
        Telegram.WebApp.close();
      }}, 1500);
    }}

    // EFFECTS
    function createSparkles(rect) {{
      for (let i = 0; i < 20; i++) {{
        const s = document.createElement('div');
        s.className = 'sparkle';
        s.style.left = (rect.left + rect.width / 2 + (Math.random() - 0.5) * 120) + 'px';
        s.style.top = (rect.top + rect.height / 2 + (Math.random() - 0.5) * 120) + 'px';
        s.style.animationDuration = (Math.random() * 0.8 + 0.6) + 's';
        document.body.appendChild(s);
        setTimeout(() => s.remove(), 1500);
      }}
    }}

    function explodeConfetti() {{
      for (let i = 0; i < 12; i++) {{
        setTimeout(() => createConfetti({{ left: innerWidth/2, top: innerHeight/2, width: 0, height: 0 }}), i * 100);
      }}
    }}

    function createConfetti(rect) {{
      const colors = ['#6366f1', '#8b5cf6', '#ec4899', '#10b981', '#fff'];
      for (let i = 0; i < 40; i++) {{
        const c = document.createElement('div');
        c.className = 'confetti';
        c.style.left = (rect.left + (Math.random() - 0.5) * 200) + 'px';
        c.style.top = (rect.top + (Math.random() - 0.5) * 200) + 'px';
        c.style.background = colors[Math.floor(Math.random() * colors.length)];
        c.style.animationDuration = (Math.random() * 3 + 2) + 's';
        c.style.animationDelay = Math.random() * 0.4 + 's';
        c.style.transform = `rotate({{Math.random() * 360}}deg)`;
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 5000);
      }}
    }}

    function createLightning() {{
      const l = document.createElement('div');
      l.style.cssText = 'position:fixed;inset:0;background:rgba(255,255,255,0.95);pointer-events:none;z-index:9999;animation:flash 1s ease-out';
      document.body.appendChild(l);
      setTimeout(() => l.remove(), 1000);
    }}

    // THEME
    function toggleTheme() {{
      isDark = !isDark;
      document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
      $('#themeIcon').textContent = isDark ? '🌙' : '☀️';
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
    }}

    // EASTER EGG: 7 tap su header
    let taps = 0;
    $('#godHeader').addEventListener('click', () => {{
      if (++taps === 7) {{
        document.body.style.filter = 'hue-rotate(360deg) brightness(2) saturate(2)';
        document.body.style.transition = 'filter 2s ease';
        setTimeout(() => document.body.style.filter = '', 3000);
        explodeConfetti();
        taps = 0;
      }}
      setTimeout(() => taps = 0, 2000);
    }});

    // INIT
    document.addEventListener('DOMContentLoaded', () => {{
      Telegram.WebApp.ready(); Telegram.WebApp.expand();
      updateCart();

      const style = document.createElement('style');
      style.textContent = `
        @keyframes flash {{ 0%,100% {{opacity:0}} 15%,35% {{opacity:1}} 25%,45% {{opacity:0}} }}
        @keyframes slideIn {{ from {{ transform: translateX(-30px); opacity: 0; }} to {{ transform: translateX(0); opacity: 1; }} }}
      `;
      document.head.appendChild(style);
    }});
  </script>
</body>
</html>
"""
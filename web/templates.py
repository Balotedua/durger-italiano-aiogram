# web/templates.py - ZEN WOW ULTIMATE EDITION
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config


def generate_menu_html():
    """IL MENU CHE FA DIRE "MA COME CAZZO È POSSIBILE" AD OGNI TAP"""

    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<div class="badge">{item["badge"]}</div>' if item["badge"] else ""
        items_html += f'''
  <div class="card" data-name="{item['name']}" data-price="{item['price']}" onclick="addItem(this)">
    <div class="card-inner">
      <div class="emoji">{item['emoji']}</div>
      <div class="info">
        <h3>{item['name']}</h3>
        {badge}
        <p>{item['description']}</p>
      </div>
      <div class="price">{item['price']:.2f}€</div>
      <div class="add-btn">
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
  <title>Durger King</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;700;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0a0a0f;
      --card: rgba(255,255,255,0.08);
      --text: #ffffff;
      --accent: #f72585;
      --success: #10b981;
      --radius: 32px;
      --shadow: 0 25px 80px rgba(0,0,0,0.5);
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
      padding: 20px 16px 160px;
      overflow-x: hidden;
    }}

    /* BACKGROUND AURA */
    .aura {{
      position: fixed; inset: 0; z-index: -1;
      background: 
        radial-gradient(circle at 30% 70%, #f72585 0%, transparent 50%),
        radial-gradient(circle at 70% 30%, #7209b7 0%, transparent 50%);
      filter: blur(100px); opacity: 0.6;
      animation: breathe 8s ease infinite;
    }}

    @keyframes breathe {{
      0%, 100% {{ transform: scale(1); opacity: 0.6; }}
      50% {{ transform: scale(1.3); opacity: 0.8; }}
    }}

    /* HEADER */
    .header {{
      text-align: center; margin-bottom: 40px;
    }}

    h1 {{
      font-size: 48px; font-weight: 900; letter-spacing: -2px;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 10px 30px rgba(247,37,133,0.4));
    }}

    .tag {{
      font-size: 14px; color: rgba(255,255,255,0.7); margin-top: 8px;
      letter-spacing: 4px; text-transform: uppercase; font-weight: 600;
    }}

    /* CARD */
    .card {{
      margin: 24px 0; animation: rise 0.8s ease backwards;
      animation-delay: calc(var(--i, 0) * 0.1s);
    }}

    @keyframes rise {{
      from {{ opacity: 0; transform: translateY(40px) scale(0.95); }}
      to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    .card-inner {{
      background: var(--card);
      backdrop-filter: blur(32px);
      border-radius: var(--radius);
      padding: 28px;
      display: flex; align-items: center; gap: 20px;
      position: relative; overflow: hidden;
      border: 1.5px solid rgba(255,255,255,0.1);
      box-shadow: var(--shadow);
      transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer;
    }}

    .card:hover .card-inner {{
      transform: translateY(-12px) scale(1.03);
      border-color: var(--accent);
      box-shadow: 0 40px 100px rgba(247,37,133,0.4);
    }}

    .emoji {{
      font-size: 56px; width: 80px; height: 80px;
      display: flex; align-items: center; justify-content: center;
      background: rgba(247,37,133,0.15);
      border-radius: 24px;
      transition: transform 0.6s ease;
    }}

    .card:hover .emoji {{
      transform: scale(1.2) rotate(12deg);
    }}

    .info h3 {{
      font-size: 22px; font-weight: 900; margin-bottom: 4px;
    }}

    .info p {{
      font-size: 14px; color: rgba(255,255,255,0.7); line-height: 1.5;
    }}

    .price {{
      font-size: 28px; font-weight: 900; margin-left: auto;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    .add-btn {{
      width: 56px; height: 56px; border-radius: 50%;
      background: var(--success); color: white;
      display: flex; align-items: center; justify-content: center;
      margin-left: 16px; cursor: pointer;
      transition: all 0.4s ease;
      box-shadow: 0 8px 32px rgba(16,185,129,0.5);
      position: relative; overflow: hidden;
    }}

    .add-btn svg {{
      width: 28px; height: 28px; fill: currentColor;
      transition: all 0.3s ease;
    }}

    .add-btn .check {{ display: none; }}
    .add-btn.added .plus {{ display: none; }}
    .add-btn.added .check {{ display: block; }}

    .add-btn.added {{
      animation: pop 0.6s ease;
    }}

    @keyframes pop {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.4); }}
    }}

    .badge {{
      background: linear-gradient(135deg, #f72585, #b5179e);
      color: white; padding: 6px 14px; border-radius: 16px;
      font-size: 11px; font-weight: 800; margin-top: 6px;
      display: inline-block; animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.1); }}
    }}

    /* CART */
    .cart {{
      position: fixed; bottom: 0; left: 0; right: 0;
      padding: 24px 20px; background: rgba(10,10,15,0.95);
      backdrop-filter: blur(40px); border-top: 1.5px solid rgba(255,255,255,0.1);
      box-shadow: 0 -20px 60px rgba(0,0,0,0.6); z-index: 100;
    }}

    .cart-row {{
      display: flex; justify-content: space-between; align-items: center;
      margin-bottom: 16px;
    }}

    .cart-info {{
      font-weight: 700; font-size: 16px;
    }}

    .cart-total {{
      font-size: 32px; font-weight: 900;
      background: linear-gradient(135deg, #fff, var(--success));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }}

    #orderBtn {{
      background: linear-gradient(135deg, var(--accent), #7209b7);
      color: white; border: none; padding: 20px;
      font-size: 18px; font-weight: 900; border-radius: 28px;
      width: 100%; cursor: pointer; text-transform: uppercase;
      letter-spacing: 1.5px; position: relative; overflow: hidden;
      box-shadow: 0 20px 60px rgba(247,37,133,0.5);
      transition: all 0.4s ease;
    }}

    #orderBtn:disabled {{
      opacity: 0.4; cursor: not-allowed;
    }}

    #orderBtn::before {{
      content: ''; position: absolute; inset: 0;
      background: radial-gradient(circle at center, rgba(255,255,255,0.3), transparent);
      opacity: 0; transition: opacity 0.4s;
    }}

    #orderBtn:hover:not(:disabled)::before {{
      opacity: 1;
    }}

    #orderBtn:hover:not(:disabled) {{
      transform: translateY(-4px);
      box-shadow: 0 30px 80px rgba(247,37,133,0.8);
    }}

    /* RIPPLE */
    .ripple {{
      position: absolute; border-radius: 50%;
      background: rgba(255,255,255,0.6);
      transform: scale(0); animation: ripple 0.6s ease-out;
      pointer-events: none;
    }}

    @keyframes ripple {{
      to {{ transform: scale(4); opacity: 0; }}
    }}

    /* CONFETTI */
    .confetti {{
      position: fixed; width: 10px; height: 10px;
      background: var(--accent); pointer-events: none;
      animation: fall linear forwards;
    }}

    @keyframes fall {{
      to {{ transform: translateY(120dvh) rotate(720deg); opacity: 0; }}
    }}
  </style>
</head>
<body>
  <div class="aura"></div>

  <div class="header">
    <h1>DURGER KING</h1>
    <div class="tag">ITALIANO • GOURMET • VELOCE</div>
  </div>

  <div id="menu">
    {items_html}
  </div>

  <div class="cart">
    <div class="cart-row">
      <div class="cart-info" id="cartInfo">0 articoli</div>
      <div class="cart-total" id="cartTotal">0,00 €</div>
    </div>
    <button id="orderBtn" onclick="sendOrder()" disabled>ORDINA ORA</button>
  </div>

  <script>
    const cart = [];
    let total = 0;

    function addItem(card) {{
      const name = card.dataset.name;
      const price = parseFloat(card.dataset.price);
      const btn = card.querySelector('.add-btn');

      // Add to cart
      const existing = cart.find(i => i.name === name);
      if (existing) {{
        existing.qty++;
      }} else {{
        cart.push({{ name, price, qty: 1 }});
      }}

      // Effects
      btn.classList.add('added');
      createRipple(btn);
      createConfetti(btn);
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');

      setTimeout(() => btn.classList.remove('added'), 600);

      updateCart();
    }}

    function updateCart() {{
      const items = cart.reduce((s, i) => s + i.qty, 0);
      total = cart.reduce((s, i) => s + i.price * i.qty, 0);

      $('#cartInfo').textContent = items + (items === 1 ? ' articolo' : ' articoli');
      $('#cartTotal').textContent = total.toFixed(2).replace('.', ',') + ' €';
      $('#orderBtn').disabled = items === 0;
    }}

    function sendOrder() {{
      if (cart.length === 0) return;

      // Final explosion
      for (let i = 0; i < 6; i++) {{
        setTimeout(() => createConfetti({{ getBoundingClientRect: () => ({{left: innerWidth/2, top: innerHeight/2}}) }}), i * 100);
      }}

      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      setTimeout(() => {{
        Telegram.WebApp.sendData(JSON.stringify(cart));
        Telegram.WebApp.close();
      }}, 800);
    }}

    function createRipple(el) {{
      const rect = el.getBoundingClientRect();
      const ripple = document.createElement('div');
      ripple.className = 'ripple';
      ripple.style.left = (rect.width / 2) + 'px';
      ripple.style.top = (rect.height / 2) + 'px';
      el.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    }}

    function createConfetti(el) {{
      const rect = el.getBoundingClientRect();
      const colors = ['#f72585', '#7209b7', '#4361ee', '#10b981'];
      for (let i = 0; i < 20; i++) {{
        const c = document.createElement('div');
        c.className = 'confetti';
        c.style.left = (rect.left + rect.width/2 + (Math.random()-0.5)*80) + 'px';
        c.style.top = (rect.top + rect.height/2 + (Math.random()-0.5)*80) + 'px';
        c.style.background = colors[Math.floor(Math.random()*colors.length)];
        c.style.animationDuration = (Math.random()*2 + 2) + 's';
        document.body.appendChild(c);
        setTimeout(() => c.remove(), 4000);
      }}
    }}

    // Init
    document.addEventListener('DOMContentLoaded', () => {{
      Telegram.WebApp.ready(); Telegram.WebApp.expand();

      // Auto-index cards
      document.querySelectorAll('.card').forEach((c, i) => {{
        c.style.setProperty('--i', i);
      }});

      // Easter egg: triple tap header
      let taps = 0;
      document.querySelector('.header').addEventListener('click', () => {{
        if (++taps === 3) {{
          document.body.style.filter = 'hue-rotate(360deg) brightness(1.5)';
          setTimeout(() => document.body.style.filter = '', 2000);
          taps = 0;
        }}
        setTimeout(() => taps = 0, 1000);
      }});
    }});

    const $ = s => document.querySelector(s);
  </script>
</body>
</html>
"""
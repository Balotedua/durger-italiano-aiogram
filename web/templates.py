# web/templates.py - Template HTML
from config import Config


def generate_menu_html():
    """Genera HTML menu dinamico da config"""

    # Genera items HTML
    items_html = ""
    for item in Config.MENU_ITEMS:
        badge = f'<span class="badge">{item["badge"]}</span>' if item["badge"] else ""
        items_html += f'''
  <div class="item" onclick="add('{item['name']}', {item['price']}, this)">
    <h3>{item['emoji']} {item['name']} {badge}</h3>
    <p>{item['description']}</p>
    <div class="price">{item['price']:.2f} €</div>
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
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      padding: 20px 16px 100px;
      overflow-x: hidden;
    }}

    @keyframes fadeInUp {{
      from {{ opacity: 0; transform: translateY(30px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes float {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-10px); }}
    }}

    h1 {{
      text-align: center;
      color: white;
      font-size: 32px;
      font-weight: 800;
      margin-bottom: 24px;
      text-shadow: 0 4px 20px rgba(0,0,0,0.3);
      animation: fadeInUp 0.6s ease, float 3s ease-in-out infinite;
      letter-spacing: -0.5px;
    }}

    .item {{
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      border-radius: 24px;
      padding: 20px;
      margin: 16px 0;
      box-shadow: 0 8px 32px rgba(0,0,0,0.12);
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      border: 2px solid transparent;
      position: relative;
      overflow: hidden;
      animation: fadeInUp 0.6s ease;
    }}

    .item::before {{
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
      transition: left 0.5s;
    }}

    .item:hover::before {{
      left: 100%;
    }}

    .item:hover {{
      transform: translateY(-4px) scale(1.02);
      box-shadow: 0 12px 48px rgba(0,0,0,0.2);
      border-color: #667eea;
    }}

    .item:active {{
      transform: scale(0.98);
    }}

    .item h3 {{
      color: #2d3748;
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .item p {{
      color: #718096;
      font-size: 14px;
      line-height: 1.5;
      margin-bottom: 12px;
    }}

    .price {{
      color: #667eea;
      font-weight: 800;
      font-size: 24px;
      display: inline-block;
      background: linear-gradient(135deg, #667eea, #764ba2);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}

    .cart-container {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 16px;
      background: rgba(255,255,255,0.95);
      backdrop-filter: blur(20px);
      box-shadow: 0 -4px 24px rgba(0,0,0,0.15);
      z-index: 100;
    }}

    .cart-info {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      color: #2d3748;
      font-weight: 600;
    }}

    .cart-count {{
      background: #667eea;
      color: white;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 14px;
      animation: fadeInUp 0.3s ease;
    }}

    .cart-total {{
      font-size: 20px;
      background: linear-gradient(135deg, #667eea, #764ba2);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}

    button {{
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      border: none;
      padding: 18px;
      font-size: 18px;
      border-radius: 16px;
      width: 100%;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    button:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(102, 126, 234, 0.5);
    }}

    button:active {{
      transform: scale(0.98);
    }}

    button:disabled {{
      opacity: 0.5;
      cursor: not-allowed;
    }}

    .badge {{
      display: inline-block;
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
    }}

    .added {{
      animation: pulse 0.3s ease;
    }}
  </style>
</head>
<body>
  <h1>🍕 Durger King Italiano 🍔</h1>

  {items_html}

  <div class="cart-container">
    <div class="cart-info">
      <span>Carrello: <span class="cart-count" id="cartCount">0 articoli</span></span>
      <span class="cart-total" id="cartTotal">0,00 €</span>
    </div>
    <button onclick="sendOrder()" id="orderBtn">🛒 Ordina Ora</button>
  </div>

  <script>
    let cart = [];

    function updateCart() {{
      const count = cart.length;
      const total = cart.reduce((sum, item) => sum + item.price, 0);
      document.getElementById('cartCount').textContent = count + (count === 1 ? ' articolo' : ' articoli');
      document.getElementById('cartTotal').textContent = total.toFixed(2).replace('.', ',') + ' €';
      document.getElementById('orderBtn').disabled = count === 0;
    }}

    function add(name, price, element) {{
      cart.push({{name, price}});
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');

      element.classList.add('added');
      setTimeout(() => element.classList.remove('added'), 300);

      updateCart();
    }}

    function sendOrder() {{
      if (cart.length === 0) {{
        Telegram.WebApp.showAlert('Carrello vuoto! Aggiungi almeno un prodotto. 🍕');
        return;
      }}
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      Telegram.WebApp.sendData(JSON.stringify(cart));
      Telegram.WebApp.close();
    }}

    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
    updateCart();
  </script>
</body>
</html>
"""
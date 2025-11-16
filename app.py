# app.py - Durger King Italiano con Webhook (Railway ready)
import os
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from flask import Flask, render_template_string

# Carica variabili ambiente
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://web-production-670b4.up.railway.app")
PORT = int(os.environ.get("PORT", 8080))

# Assicura che WEBHOOK_URL abbia https://
if not WEBHOOK_URL.startswith("http"):
    WEBHOOK_URL = f"https://{WEBHOOK_URL}"

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN mancante!")

# Bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# HTML MENU
HTML_MENU = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Durger King Italiano</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      padding: 20px 16px 100px;
      overflow-x: hidden;
    }

    @keyframes fadeInUp {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @keyframes float {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-10px); }
    }

    h1 {
      text-align: center;
      color: white;
      font-size: 32px;
      font-weight: 800;
      margin-bottom: 24px;
      text-shadow: 0 4px 20px rgba(0,0,0,0.3);
      animation: fadeInUp 0.6s ease, float 3s ease-in-out infinite;
      letter-spacing: -0.5px;
    }

    .item {
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
    }

    .item::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
      transition: left 0.5s;
    }

    .item:hover::before {
      left: 100%;
    }

    .item:hover {
      transform: translateY(-4px) scale(1.02);
      box-shadow: 0 12px 48px rgba(0,0,0,0.2);
      border-color: #667eea;
    }

    .item:active {
      transform: scale(0.98);
    }

    .item h3 {
      color: #2d3748;
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .item p {
      color: #718096;
      font-size: 14px;
      line-height: 1.5;
      margin-bottom: 12px;
    }

    .price {
      color: #667eea;
      font-weight: 800;
      font-size: 24px;
      display: inline-block;
      background: linear-gradient(135deg, #667eea, #764ba2);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .cart-container {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 16px;
      background: rgba(255,255,255,0.95);
      backdrop-filter: blur(20px);
      box-shadow: 0 -4px 24px rgba(0,0,0,0.15);
      z-index: 100;
    }

    .cart-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      color: #2d3748;
      font-weight: 600;
    }

    .cart-count {
      background: #667eea;
      color: white;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 14px;
      animation: fadeInUp 0.3s ease;
    }

    .cart-total {
      font-size: 20px;
      background: linear-gradient(135deg, #667eea, #764ba2);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    button {
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
    }

    button:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 32px rgba(102, 126, 234, 0.5);
    }

    button:active {
      transform: scale(0.98);
    }

    button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    .badge {
      display: inline-block;
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase;
    }

    @keyframes pulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.05); }
    }

    .added {
      animation: pulse 0.3s ease;
    }
  </style>
</head>
<body>
  <h1>🍕 Durger King Italiano 🍔</h1>

  <div class="item" onclick="add('PizzaBurger', 8.50, this)">
    <h3>🍕 PizzaBurger <span class="badge">Hot</span></h3>
    <p>Mozzarella fior di latte, pomodoro San Marzano, basilico fresco</p>
    <div class="price">8,50 €</div>
  </div>

  <div class="item" onclick="add('PastaBurger', 9.00, this)">
    <h3>🍝 PastaBurger <span class="badge">Bestseller</span></h3>
    <p>Spaghetti al ragù della nonna, croccante e gustoso!</p>
    <div class="price">9,00 €</div>
  </div>

  <div class="item" onclick="add('Tiramisù Shake', 5.50, this)">
    <h3>☕ Tiramisù Shake <span class="badge">New</span></h3>
    <p>Caffè espresso, mascarpone cremoso, cacao amaro</p>
    <div class="price">5,50 €</div>
  </div>

  <div class="item" onclick="add('Arancino Durger', 7.00, this)">
    <h3>🍙 Arancino Durger</h3>
    <p>Riso carnaroli, ragù siciliano, piselli dolci, fritto alla perfezione</p>
    <div class="price">7,00 €</div>
  </div>

  <div class="cart-container">
    <div class="cart-info">
      <span>Carrello: <span class="cart-count" id="cartCount">0 articoli</span></span>
      <span class="cart-total" id="cartTotal">0,00 €</span>
    </div>
    <button onclick="sendOrder()" id="orderBtn">🛒 Ordina Ora</button>
  </div>

  <script>
    let cart = [];

    function updateCart() {
      const count = cart.length;
      const total = cart.reduce((sum, item) => sum + item.price, 0);
      document.getElementById('cartCount').textContent = count + (count === 1 ? ' articolo' : ' articoli');
      document.getElementById('cartTotal').textContent = total.toFixed(2).replace('.', ',') + ' €';
      document.getElementById('orderBtn').disabled = count === 0;
    }

    function add(name, price, element) {
      cart.push({name, price});
      Telegram.WebApp.HapticFeedback.impactOccurred('medium');

      // Animazione elemento
      element.classList.add('added');
      setTimeout(() => element.classList.remove('added'), 300);

      updateCart();
    }

    function sendOrder() {
      if (cart.length === 0) {
        Telegram.WebApp.showAlert('Carrello vuoto! Aggiungi almeno un prodotto. 🍕');
        return;
      }
      Telegram.WebApp.HapticFeedback.notificationOccurred('success');
      Telegram.WebApp.sendData(JSON.stringify(cart));
      Telegram.WebApp.close();
    }

    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
    updateCart();
  </script>
</body>
</html>
"""


# Handler /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🍕 Apri Menu 🍔", web_app=WebAppInfo(url=WEBHOOK_URL))]],
        resize_keyboard=True
    )
    await message.answer(
        "🍕 *Benvenuto al Durger King Italiano!*\n\n"
        "Premi il pulsante qui sotto per ordinare il tuo panino italiano! 🇮🇹",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )


# Handler ordine
@dp.message(lambda m: m.web_app_data)
async def webapp_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
        if not data:
            await message.answer("❌ Carrello vuoto!")
            return
        total = sum(item["price"] for item in data)
        items = "\n".join([f"• {i['name']} - {i['price']:.2f}€" for i in data])
        await message.answer(
            f"✅ *ORDINE CONFERMATO!*\n\n"
            f"{items}\n\n"
            f"💰 *Totale: {total:.2f}€*\n\n"
            f"Grazie per aver ordinato da Durger King Italiano! 🇮🇹",
            parse_mode="Markdown"
        )
    except Exception as e:
        await message.answer(f"❌ Errore: {e}")


# Setup webhook con aiohttp
async def on_startup(app):
    webhook_url = f"{WEBHOOK_URL}/webhook"
    await bot.set_webhook(webhook_url)
    print(f"✅ Webhook impostato: {webhook_url}")


async def on_shutdown(app):
    await bot.delete_webhook()
    await bot.session.close()


# Route HTML menu
async def serve_menu(request):
    return web.Response(text=HTML_MENU, content_type='text/html')


# Health check
async def health(request):
    return web.Response(text="OK")


# Main application
def create_app():
    app = web.Application()

    # Route HTML
    app.router.add_get('/', serve_menu)
    app.router.add_get('/health', health)

    # Webhook handler
    webhook_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_handler.register(app, path='/webhook')

    # Startup/shutdown
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="0.0.0.0", port=PORT)
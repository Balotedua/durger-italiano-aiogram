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
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://durger-italiano-aiogram.up.railway.app")
PORT = int(os.environ.get("PORT", 8080))

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
  <title>Durger King Italiano</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <style>
    body { font-family: 'Segoe UI', sans-serif; background: linear-gradient(#fff, #fff3e0); margin: 0; padding: 15px; }
    h1 { text-align: center; color: #d32f2f; font-size: 24px; }
    .item { background: white; border-radius: 16px; padding: 18px; margin: 12px 0; box-shadow: 0 4px 12px rgba(0,0,0,0.1); cursor: pointer; transition: 0.2s; }
    .item:active { transform: scale(0.98); }
    .item h3 { margin: 0; color: #1b5e20; font-size: 18px; }
    .price { color: #d32f2f; font-weight: bold; font-size: 16px; }
    button { background: #d32f2f; color: white; border: none; padding: 16px; font-size: 20px; border-radius: 12px; width: 100%; font-weight: bold; margin-top: 20px; }
  </style>
</head>
<body>
  <h1>🍕 Durger King Italiano 🍔</h1>
  <div class="item" onclick="add('PizzaBurger', 8.50)">
    <h3>PizzaBurger</h3>
    <p>Mozzarella, pomodoro, basilico fresco</p>
    <div class="price">8,50 €</div>
  </div>
  <div class="item" onclick="add('PastaBurger', 9.00)">
    <h3>PastaBurger</h3>
    <p>Spaghetti al ragù nel panino!</p>
    <div class="price">9,00 €</div>
  </div>
  <div class="item" onclick="add('Tiramisù Shake', 5.50)">
    <h3>Tiramisù Shake</h3>
    <p>Caffè, mascarpone, cacao</p>
    <div class="price">5,50 €</div>
  </div>
  <div class="item" onclick="add('Arancino Durger', 7.00)">
    <h3>Arancino Durger</h3>
    <p>Riso, ragù, piselli, fritto!</p>
    <div class="price">7,00 €</div>
  </div>

  <button onclick="sendOrder()">🛒 ORDINA ORA</button>

  <script>
    let cart = [];
    function add(name, price) {
      cart.push({name, price});
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
      alert(name + " aggiunto!");
    }
    function sendOrder() {
      if (cart.length === 0) {
        alert("Carrello vuoto! Aggiungi almeno un prodotto.");
        return;
      }
      Telegram.WebApp.sendData(JSON.stringify(cart));
      Telegram.WebApp.close();
    }
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
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
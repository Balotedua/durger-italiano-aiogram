# app.py - Durger King Italiano con Aiogram + Flask
import asyncio
import os
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from flask import Flask, render_template_string
from threading import Thread
from dotenv import load_dotenv
import os


# Carica token da .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN mancante! Aggiungilo su Railway → Settings → Variables")

# Inizializza bot e Flask
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = Flask(__name__)

# HTML MENU ITALIANO (completo)
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
    .cart { position: fixed; bottom: 0; left: 0; right: 0; background: #ff6f00; color: white; padding: 15px; text-align: center; }
    button { background: #d32f2f; color: white; border: none; padding: 16px; font-size: 20px; border-radius: 12px; width: 100%; font-weight: bold; }
  </style>
</head>
<body>
  <h1>Durger King Italiano</h1>
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
    <p>Caffè, mascarpone, cacao in bicchiere</p>
    <div class="price">5,50 €</div>
  </div>
  <div class="item" onclick="add('Arancino Durger', 7.00)">
    <h3>Arancino Durger</h3>
    <p>Riso, ragù, piselli, fritto!</p>
    <div class="price">7,00 €</div>
  </div>

  <div class="cart">
    <button onclick="sendOrder()">ORDINA ORA</button>
  </div>

  <script>
    let cart = [];
    function add(name, price) {
      cart.push({name, price});
      Telegram.WebApp.HapticFeedback.impactOccurred('light');
    }
    function sendOrder() {
      Telegram.WebApp.sendData(JSON.stringify(cart));
      alert("Ordine inviato! Grazie!");
      Telegram.WebApp.close();
    }
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
  </script>
</body>
</html>
"""

# Route Flask
@app.route('/')
def index():
    print("HIT ROOT!")  # Log per Railway
    return render_template_string(HTML_MENU)

@app.route('/health')
def health():
    return "OK", 200


# Comando /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Apri Menu", web_app=WebAppInfo(url="https://durger-italiano-aiogram.up.railway.app"))]],
        resize_keyboard=True
    )
    await message.answer(
        "Benvenuto al *Durger King Italiano*! \n"
        "Premi il pulsante per ordinare il tuo panino italiano!",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# Ricevi ordine
@dp.message(lambda m: m.web_app_data)
async def webapp_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
        if not data:
            await message.answer("Carrello vuoto!")
            return
        total = sum(item["price"] for item in data)
        items = "\n".join([f"• {i['name']} - {i['price']}€" for i in data])
        await message.answer(
            f"*ORDINE CONFERMATO!*\n\n"
            f"{items}\n\n"
            f"*Totale: {total}€*\n"
            f"Grazie per aver ordinato da Durger King Italiano!",
            parse_mode="Markdown"
        )
    except:
        await message.answer("Errore nell'ordine. Riprova!")

# Avvia Flask + Bot
import os  # ← AGGIUNGI QUESTA RIGA IN ALTO (se non c'è già)

async def main():
    # Avvia Flask in background con PORTA DINAMICA per Railway
    import os
    port = int(os.environ.get("PORT", 8080))
    from threading import Thread
    Thread(target=lambda: app.run(
        host="0.0.0.0",
        port=port,
        use_reloader=False,
        debug=False
    )).start()
    # Avvia polling bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
# app.py - Main entry point
from aiohttp import web
from aiogram import Bot, Dispatcher
from config import Config
from bot.handlers import router as bot_router
from web.server import create_app


def main():
    """Entry point principale"""

    # Valida configurazione
    Config.validate()

    # Inizializza bot e dispatcher
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()

    # Registra router bot
    dp.include_router(bot_router)

    # Crea app web
    app = create_app(bot, dp)

    # Avvia server
    print(f"🚀 Avvio server su {Config.HOST}:{Config.PORT}")
    print(f"📱 Bot: @{bot.token.split(':')[0]}")
    print(f"🌐 Webhook: {Config.WEBHOOK_URL}{Config.WEBHOOK_PATH}")

    web.run_app(
        app,
        host=Config.HOST,
        port=Config.PORT
    )


if __name__ == "__main__":
    main()
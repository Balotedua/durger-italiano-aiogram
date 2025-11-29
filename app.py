# app.py - Main entry point
from aiohttp import web
from aiogram import Bot, Dispatcher
from config import Config
from bot.routers import get_routers
from web.server import create_app


import logging

def main():
    """Entry point principale"""
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Valida configurazione
    Config.validate()

    # Inizializza bot e dispatcher
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()
    
    logger.info("Bot e dispatcher inizializzati")

    # Registra router bot
    for router in get_routers():
        dp.include_router(router)

    # Crea app web
    app = create_app(bot, dp)

    # Avvia server
    logger.info(f"🚀 Avvio server su {Config.HOST}:{Config.PORT}")
    logger.info(f"📱 Bot: @{bot.token.split(':')[0]}")
    logger.info(f"🌐 Webhook: {Config.WEBHOOK_URL}{Config.WEBHOOK_PATH}")

    web.run_app(
        app,
        host=Config.HOST,
        port=Config.PORT
    )


if __name__ == "__main__":
    main()

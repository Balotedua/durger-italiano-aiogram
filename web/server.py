# web/server.py - Server web aiohttp con routing
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from config import Config
from router import setup_routes


async def health_check(request):
    """Health check endpoint"""
    return web.Response(text="OK")


async def on_startup(app):
    """Setup webhook all'avvio"""
    bot = app['bot']
    webhook_url = f"{Config.WEBHOOK_URL}{Config.WEBHOOK_PATH}"
    await bot.set_webhook(webhook_url)
    print(f"✅ Webhook impostato: {webhook_url}")


async def on_shutdown(app):
    """Cleanup allo shutdown"""
    bot = app['bot']
    await bot.delete_webhook()
    await bot.session.close()
    print("🛑 Bot fermato")


def create_app(bot: Bot, dp: Dispatcher):
    """Crea applicazione web"""
    app = web.Application()

    # Salva bot nell'app
    app['bot'] = bot

    # Setup routes multi-page
    setup_routes(app)

    # Health check
    app.router.add_get('/health', health_check)

    # Webhook handler
    webhook_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_handler.register(app, path=Config.WEBHOOK_PATH)

    # Lifecycle
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app
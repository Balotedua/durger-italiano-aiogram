# web/server.py - Server web aiohttp
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from config import Config
from web.templates import generate_menu_html


async def serve_menu(request):
    """Serve pagina menu HTML"""
    html = generate_menu_html()
    return web.Response(text=html, content_type='text/html')


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

    # Route pubbliche
    app.router.add_get('/', serve_menu)
    app.router.add_get('/health', health_check)

    # Webhook handler
    webhook_handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    webhook_handler.register(app, path=Config.WEBHOOK_PATH)

    # Lifecycle
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    return app
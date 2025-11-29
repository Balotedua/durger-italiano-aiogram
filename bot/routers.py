"""Registrazione di tutti i router"""
from bot.handlers.start import router as start_router
from bot.handlers.webapp import router as webapp_router

def get_routers():
    """Restituisce tutti i router da registrare"""
    return [
        start_router,
        webapp_router,
    ]

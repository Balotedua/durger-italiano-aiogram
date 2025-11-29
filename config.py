import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bot (esistente)
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://web-production-670b4.up.railway.app")
    WEBHOOK_PATH = "/webhook"
    HOST = "0.0.0.0"
    PORT = int(os.getenv("PORT", 8080))

    # Menu Durger King (esistente)
    MENU_ITEMS = [
        {
            "name": "PizzaBurger",
            "emoji": "🍕",
            "description": "Mozzarella fior di latte, pomodoro San Marzano, basilico fresco",
            "price": 8.50,
            "badge": "Hot"
        },
        # ... altri items esistenti
    ]

from colors import get_module_color

    # 🆕 NUOVA CONFIGURAZIONE MODULI
    MODULES = {
        'home': {
            'name': 'Assistente AI',
            'icon': '🤖',
            'color': get_module_color('home'),
            'path': '/'
        },
        'finance': {
            'name': 'Finanza',
            'icon': '💰',
            'color': get_module_color('finance'),
            'path': '/finance'
        },
        'psychology': {
            'name': 'Psicologia',
            'icon': '🧠',
            'color': get_module_color('psychology'),
            'path': '/psychology'
        },
        'fitness': {
            'name': 'Fitness',
            'icon': '💪',
            'color': get_module_color('fitness'),
            'path': '/fitness'
        },
        'durger_king': {
            'name': 'Durger King',
            'icon': '🍔',
            'color': get_module_color('durger_king'),
            'path': '/menu'
        }
    }

    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError("❌ BOT_TOKEN mancante!")
        return True

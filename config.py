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

    # 🆕 NUOVA CONFIGURAZIONE MODULI
    MODULES = {
        'home': {
            'name': 'Assistente AI',
            'icon': '🤖',
            'color': '#6366f1',
            'path': '/'
        },
        'finance': {
            'name': 'Finanza',
            'icon': '💰',
            'color': '#10b981',
            'path': '/finance'
        },
        'psychology': {
            'name': 'Psicologia',
            'icon': '🧠',
            'color': '#8b5cf6',
            'path': '/psychology'
        },
        'fitness': {
            'name': 'Fitness',
            'icon': '💪',
            'color': '#ec4899',
            'path': '/fitness'
        },
        'durger_king': {
            'name': 'Durger King',
            'icon': '🍔',
            'color': '#f59e0b',
            'path': '/menu'
        }
    }

    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError("❌ BOT_TOKEN mancante!")
        return True
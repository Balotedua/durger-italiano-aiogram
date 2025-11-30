import os
from dotenv import load_dotenv
from colors import get_module_color

load_dotenv()

class Config:
    # Bot (esistente)
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")  # type: ignore
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "https://web-production-670b4.up.railway.app")
    WEBHOOK_PATH: str = "/webhook"
    HOST: str = "0.0.0.0"
    PORT: int = int(os.getenv("PORT", 8080))

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
    # Descrizione della struttura di ogni modulo:
    # - 'name': Nome visualizzato del modulo.
    # - 'icon': Emoji o carattere unicode che rappresenta il modulo.
    # - 'color': Colore associato al modulo, ottenuto da `get_module_color`.
    # - 'path': Percorso URL associato al modulo.
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

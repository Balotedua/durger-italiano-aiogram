
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configurazione app"""

    # Bot
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    # Webhook
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://web-production-670b4.up.railway.app")

    # Assicura https://
    if not WEBHOOK_URL.startswith("http"):
        WEBHOOK_URL = f"https://{WEBHOOK_URL}"

    WEBHOOK_PATH = "/webhook"

    # Server
    HOST = "0.0.0.0"
    PORT = int(os.getenv("PORT", 8080))

    # Menu
    MENU_ITEMS = [
        {
            "name": "PizzaBurger",
            "emoji": "🍕",
            "description": "Mozzarella fior di latte, pomodoro San Marzano, basilico fresco",
            "price": 8.50,
            "badge": "Hot"
        },
        {
            "name": "PastaBurger",
            "emoji": "🍝",
            "description": "Spaghetti al ragù della nonna, croccante e gustoso!",
            "price": 9.00,
            "badge": "Bestseller"
        },
        {
            "name": "Tiramisù Shake",
            "emoji": "☕",
            "description": "Caffè espresso, mascarpone cremoso, cacao amaro",
            "price": 5.50,
            "badge": "New"
        },
        {
            "name": "Arancino Durger",
            "emoji": "🍙",
            "description": "Riso carnaroli, ragù siciliano, piselli dolci, fritto alla perfezione",
            "price": 7.00,
            "badge": None
        }
    ]

    @classmethod
    def validate(cls):
        """Valida configurazione"""
        if not cls.BOT_TOKEN:
            raise ValueError("❌ BOT_TOKEN mancante! Aggiungilo in Railway → Variables")
        return True
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from config import Config

def get_menu_keyboard():
    """Tastiera con pulsante WebApp - MODIFICATO"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text="🎯 Apri Life Assistant",  # 🆕 Testo aggiornato
                web_app=WebAppInfo(url=Config.WEBHOOK_URL)  # Ora punta alla homepage
            )]
        ],
        resize_keyboard=True
    )
    return keyboard
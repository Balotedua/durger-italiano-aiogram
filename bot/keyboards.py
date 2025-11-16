# bot/keyboards.py - Tastiere e pulsanti
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from config import Config

def get_menu_keyboard():
    """Tastiera con pulsante WebApp menu"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text="🍕 Apri Menu 🍔",
                web_app=WebAppInfo(url=Config.WEBHOOK_URL)
            )]
        ],
        resize_keyboard=True
    )
    return keyboard
# bot/handlers.py - Handler comandi bot
import json
from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards import get_menu_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Handler comando /start"""
    await message.answer(
        "🍕 *Benvenuto al Durger King Italiano!*\n\n"
        "Premi il pulsante qui sotto per ordinare il tuo panino italiano! 🇮🇹",
        reply_markup=get_menu_keyboard(),
        parse_mode="Markdown"
    )


@router.message(lambda m: m.web_app_data)
async def handle_webapp_data(message: types.Message):
    """Handler dati da WebApp (ordine)"""
    try:
        data = json.loads(message.web_app_data.data)

        if not data:
            await message.answer("❌ Carrello vuoto!")
            return

        # Calcola totale
        total = sum(item["price"] for item in data)

        # Formatta lista prodotti
        items = "\n".join([
            f"• {item['name']} - {item['price']:.2f}€"
            for item in data
        ])

        # Invia conferma
        await message.answer(
            f"✅ *ORDINE CONFERMATO!*\n\n"
            f"{items}\n\n"
            f"💰 *Totale: {total:.2f}€*\n\n"
            f"Grazie per aver ordinato da Durger King Italiano! 🇮🇹",
            parse_mode="Markdown"
        )
    except Exception as e:
        await message.answer(f"❌ Errore nell'ordine: {str(e)}")
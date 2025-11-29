from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards import get_menu_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Handler comando /start"""
    await message.answer(
        "🍕 *Benvenuto al Durger King di Danizonsanseng!*\n\n"
        "Premi il pulsante qui sotto per ordinare il tuo panino! 🇮🇹",
        reply_markup=get_menu_keyboard(),
        parse_mode="Markdown"
    )

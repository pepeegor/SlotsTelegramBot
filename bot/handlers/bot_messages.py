from aiogram import Router
from aiogram.types import Message

from keyboards.reply import start

router = Router()


@router.message()
async def echo(message: Message):
    await message.answer(
        "Следуй инструкции по кнопке ниже",
        reply_markup=start
    )

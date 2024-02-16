from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from keyboards.inline import main

router = Router()


@router.message(CommandStart())
async def welcome(message: Message):
    text ="""
🖐Привет для подачи заявки на розыгрыш отправь мне свое имя юзера в формате @username.
Username — это уникальное имя, которое человек придумывает себе в социальных сетях или играх. Ник можно установить или изменить. Вы можете удалить никнейм, чтобы другие пользователи не смогли вас найти.

ИНСТРУКЦИЯ ДЛЯ ТЕХ У КОГО ЕЩЕ НЕТ USERNAME
Чтобы установить себе username выполните следующие действия:

⁃ Нажмите на три черточки в правом верхнем углу

⁃ Тапните на «Настройки»

⁃ Коснитесь поля «Имя пользователя»

⁃ Введите уникальное имя

⁃ Для сохранения, нажмите на кнопку в правом углу.

✅Отлично. Жми кнопку "продолжить" для перехода к следующему шагу."""
    photo = FSInputFile("data/images/start_img.jpg")

    await message.answer_photo(
        photo,
        reply_markup=main,
        caption=text
    )
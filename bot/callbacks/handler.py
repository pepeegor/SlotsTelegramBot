from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile

from keyboards.inline import user, slot
from keyboards.reply import start
from utils.states import Form
from utils.utils import push_data

router = Router()

que = set()


@router.callback_query(F.data == "continue")
async def get_username(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.username)
    text = """✅Отлично. С формальностями разобрались, теперь отправь мне username."""
    await callback_query.message.answer(text)
    await callback_query.answer()


@router.message(Form.username)
async def form_name(message: Message, state: FSMContext):
    if message.text[0] == "@":
        await state.update_data(username=message.text)
        gif = FSInputFile("data/gifs/confirm.gif")
        text = f"✅{message.text} - принято.✅"
        result = await message.answer_animation(
            gif,
            reply_markup=user,
            caption=text
        )
        print(result.animation.file_id, "confirm username")
    else:
        await message.answer(f"{message.text} - не подходит требованиям. Введи username, начинающийся с @.")


@router.callback_query(F.data == 'change_username')
async def change_username(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.username)
    await callback_query.message.answer("Введи новый username.")


@router.callback_query(F.data == "username_cont")
async def get_slot(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.slot)
    text = "🎁 Отправь мне свой вариант слота с функцией покупки."
    await callback_query.message.answer(text)
    await callback_query.answer()


@router.message(Form.slot)
async def form_slot(message: Message, state: FSMContext):
    if all(char.isalpha() and char in "abcdefghijklmnopqrstuvwxyz " for char in message.text.lower()):
        await state.update_data(slot=message.text)
        gif = FSInputFile("data/gifs/end_bot.gif")
        text = f"✅{message.text} - принято.✅"
        result = await message.answer_animation(
            gif,
            reply_markup=slot,
            caption=text
        )
        print(result.animation.file_id, "confirm slot")
    else:
        await message.answer(f"{message.text} - не подходит требованиям."
                             " Все буквы дожны быть на латинице! Отправь новый слот, подходящий под требования.")


@router.callback_query(F.data == 'change_slot')
async def change_slot(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.slot)
    await callback_query.message.answer("🎁 Отправь мне новый вариант слота с функцией покупки.")
    await callback_query.answer()


@router.callback_query(F.data == 'slot_cont')
async def push_all(callback_query: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_id = callback_query.from_user.username
    push_id = user_data.get("username")
    push_d = user_data.get("slot")
    # if user_id not in que:
    #     que.add(user_id)
    res = push_data(str(push_id), str(push_d))
    if res == 0:
        gif = FSInputFile("data/gifs/cap.gif")
        text = "✅ Ура твоя заявка принята. Свою заявку ты можешь отследить перейдя по ссылке " \
            "с таблицей заявок которая находится в посте с розыгрышем в TG - @casino_malaya."
        result = await callback_query.message.answer_animation(
            gif,
            reply_markup=start,
            caption=text
        )
        print(result.animation.file_id, "confirm request")
    elif res == 1:
        text = "Упс! Кажется, пользователь с таким же username уже отправлял заявку!"
        await callback_query.message.answer(text, reply_markup=start)
        await callback_query.answer()
    elif res == 2:
        text = "Упс! Кажется, такой слот уже занят!"
        await callback_query.message.answer(text, reply_markup=start)
        await callback_query.answer()

    # que.remove(user_id)
    await state.clear()

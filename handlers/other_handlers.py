from aiogram import Router, F
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from lexicon.lexicon import LEXICON_RU
from aiogram.filters import Text


# Инициализируем роутер уровня модуля
router: Router = Router()
# создаем фильтр на самом роутере, чтобы не прописывать в каждом хэндлере.
# Этот фильтра пропускает только стикеры
#router.message.filter(F.sticker)

button_1: KeyboardButton = KeyboardButton(text='Собак 🦮')
button_2: KeyboardButton = KeyboardButton(text='огурцов 🥒')

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]])

@router.message(F.text == 'задай вопрос')
async def question_button(msg: Message):
    await msg.answer(text='чего кошки боятся больше всего', reply_markup=keyboard)

@router.message(F.text == 'Собак 🦮')
async def answer_dogs(msg: Message):
    await msg.answer(text='Да, кошки боятся собак',
                     reply_markup=ReplyKeyboardRemove)

@router.message(F.text == 'огурцов 🥒')
async def answer_cuc(msg: Message):
    await msg.answer(text='Но огурцов кошки боятся еще больше',
                     reply_markup = ReplyKeyboardRemove)

@router.message(F.text)
async def echo(msg: Message):
    try:
        await msg.send_copy(chat_id=msg.chat.id)
    except TypeError:
        await msg.reply(text=LEXICON_RU['no_echo'])


@router.message(F.sticker)
async def echo_sticker(msg: Message):
    try:
        await msg.answer_sticker(msg.sticker.file_id)
    except:
        await msg.reply(text=LEXICON_RU['no_echo'])
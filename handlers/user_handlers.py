from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router: Router = Router()

@router.message(CommandStart())
async def command_start(msg: Message):
    await msg.answer(text=LEXICON_RU['/start'])

@router.message(Command('help'))
async def command_help(msg: Message):
    await msg.answer(text=LEXICON_RU['/help'])

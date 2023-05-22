from aiogram import Router, F
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


# Инициализируем роутер уровня модуля
router: Router = Router()
# создаем фильтр на самом роутере, чтобы не прописывать в каждом хэндлере.
# Этот фильтра пропускает только стикеры
#router.message.filter(F.sticker)

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
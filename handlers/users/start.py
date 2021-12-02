from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext
from keyboards.inline.ijaraTugma import tumanTugma
# from utils.db_api.database import DBcommands
from loader import dp
from data.config import ADMINS
# db = DBcommands()


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message , state:FSMContext):
    await state.finish()
    await message.answer(f"Uy manzili tanlang", reply_markup=tumanTugma)

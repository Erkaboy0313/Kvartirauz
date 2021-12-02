from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
import states
from states.ijara import Ijara,Ijarachi
from keyboards.inline.ijaraTugma import tumanTugma
from keyboards.default.asosiyTugmalar import telTugma
from utils.db_api.database import DBcommands

db = DBcommands()

from loader import dp

@dp.callback_query_handler(lambda text: text.data == 'back', state=Ijara.atrofida)
async def typework(call: CallbackQuery, state:FSMContext):
    await call.message.answer('Главное меню-Бош меню')
    await call.message.delete()
    await call.answer(cache_time=0.02)
    await state.finish()
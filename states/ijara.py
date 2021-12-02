from aiogram.dispatcher.filters.state import State, StatesGroup

class Ijara(StatesGroup):
    manzil = State()
    turi = State()
    egasi = State() # xazayka 
    xona_soni = State()
    buyumlar = State()
    atrofida = State()
    kim_uchun = State() #sheriklikka
    odam_soni = State()
    valyuta = State()
    narx = State()
    tel = State()
    makler = State()
    rasm = State() # ?

class Ijarachi(StatesGroup):
    manzil = State() #pass qilish mumkin
    turi = State()
    egasi = State() # xazayka 
    xona_soni = State()
    buyumlar = State()
    atrofida = State()
    kim_uchun = State() #sheriklikka
    odam_soni = State()
    narx = State()
    tel = State()
    makler = State()


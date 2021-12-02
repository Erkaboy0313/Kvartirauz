from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram import types


tumanTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Uchtepa tumani", callback_data="region_Uchtepa"),
        InlineKeyboardButton("Bektemir tumani", callback_data="region_Bektemir")],
        [InlineKeyboardButton("Mirzo Ulug'bek tumani", callback_data="region_Mirzo Ulug'bek"),
        InlineKeyboardButton("Mirobod", callback_data="region_Mirobod")],
        [InlineKeyboardButton("Sergeli", callback_data="region_Sergeli"),
        InlineKeyboardButton("Olmazor", callback_data="region_Olmazor")],
        [InlineKeyboardButton("Chilonzor", callback_data="region_Chilonzor"),
        InlineKeyboardButton("SShayxontohur", callback_data="region_Shayxontohur")],
        [InlineKeyboardButton("Yunusobod", callback_data="region_Yunusobod"),
        InlineKeyboardButton("Yakkasaroy", callback_data="region_Yakkasaroy")],
        [InlineKeyboardButton("Yashnobod", callback_data="region_Yashnobod"),
        InlineKeyboardButton("Chirchiq", callback_data="region_Chirchiq")],      
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

turTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Hovli', callback_data="hovli")],
        [InlineKeyboardButton(text="Ko'p qavatli", callback_data='kop')]   
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

egaTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Xazaykali', callback_data="Xazaykali")],
        [InlineKeyboardButton(text="Xazaykasiz", callback_data='Xazaykasiz')]   
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

xonaTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data="1"),
            InlineKeyboardButton(text='2', callback_data="2"),
            InlineKeyboardButton(text='3', callback_data="3"),
        ],  
        [
            InlineKeyboardButton(text='4', callback_data="4"),
            InlineKeyboardButton(text='5', callback_data="5"),
            InlineKeyboardButton(text='6', callback_data="6"),
        ],  
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

xonaTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Televezor', callback_data="Televezor")],
        [InlineKeyboardButton(text='Muzlatgich', callback_data="Muzlatgich")],
        [InlineKeyboardButton(text='Kir yuvish mashinasi', callback_data="Kir yuvish mashinasi")],
        [InlineKeyboardButton(text='Wi-fi', callback_data="Wi-fi")],
        [InlineKeyboardButton(text='Gaz plita', callback_data="Gaz plita")],
        [InlineKeyboardButton(text='Mebel', callback_data="Mebel")],
        [InlineKeyboardButton(text='Gilam', callback_data="Gilam")],
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

xonaTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Metro', callback_data="Metro")],
        [InlineKeyboardButton(text='Maktab', callback_data="Maktab")],
        [InlineKeyboardButton(text='Dorixona', callback_data="Dorixona")],
        [InlineKeyboardButton(text='Supermarket', callback_data="Supermarket")],
        [InlineKeyboardButton(text='Bog\'cha', callback_data="Bog\'cha")],
        [InlineKeyboardButton(text='Anhor', callback_data="Anhor")],
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

xonaTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Oila', callback_data="Oila")],
        [InlineKeyboardButton(text='Yigitlar', callback_data="Yigitlar")],
        [InlineKeyboardButton(text='Qizlar', callback_data="Qizlar")]
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

odamTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data="1"),
            InlineKeyboardButton(text='2', callback_data="2"),
            InlineKeyboardButton(text='3', callback_data="3"),
        ],  
        [
            InlineKeyboardButton(text='4', callback_data="4"),
            InlineKeyboardButton(text='5', callback_data="5"),
            InlineKeyboardButton(text='6', callback_data="6"),
        ],
        [
            InlineKeyboardButton(text='7', callback_data="7"),
            InlineKeyboardButton(text='8', callback_data="8"),
            InlineKeyboardButton(text='9', callback_data="9"),
        ],  
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))

valyutaTugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='💵 UZS', callback_data="som")],
        [InlineKeyboardButton(text='💵 USD', callback_data='$')]   
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))


confirmationKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Bor', callback_data="Bor")],
        [InlineKeyboardButton(text='❌ Yo\'q', callback_data='Yo\'q')]   
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))


confirmationKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Tasdishlash', callback_data="post")],
        [InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel')]   
    ]
).add(types.InlineKeyboardButton('Ortga', callback_data='back'))
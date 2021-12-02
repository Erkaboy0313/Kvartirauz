from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

telTugma = ReplyKeyboardMarkup(
    keyboard=[
        [   
            KeyboardButton(text='📞 Mening raqamim',request_contact=True),
        ],
        [   
            KeyboardButton(text='Ortga'),
        ],
    ],
    resize_keyboard=True
)

locationKey = ReplyKeyboardMarkup(
    keyboard=[
        [   
            KeyboardButton(text='📍 Локация | Манзил',request_location=True),
        ],
        [   
            KeyboardButton(text='След. | Кенгиси'),
        ],
        [   
            KeyboardButton(text='Назад | Ортга'),
        ],
    ],
    resize_keyboard=True
)

button_back = ReplyKeyboardMarkup(
    keyboard=[
        [   
            KeyboardButton(text='Назад | Ортга'),
        ],
    ],
    resize_keyboard=True
)
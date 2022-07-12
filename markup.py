from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profileMenu = ReplyKeyboardMarkup(resize_keyboard=True)
profileBack = ReplyKeyboardMarkup(resize_keyboard=True)
btnSkills = KeyboardButton(text="Навыки")
btnBack = KeyboardButton(text="Профиль")
btnUp = KeyboardButton(text="Прорваться")


profileMenu.add(btnBack, btnSkills, btnUp)
profileBack.insert(btnBack)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profileMenu = ReplyKeyboardMarkup(resize_keyboard=True)
profileBack = ReplyKeyboardMarkup(resize_keyboard=True)
btnSkills = KeyboardButton(text="Навыки")
btnBack = KeyboardButton(text="Профиль")

profileMenu.insert(btnSkills)
profileBack.insert(btnBack)

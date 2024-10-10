from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text='Библиотека')],
									   [KeyboardButton(text='Контакты'),
									    KeyboardButton(text='О нас')]],
									resize_keyboard=True,
									input_field_placeholder='Выберите пункт меню'	)

list_books = InlineKeyboardMarkup(inline_keyboard=[
	[InlineKeyboardButton(text='Айзек Азимов - "Конец вечности"', callback_data='book-1')],
	[InlineKeyboardButton(text='Джек Лондон - "Мартин Иден"', callback_data='book-2')],
	[InlineKeyboardButton(text='Рэй Брэдбери - "451 градус по Фаренгейту"',callback_data='book-3')],
	])


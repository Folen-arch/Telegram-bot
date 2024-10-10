from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет', reply_markup=kb.main)
    await message.reply('Как дела?')

@router.message(F.text == 'Библиотека')   
async def library(message:Message):
    await message.answer('Выберите книгу', reply_markup=kb.list_books)

@router.callback_query(F.data == 'book-1')
async def b1_select(callback: CallbackQuery):
    await callback.answer('Вы выбрали книгу')
    await callback.message.answer('https://fantasy-worlds.org/lib/id2319/')

@router.callback_query(F.data =='book-2')
async def b2_select(callback:CallbackQuery):
    await callback.answer('Вы выбрали книгу')
    await callback.message.answer('https://librebook.me/martin_eden')

@router.callback_query(F.data == 'book-3')
async def b3_select(callback:CallbackQuery):
    await callback.answer('Вы выбрали книгу')
    await callback.message.answer('https://fantasy-worlds.org/lib/id34650/')

@router.message(F.text == 'О нас')
async def about(message:Message):
    await message.answer('Привет! 👋 Меня зовут Дима, и этот бот ведет 📚 список прочитанных и не очень мною книг!')

@router.message(F.text == 'Контакты')
async def contacts(message:Message):
    await message.answer('https://t.me/FolenV')
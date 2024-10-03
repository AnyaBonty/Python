from email.policy import default

from aiogram import F,Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from pyexpat.errors import messages

import app.keyboards as kb
import app.sost as s
from app.sost import Register

router=Router()


@router.message(CommandStart())
async def start(message:Message):
    await message.answer('start',reply_markup=kb.main)
@router.message (Command('help'))
async def cmd_help(message:Message):
    await message.reply('ne pomogy')

@router.message (F.text=='Каталог')
async def nice(message:Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog)

@router.callback_query(F.data=='futb')
async def futbolk(callback: CallbackQuery):
    await callback.answer('Cruto')
    await callback.message.answer('Футболка :)')

@router.message(Command('reg'))
async def register(message: Message, state: FSMContext):
    await state.set_state(s.Register.name)
    await message.answer('Vvedi imya:')

@router.message(s.Register.name)
async def reg_name(message:Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(s.Register.fam)
    await message.answer('Введите фамилию')

@router.message(s.Register.fam)
async def reg_fam(message:Message, state: FSMContext):
    await state.update_data(fam=message.text)
    await state.set_state(s.Register.age)
    await message.answer('Введите ваш возраст')

@router.message(s.Register.age)
async def reg_age(message:Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(s.Register.number)
    await message.answer('Введите номер телефона:',reply_markup=kb.number)

@router.message(s.Register.number, F.contact)
async def reg_age(message:Message, state: FSMContext):
    if message.contact:
        await state.update_data(number=message.contact.phone_number)
    elif message.contact:
        await state.update_data(number=message.text)
    data=await state.get_data()
    await message.answer(f'Имя: {data["name"]}\nФамилия: {data["fam"]}\nВозраст: {data["age"]}\n Телефон: {data["number"]}')
    await state.clear()









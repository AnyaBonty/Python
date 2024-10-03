from urllib.request import request_host

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
main=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                   [KeyboardButton(text='Корзина ')],
                                   [KeyboardButton(text='Контакты'),
                                    KeyboardButton(text='О нас')]],
                         resize_keyboard=True,
                         input_field_placeholder='Выбери пунктик...')
catalog=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Футболки', callback_data='futb')],
                                              [InlineKeyboardButton(text='Кроссовки', callback_data='cros')],
                                              [InlineKeyboardButton(text='Штаны', callback_data='shtan')],
                                              [InlineKeyboardButton(text='Аксессуары', callback_data='aks'),
                                               InlineKeyboardButton(text='Головные уборы', callback_data='gol')]])
number=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]],resize_keyboard=True)
from symtable import Class

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Register(StatesGroup):
    name=State()
    fam=State()
    age=State()
    number=State()

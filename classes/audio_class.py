from aiogram.fsm.state import State, StatesGroup


class GetAudio(StatesGroup):
    audio_class_1 = State()
    audio_class_2 = State()
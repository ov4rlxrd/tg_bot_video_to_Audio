import moviepy.editor
import time
import os

from pathlib import Path
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from keyboard import kb_start
from classes.audio_class import GetAudio

router = Router()


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer('Привет! Для продолжения нажми кнопку ниже!', reply_markup=kb_start)


@router.message(F.text == 'Получить аудиодорожку!')
async def get_audio(message: Message, state: FSMContext):
    await message.answer('Пожалуйста напишите как назвать файл с аудиодорожкой')
    await state.set_state(GetAudio.audio_class_1)


@router.message(GetAudio.audio_class_1)
async def audio_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Пожалуйста отправьте видео, аудиодорожку которого вы хотите получить!')
    await state.set_state(GetAudio.audio_class_2)


# @router.message(F.text == 'Получить аудиодорожку!')
# async def get_audio(message: Message, state: FSMContext):
#     await message.answer('Пожалуйста отправьте видео, аудиодорожку которого вы хотите получить!')
#     await state.set_state(GetAudio.audio_class_2)


@router.message(GetAudio.audio_class_2)
async def audio_generation(message: Message, state: FSMContext, bot: Bot):
    file_name = await state.get_data()
    file = await bot.get_file(message.video.file_id)
    await bot.download_file(file.file_path, "video.mp4")  # Download video and save output in file "video.mp4"
    video = moviepy.editor.VideoFileClip("video.mp4")
    audio = video.audio
    audio.write_audiofile(f'{file_name["name"]}.mp3')
    await message.answer('Подождите идет обработка запроса')

    await bot.send_audio(message.chat.id, audio=FSInputFile(f'{file_name["name"]}.mp3'))
    os.remove(f'{file_name["name"]}.mp3')
    await state.clear()

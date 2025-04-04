import requests

from vkbottle.bot import Message
from PIL import Image

from bot import bot, USERS, Translator
from constants import *
from functions import *


def main():
    # Начать
    @bot.on.private_message(text="Начать")
    async def start_answer(message: Message):
        id = message.from_id
        lang_def_1, lang_def_2, lang_photo_3, lang_photo_4 = USERS.get_data(id)

        keyboard = make_keyboard()

        text = f"""Привет!\n
Я здесь, чтобы помочь с переводом. Напиши что угодно, и я переведу это на нужный язык.\n
Сейчас стоит перевод с {genitive(lang_def_1.lower())} на {lang_def_2.lower()} для обычного перевода.
И перевод с {genitive(lang_photo_3.lower())} на {lang_photo_4.lower()} для фотоперевода.\n
Ты можешь это изменить командами. Информацию о них и о всех других возможностях переводчика ты найдешь в /help.\n
Всё просто! 😎"""

        await message.answer(text, keyboard=keyboard.get_json())

    # /help
    @bot.on.private_message(text="/help")
    async def help_answer(message: Message):
        lang_def_1, lang_def_2, lang_photo_3, lang_photo_4 = USERS.get_data(message.from_id)
        text = f"""/help - меню помощи
/change_lang_def <язык текста> <язык перевода> - поменять языки для обычного перевода
/change_lang_photo <язык текста> <язык перевода> - поменять языки для фотоперевода
* регистр языков не учитывается
/fast_change_def - меняет местами языки для обычно перевода
/fast_change_photo - меняет местами языки для фотоперевода
/all_languages - списки всех языков для обычного перевода
/random_word - случайное слово на английском и его перевод на выбранный язык\n
Чтобы перевести текст, отправьте сообщение на выбранном языке
Чтобы перевести фото, отправьте фото с текстом на выбранном языке\n
Сейчас стоит перевод с {genitive(lang_def_1.lower())} на {lang_def_2.lower()} для обычного перевода.
И перевод с {genitive(lang_photo_3.lower())} на {lang_photo_4.lower()} для фотоперевода.\n
Для языка текст в обычном переводе есть особый язык - "Авто". Он автоматически опередят язык текста."""

        await message.answer(text)

    # /all_languages
    @bot.on.private_message(text="/all_languages")
    async def echo_answer(message: Message):
        keyboard = Keyboard(one_time=False, inline=True)
        keyboard.add(Text("Обычный перевод"), KeyboardButtonColor.PRIMARY)
        keyboard.row()
        keyboard.add(Text("Фотоперевод"), KeyboardButtonColor.PRIMARY)

        text = """Для какого перевода интересует набор языков?"""

        await message.answer(text, keyboard=keyboard.get_json())

    # /fast_change_def
    @bot.on.private_message(text="/fast_change_def")
    async def fast_change_def_answer(message: Message):
        languages = USERS.get_data(message.from_id)
        if languages[0].lower() == 'авто':
            await message.answer(f"Нельзя перевести на автоопределяемый язык.")
        else:
            USERS.change_languages(message.from_id, languages[1], languages[0], 'def')
            await message.answer(f"Теперь перевод с {genitive(languages[1])} на {languages[0].lower()}.")

    # /change_lang_def
    @bot.on.private_message(text="/change_lang_def <lang1> <lang2>")
    async def change_lang_def_answer(message: Message, lang1, lang2):
        if lang1.capitalize() in TRANSLATED_LANGUAGES.keys() and lang2.capitalize() in SECOND_LANGUAGE:
            USERS.change_languages(message.from_id, lang1.capitalize(), lang2.capitalize(), 'def')
            await message.answer(f"Теперь перевод с {genitive(lang1)} на {lang2.lower()}.")
        elif lang2.capitalize() == 'Авто':
            await message.answer(f"Нельзя перевести на автоопределяемый язык.")
        else:
            await message.answer('Я не знаю такого языка!\nПовтори попытку с одним из моих поддерживаемых языков.')

    # /fast_change_photo
    @bot.on.private_message(text="/fast_change_photo")
    async def fast_change_photo_answer(message: Message):
        languages = USERS.get_data(message.from_id)
        if languages[0].lower() == 'автоопределение языка':
            await message.answer(f"Нельзя перевести на автоопределение языка.")
        else:
            USERS.change_languages(message.from_id, languages[3], languages[2], 'photo')
            await message.answer(f"Теперь фотоперевод с {genitive(languages[3])} на {languages[2].lower()}.")

    # /change_photo
    @bot.on.private_message(text="/change_lang_photo <lang1> <lang2>")
    async def change_photo_answer(message: Message, lang1, lang2):
        if lang1.capitalize() in TRANSLATED_LANGUAGES.keys()[1:] and lang2.capitalize() in SECOND_LANGUAGE:
            USERS.change_languages(message.from_id, lang1.capitalize(), lang2.capitalize(), 'photo')
            await message.answer(f"Теперь фотоперевод с {genitive(lang1)} на {lang2.lower()}.")
        elif lang2.capitalize() == 'Авто' or lang1.capitalize() == 'Авто':
            await message.answer(f"Функция автоопределение языка не поддерживается в фотопереводе.")
        else:
            await message.answer('Я не знаю такого языка!\nПовтори попытку с одним из моих поддерживаемых языков.')

    # /random_word
    @bot.on.private_message(text="/random_word")
    async def send_welcome(message: Message):
        word = random_word()
        src, dest = USERS.get_data(message.from_id, 'def')
        dest = TRANSLATED_LANGUAGES[dest.capitalize()]
        result = '\n'.join(Translator.translate(word.split('\n'), 'en', dest))

        await message.answer(f"Ваше слово:\n{word}\n\nПеревод:\n{result}")

    # перевод фото
    @bot.on.private_message(attachment='photo')
    async def func(message: Message):
        try:
            await message.answer('Внимание! Фотоперевод может занять значительное время.')
            response = requests.get(message.attachments[0].photo.sizes[-5].url, stream=True)
            response.raw.decode_content = True
            image = Image.open(response.raw)

            src, dest = USERS.get_data(message.from_id)[2:]
            src, dest = LANGUAGES_FOR_PHOTOES[src.capitalize()], TRANSLATED_LANGUAGES[dest.capitalize()]

            text, result = Translator.get_text_and_translate(image, src, dest)
            text, result = '\n'.join(text), '\n'.join(result)

            await message.answer('Текст на фото:\n\n' + text)
            await message.answer('Переведенный текст:\n\n' + result)
        except Exception:
            await message.answer('Извините, произошли технические неполадки.')

    # ответы на текст
    @bot.on.private_message(text="<msg>")
    async def answer(message: Message, msg):
        if msg == 'Обычный перевод':  # продолжение /all_languages
            start = 'Надеюсь, ты найдешь нужный язык!)\n\n'
            text = start + '\n'.join([i for i in TRANSLATED_LANGUAGES.keys()])
            await message.answer(text)

        elif msg == 'Фотоперевод':  # продолжение /all_languages
            start = ('Вот языки, С КОТОРОЫХ ты можешь перевести фото. Список языков для '
                     'перевода такой же, как и в обычном.\n'
                     'Надеюсь, ты найдешь нужный язык!)\n\n')
            text = start + '\n'.join([i for i in LANGUAGES_FOR_PHOTOES.keys()])
            await message.answer(text)

        else:
            src, dest = USERS.get_data(message.from_id)[:2]
            src, dest = TRANSLATED_LANGUAGES[src.capitalize()], TRANSLATED_LANGUAGES[dest.capitalize()]
            print(f"{message.text}")
            result = '\n'.join(Translator.translate(message.text.split('\n'), src, dest))
            await message.answer(result)

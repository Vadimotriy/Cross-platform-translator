import os
import soundfile

from aiogram import Bot, types, html, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from io import BytesIO
from os import path
from PIL import Image

from constants import *
from bot import USERS, Translator
from functions import genitive, random_word

router = Router()
router_for_translate = Router()


def main():
    # /start
    @router.message(F.text, Command('start'))
    async def send_welcome(message: types.Message):
        lang_def_1, lang_def_2, lang_photo_3, lang_photo_4 = USERS.get_data(message.from_user.id)
        lang_aud_1, lang_aud_2 = USERS.get_data(message.from_user.id, 'audio')

        builder = ReplyKeyboardBuilder()
        buttons = ['/change_lang_def', '/fast_change_def', '/change_lang_photo', '/fast_change_photo',
                   '/change_lang_audio', '/fast_change_audio', '/all_languages', '/random_word', '/help']
        for i in buttons:
            builder.add(types.KeyboardButton(text=str(i)))
        builder.adjust(2)

        await message.answer(
            f"Привет {html.bold(html.quote(message.from_user.first_name))}!\n\n"
            "Я здесь, чтобы помочь с переводом. Напиши что угодно, и я переведу это на нужный язык.\n\n"
            f"Сейчас стоит обычный перевод с <b>{genitive(lang_def_1.lower())}</b> на <b>{lang_def_2.lower()}</b>.\n"
            f"Фотоперевод с <b>{genitive(lang_photo_3.lower())}</b> на <b>{lang_photo_4.lower()}</b>.\n"
            f"Аудиоперевод с <b>{genitive(lang_aud_1.lower())}</b> на <b>{lang_aud_2.lower()}</b>.\n\n"
            "О смене языка и о многом другом ты узнаешь в /help.\n\n"
            "Всё просто! 😎",
            parse_mode=ParseMode.HTML, reply_markup=builder.as_markup(resize_keyboard=True)
        )

    # /help
    @router.message(F.text, Command('help'))
    async def send_help(message: types.Message):
        lang_def_1, lang_def_2, lang_photo_3, lang_photo_4 = USERS.get_data(message.from_user.id)
        lang_aud_1, lang_aud_2 = USERS.get_data(message.from_user.id, 'audio')
        await message.answer(
            "/help - меню помощи\n"
            "/change_lang_def - поменять языки для обычного перевода\n"
            "/change_lang_photo - поменять языки для фотоперевода\n"
            "/change_lang_audio - поменять языки для аудиоперевода\n"
            "/fast_change_def - меняет местами языки для обычно перевода\n"
            "/fast_change_photo - меняет местами языки для фотоперевода\n"
            "/fast_change_audio - меняет местами языки для аудиоперевода\n"
            "/all_languages - списки всех языков\n"
            "/random_word - случайное слово на английском и его перевод на выбранный язык\n\n"
            "Чтобы перевести текст, отправьте сообщение на выбранном языке\n"
            "Чтобы перевести фото, отправьте фото с текстом на выбранном языке\n"
            "Чтобы перевести голосовое сообщение, отправьте голосовое сообщение МЕНЕЕ 40 СЕКУНД на выбранном языке\n\n"
            f"Сейчас стоит обычный перевод с <b>{genitive(lang_def_1.lower())}</b> на <b>{lang_def_2.lower()}</b>\n"
            f"Фотоперевод с <b>{genitive(lang_photo_3.lower())}</b> на <b>{lang_photo_4.lower()}</b>\n"
            f"Аудиоперевод с <b>{genitive(lang_aud_1)}</b> на <b>{lang_aud_2}</b>\n\n"
            f"В обычном переводе есть особый язык - <i>'Автоопределение языка'.</i> "
            f"Он автоматически опередят язык текста. С него можно только переводить.", parse_mode=ParseMode.HTML
        )

    # /change_lang_audio
    @router.message(F.text, StateFilter(None), Command('change_lang_audio'))
    async def choose_audio(message: types.Message, state: FSMContext):
        await message.answer(text="Введи язык голосового сообщения:")
        await state.set_state(ChangeAudLanguage.choosing_first_lang)

    # выбор второго языка
    @router.message(ChangeAudLanguage.choosing_first_lang, F.text.capitalize().in_(LANGUAGES_FOR_AUDIO.keys()))
    async def choose_audio_lang(message: types.Message, state: FSMContext):
        await state.update_data(chosen_lang=message.text.lower())
        await message.answer(text="Теперь, введи язык перевода: ")
        await state.set_state(ChangeAudLanguage.choosing_second_lang)

    # ошибочный выбор
    @router.message(StateFilter("ChangeAudLanguage:choosing_first_lang"))
    async def choose_audio_incorrectly(message: types.Message):
        await message.answer(
            text="Я не знаю такого языка!\n\n"
                 "Введи один из моих поддерживаемых языков:"
        )

    # Итог
    @router.message(ChangeAudLanguage.choosing_second_lang, F.text.capitalize().in_(SECOND_LANGUAGE))
    async def audio_chosen(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        USERS.change_languages(message.from_user.id, user_data['chosen_lang'], message.text.lower(), 'audio')
        await message.answer(
            text=f"Вы выбрали аудиоперевод с <b>{genitive(user_data['chosen_lang'])}</b> на <b>{message.text.lower()}</b>.\n",
            parse_mode=ParseMode.HTML
        )
        await state.clear()

    # ошибочный выбор
    @router.message(ChangeAudLanguage.choosing_second_lang)
    async def audio_chosen_incorrectly(message: types.Message):
        await message.answer(
            text="Я не знаю такого языка!\n\n"
                 "Введи один из моих поддерживаемых языков:"
        )









    # /change_lang_photo
    @router.message(F.text, StateFilter(None), Command('change_lang_photo'))
    async def choose_photo(message: types.Message, state: FSMContext):
        await message.answer(text="Введи язык текста:")
        await state.set_state(ChangePhotoLanguage.choosing_first_lang)

    # выбор второго языка
    @router.message(ChangePhotoLanguage.choosing_first_lang, F.text.capitalize().in_(LANGUAGES_FOR_PHOTOES.keys()))
    async def choose_photo_lang(message: types.Message, state: FSMContext):
        await state.update_data(chosen_lang=message.text.lower())
        await message.answer(text="Теперь, введи язык перевода: ")
        await state.set_state(ChangePhotoLanguage.choosing_second_lang)

    # ошибочный выбор
    @router.message(StateFilter("ChangePhotoLanguage:choosing_first_lang"))
    async def choose_photo_incorrectly(message: types.Message):
        await message.answer(
            text="Я не знаю такого языка!\n\n"
                 "Введи один из моих поддерживаемых языков:"
        )

    # Итог
    @router.message(ChangePhotoLanguage.choosing_second_lang, F.text.capitalize().in_(SECOND_LANGUAGE))
    async def photo_chosen(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        USERS.change_languages(message.from_user.id, user_data['chosen_lang'], message.text.lower(), 'photo')
        await message.answer(
            text=f"Вы выбрали фотоперевод с <b>{genitive(user_data['chosen_lang'])}</b> на <b>{message.text.lower()}</b>.\n",
            parse_mode=ParseMode.HTML
        )
        await state.clear()

    # ошибочный выбор
    @router.message(ChangePhotoLanguage.choosing_second_lang)
    async def photo_chosen_incorrectly(message: types.Message):
        await message.answer(
            text="Я не знаю такого языка!\n\n"
                 "Введи один из моих поддерживаемых языков:"
        )






    # /fast_change_def
    @router.message(F.text, StateFilter(None), Command('fast_change_def'))
    async def fast_change_def(message: types.Message):
        languages = USERS.get_data(message.from_user.id)
        if languages[0].lower() == 'автоопределение языка':
            await message.answer(f"Нельзя перевести на автоопределение языка.")
            return
        USERS.change_languages(message.from_user.id, languages[1], languages[0], 'def')
        await message.answer(f"Теперь перевод с {genitive(languages[1])} на {languages[0].lower()}\n")

    # /fast_change_photo
    @router.message(F.text, StateFilter(None), Command('fast_change_photo'))
    async def fast_change_def(message: types.Message):
        languages = USERS.get_data(message.from_user.id)
        if languages[3] in LANGUAGES_FOR_PHOTOES.keys():
            USERS.change_languages(message.from_user.id, languages[3], languages[2], 'photo')
            await message.answer(f"Теперь фотоперевод с {genitive(languages[3])} на {languages[2].lower()}.")
        else:
            await message.answer(f"Фотоперевода с {genitive(languages[3])} нет.")

    # /fast_change_photo
    @router.message(F.text, StateFilter(None), Command('fast_change_audio'))
    async def fast_change_def(message: types.Message):
        lang1, lang2 = USERS.get_data(message.from_user.id, 'audio')
        if lang2 in LANGUAGES_FOR_AUDIO.keys():
            USERS.change_languages(message.from_user.id, lang2, lang1, 'audio')
            await message.answer(f"Теперь aудиоперевод с {genitive(lang2)} на {lang1.lower()}.")
        else:
            await message.answer(f"Аудиоперевода с {genitive(lang2)} нет.")

    # /change_lang_def
    @router.message(F.text, StateFilter(None), Command('change_lang_def'))
    async def choose_def(message: types.Message, state: FSMContext):
        await message.answer(text="Введи язык текста:")
        await state.set_state(ChangeDefLanguage.choosing_first_lang)

    # выбор второго языка
    @router.message(ChangeDefLanguage.choosing_first_lang, F.text.capitalize().in_(TRANSLATED_LANGUAGES.keys()))
    async def choose_def_lang(message: types.Message, state: FSMContext):
        await state.update_data(chosen_lang=message.text.lower())
        await message.answer(text="Теперь, введи язык перевода: ")
        await state.set_state(ChangeDefLanguage.choosing_second_lang)

    # ошибочный выбор
    @router.message(StateFilter("ChangeDefLanguage:choosing_first_lang"))
    async def choose_def_incorrectly(message: types.Message):
        await message.answer(
            text="Я не знаю такого языка!\n\n"
                 "Введи один из моих поддерживаемых языков:"
        )

    # итог
    @router.message(ChangeDefLanguage.choosing_second_lang, F.text.capitalize().in_(SECOND_LANGUAGE))
    async def def_chosen(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        USERS.change_languages(message.from_user.id, user_data['chosen_lang'], message.text.lower(), 'def')
        await message.answer(
            text=f"Вы выбрали перeвод с <b>{genitive(user_data['chosen_lang'])}</b> на <b>{message.text.lower()}</b>.\n",
            parse_mode=ParseMode.HTML
        )
        await state.clear()

    # ошибочный выбор
    @router.message(ChangeDefLanguage.choosing_second_lang)
    async def def_chosen_incorrectly(message: types.Message):
        await message.answer(
            text="Я не знаю такого языка!\n\n"
                 "Введи один из моих поддерживаемых языков:"
        )

    # /all_languages
    @router.message(F.text, Command('all_languages'))
    async def send_welcome(message: types.Message):
        buttons = []
        for i in ['Обычный перевод', "Фотоперевод", 'Аудиоперевод']:
            buttons.append([types.InlineKeyboardButton(text=i, callback_data=i)])
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

        await message.answer("Для какого перевода тебя интересует набор языков?", reply_markup=keyboard)

    # /random_word
    @router.message(F.text, Command('random_word'))
    async def send_welcome(message: types.Message):
        word = random_word()
        src, dest = USERS.get_data(message.from_user.id, 'def')
        dest = TRANSLATED_LANGUAGES[dest.capitalize()]
        result = '\n'.join(Translator.translate(word.split('\n'), 'en', dest))

        await message.answer(f"Ваше слово:<i>\n{word}</i>\n\nПеревод:\n<i>{result}</i>",
                             parse_mode=ParseMode.HTML)

    # перевод слов
    @router_for_translate.message(F.text)
    async def echo(message: types.Message):
        try:
            print(f"{message.from_user.full_name}:\t{message.text}")
            await message.bot.send_chat_action(message.chat.id, 'typing')
            src, dest = USERS.get_data(message.from_user.id)[:2]
            src, dest = TRANSLATED_LANGUAGES[src.capitalize()], TRANSLATED_LANGUAGES[dest.capitalize()]
            result = '\n'.join(Translator.translate(message.text.split('\n'), src, dest))
            await message.answer(result)
        except Exception:
            await message.answer('Извините, произошли какие-то технические неполадки.')

    # фотоперевод
    @router_for_translate.message(F.photo)
    async def photo_msg(message: types.Message, bot: Bot):
        try:
            await message.bot.send_chat_action(message.chat.id, 'typing')
            image = BytesIO()
            await bot.download(message.photo[-1], destination=image)
            image = Image.open(image)
            src, dest = USERS.get_data(message.from_user.id)[2:]
            src, dest = LANGUAGES_FOR_PHOTOES[src.capitalize()], TRANSLATED_LANGUAGES[dest.capitalize()]

            text, result = Translator.get_text_and_translate(image, src, dest)
            text, result = '\n'.join(text), '\n'.join(result)
            await message.answer('Текст на фото:\n\n' + text)
            print(f"{message.from_user.full_name}:\t{text}")
            await message.answer('Переведенный текст:\n\n' + result)
        except Exception:
            await message.answer('Извините, перевод фото с этого языка недоступен по техническим неполадкам.')

    @router_for_translate.message(F.voice)
    async def audio_msg(message: types.Message, bot: Bot):
        try:
            split_up = path.splitext(message.voice.file_id)
            file_name = f'Data/aud_{message.from_user.id}.ogg'
            await bot.download(message.voice, file_name)

            file_name_wav = f'Data/aud_{message.from_user.id}.wav'
            data, samplerate = soundfile.read(file_name)
            soundfile.write(file_name_wav, data, samplerate)

            src, dest = USERS.get_data(message.from_user.id, 'audio')
            src, dest = LANGUAGES_FOR_AUDIO[src.capitalize()], TRANSLATED_LANGUAGES[dest.capitalize()]
            text, result = Translator.get_and_translate_audio(file_name_wav, src, dest)

            result = '\n'.join(result)
            await message.answer('Текст в голосовом сообщении:\n\n' + text)
            print(f"{message.from_user.full_name}:\t{text}")
            await message.answer('Переведенный текст:\n\n' + result)

            os.remove(file_name)
            os.remove(file_name_wav)

        except TimeoutError:
            await message.answer('Ваше голосовое сообщение больше 40 секунд!')
        except Exception:
            await message.answer('Извините, произошла ошибка при скачивании голосового сообщения.')


def callbacks():
    # список обычного перевода
    @router.callback_query(F.data == "Обычный перевод")
    async def send_random_value(callback: types.CallbackQuery):
        start = 'Надеюсь, ты найдешь нужный язык!)\n\n'
        text = start + '\n'.join([i for i in TRANSLATED_LANGUAGES.keys()])
        await callback.message.answer(text)
        await callback.answer()

    # список фото перевода
    @router.callback_query(F.data == "Фотоперевод")
    async def send_random_value(callback: types.CallbackQuery):
        start = ('Вот языки, С КОТОРОЫХ ты можешь перевести фото. Список языков для '
                 'перевода такой же, как и в обычном.\n\n'
                 'Надеюсь, ты найдешь нужный язык!)\n\n')
        text = start + '\n'.join([i for i in LANGUAGES_FOR_PHOTOES.keys()])
        await callback.message.answer(text)
        await callback.answer()

    # список фото перевода
    @router.callback_query(F.data == "Аудиоперевод")
    async def send_random_value(callback: types.CallbackQuery):
        start = ('Вот языки, С КОТОРОЫХ ты можешь перевести голосовое сообщение. Список языков для '
                 'перевода такой же, как и в обычном.\n\n'
                 'Надеюсь, ты найдешь нужный язык!)\n\n')
        text = start + '\n'.join([i for i in LANGUAGES_FOR_AUDIO.keys()])
        await callback.message.answer(text)
        await callback.answer()


main()
callbacks()

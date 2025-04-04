import random
import pymorphy3

from vkbottle import Keyboard, KeyboardButtonColor, Text


def genitive(word):  # функция по переводу названий языков в родительный падеж
    if word.lower() == 'автоопределение языка':
        return word
    ost = ''
    if word.lower() in ['китайский (торговый)', 'китайский (упрощенный)', 'курдский (курманджи)']:
        word, ost = word.split()
    try:
        morph = pymorphy3.MorphAnalyzer()
        word = morph.parse(word)[0].inflect({'gent'})
        return (word.word + ' ' + ost).strip()
    except Exception:
        return word + ost


def random_word():  # выбор случайного слова из 9999
    with open('Data/top-9999-words.txt') as file:
        words = list(map(str.strip, file.read().split('\n')))

    return random.choice(words)


def make_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    commands = ['/change_lang_def', '/change_lang_photo',
                '/fast_change_def', '/fast_change_photo',
                '/all_languages', '/random_word', '/help']
    for i in range(1, len(commands) + 1):
        keyboard.add(Text(commands[i - 1]), color=KeyboardButtonColor.PRIMARY)
        if i % 2 == 0:
            keyboard.row()

    return keyboard

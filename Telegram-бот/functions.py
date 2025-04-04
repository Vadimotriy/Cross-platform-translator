import random
import pymorphy3


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

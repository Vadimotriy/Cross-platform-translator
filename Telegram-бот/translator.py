import easyocr
import speech_recognition
import soundfile

from googletrans import Translator
from constants import *


class My_Translator:  # класс по работе с переводом
    def __init__(self):
        self.translator = Translator()
        self.rec = speech_recognition.Recognizer()
        print(dir(self.rec))

    def translate(self, text, src, dest):  # Перевод входных данных на требования библиотеки googleTrans
        try:
            if src is None:
                for i in text:
                    if i.strip() != '':
                        src = self.translator.detect(i).lang
                        break

            result = []
            for i in text:
                if i.strip() != '':
                    translated = self.translator.translate(i, dest, src).text
                    result.append(translated)
                else:
                    result.append('')

            return result

        except Exception:
            raise InternetException

    def translate_file(self, file, src, dest):  # получение текста из файла и его перевод
        with open(file, encoding='utf-8') as text:
            strings = text.read().split('\n')
            translated_strings = self.translate(strings, src, dest)

        return strings, translated_strings

    def get_text_and_translate(self, img, src, dest):  # получение текста из изображения и его перевод
        src_easyocr, src_googletrans = (src[1], src[0]) if type(src) is tuple else (src, src)

        self.reader = easyocr.Reader([src_easyocr], gpu=True)
        text = self.reader.readtext(img, detail=0, paragraph=True)
        translated_text = self.translate(text, src_googletrans, dest)

        return text, translated_text

    def get_and_translate_audio(self, audio, src, dest):
        f = soundfile.SoundFile(audio)
        dur = round(f.frames / f.samplerate)
        if dur > 40:
            raise TimeoutError
        else:
            src_googletrans, src_speech = src
            aud = speech_recognition.AudioFile(audio)
            with aud as source:
                audio = self.rec.record(source)
                text = self.rec.recognize_google(audio, language=src_speech)
                translated_text = self.translate([text], src_googletrans, dest)

            return text, translated_text

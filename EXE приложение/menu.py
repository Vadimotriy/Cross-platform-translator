from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap, QIcon

from io import BytesIO
from PIL import Image

from constants import TRANSLATED_LANGUAGES, LANGUAGES_FOR_PHOTOES, InternetException
from design import DesignMainWindow, DesignFiles, DesignPhotoes
from translator import My_Translator


class MainWindow(QMainWindow, DesignMainWindow):  # главное окно
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.LANGUAGE = TRANSLATED_LANGUAGES
        self.translator = My_Translator()
        self.initUI()

    def initUI(self):  # настройка дизайна и подключение кнопок
        self.setWindowTitle('Переводчик')
        self.setWindowIcon(QIcon('Data/Translator.ico'))

        for i in self.LANGUAGE.keys():
            self.text_language.addItem(i)
        self.text_language.setCurrentText('Русский')

        for i in list(self.LANGUAGE.keys())[1:]:
            self.translated_text_language.addItem(i)
        self.translated_text_language.setCurrentText('Английский')

        self.translate.clicked.connect(self.run)
        self.translate_file.clicked.connect(self.file_run)
        self.translate_image.clicked.connect(self.image_run)
        self.settings.clicked.connect(self.change_run)

        self.file_menu = FileMenu(self)  # подключение основных окон
        self.photo_menu = PhotoMenu(self)

    def run(self):  # перевод текста
        text = self.text.toPlainText().split('\n')

        if text not in [[''], [], [' ']]:
            src = self.LANGUAGE[self.text_language.currentText()]
            dest = self.LANGUAGE[self.translated_text_language.currentText()]

            try:
                self.statusbar.clearMessage()
                translated_text = self.translator.translate(text, src, dest)

                self.translated_text.clear()
                for cur_text in translated_text:  # размещение текста
                    self.translated_text.appendPlainText(cur_text)

            except InternetException:
                self.statusbar.showMessage('Ошибка соединения!')
            except Exception:
                self.statusbar.showMessage('Ошибка!')

    def file_run(self):  # открытие нового окна по переводу файлов txt
        self.file_menu.show()

    def image_run(self):  # открытие нового окна по переводу изображений
        self.photo_menu.show()

    def change_run(self):  # меняем язык
        src = self.text_language.currentText()
        dest = self.translated_text_language.currentText()

        if src != 'Автоопределение языка':
            self.text_language.setCurrentText(dest)
            self.translated_text_language.setCurrentText(src)


class FileMenu(QMainWindow, DesignFiles):  # Окно по переводу txt
    def __init__(self, parent=None):
        super(FileMenu, self).__init__(parent)
        super().setupUi(self)

        self.translator = My_Translator()
        self.LANGUAGE = TRANSLATED_LANGUAGES
        self.initUI()

    def initUI(self):  # настройка дизайна и подключение кнопок
        self.setWindowTitle('Перевод txt')
        self.setWindowIcon(QIcon('Data/Translator.ico'))

        for i in self.LANGUAGE.keys():
            self.original_language.addItem(i)
        self.original_language.setCurrentText('Русский')

        for i in list(self.LANGUAGE.keys())[1:]:
            self.translate_language.addItem(i)
        self.translate_language.setCurrentText('Английский')

        self.choose_file.clicked.connect(self.get_file)
        self.download_button.clicked.connect(self.download)
        self.settings.clicked.connect(self.change_run)

    def get_file(self):  # получение и перевод файла
        src = self.LANGUAGE[self.original_language.currentText()]
        dest = self.LANGUAGE[self.translate_language.currentText()]
        self.file = QFileDialog.getOpenFileName(self, 'Выберите текстовый файл', '', 'Текстовый документ (*.txt)')[0]
        if self.file:
            try:
                self.statusbar.clearMessage()
                strings, translated_strings = self.translator.translate_file(self.file, src, dest)

                self.original_text_from_file.clear()
                self.translated_text_from_file.clear()
                for cur_text in strings:  # размещение текста
                    self.original_text_from_file.appendPlainText(cur_text)
                for cur_text in translated_strings:
                    self.translated_text_from_file.appendPlainText(cur_text)

                self.download_button.setEnabled(True)

            except InternetException:
                self.statusbar.showMessage('Ошибка соединения!')
            except Exception:
                self.statusbar.showMessage('Файл не найден!')

    def change_run(self):  # меняем язык
        src = self.original_language.currentText()
        dest = self.translate_language.currentText()

        if src != 'Автоопределение языка':
            self.original_language.setCurrentText(dest)
            self.translate_language.setCurrentText(src)

    def download(self):  # скачка переведенного файла
        text = self.translated_text_from_file.toPlainText()
        name = self.file.split('/')[-1]

        with open(f'translated_{name}', mode='w', encoding='utf-8') as result:
            print(text, file=result)


class PhotoMenu(QMainWindow, DesignPhotoes):  # Окно по переводу изображений
    def __init__(self, parent=None):
        super(PhotoMenu, self).__init__(parent)
        super().setupUi(self)

        self.translator = My_Translator()
        self.LANGUAGE = LANGUAGES_FOR_PHOTOES
        self.TRANS_LANGUAGE = TRANSLATED_LANGUAGES
        self.initUI()

    def initUI(self):  # дизайн и подключение кнопок
        self.setWindowTitle('Перевод изображений')
        self.setWindowIcon(QIcon('Data/Translator.ico'))

        for i in self.LANGUAGE.keys():
            self.photo_language.addItem(i)
        self.photo_language.setCurrentText('Русский')

        for i in list(self.TRANS_LANGUAGE.keys())[1:]:
            self.translate_photo_language.addItem(i)
        self.translate_photo_language.setCurrentText('Английский')

        self.translate_photo.clicked.connect(self.get_text_from_image)
        self.settings.clicked.connect(self.change_run)

    def get_text_from_image(self):  # Перевод изображения
        src = self.LANGUAGE[self.photo_language.currentText()]
        dest = self.LANGUAGE[self.translate_photo_language.currentText()]
        sorts = 'Картинка (*.jpg);;Картинка (*.png)'
        self.image_name = QFileDialog.getOpenFileName(self, 'Выберите изображение', '', sorts)[0]
        if self.image_name:
            try:
                image = Image.open(self.image_name)
                image = image.convert('RGB')
                with BytesIO() as f:
                    image.save(f, format='JPEG')
                    image = Image.open(f)
                    image.load()

                self.statusbar.clearMessage()  # размещения уменьшенного фото
                pixmap = QPixmap(self.image_name)
                pixmap = pixmap.scaledToWidth(600)
                self.photo.setPixmap(pixmap)

                text_orig, text_trans = self.translator.get_text_and_translate(image, src, dest)

                self.photo_text.clear()
                self.photo_translated_text.clear()
                for cur_text in text_orig:  # размещение текста
                    self.photo_text.appendPlainText(cur_text)
                for cur_text in text_trans:
                    self.photo_translated_text.appendPlainText(cur_text)
            except InternetException:
                self.statusbar.showMessage('Ошибка соединения!')
            except Exception:
                self.statusbar.showMessage('Файл не найден!')

    def change_run(self):  # меняем язык
        src = self.photo_language.currentText()
        dest = self.translate_photo_language.currentText()

        self.photo_language.setCurrentText(dest)
        self.translate_photo_language.setCurrentText(src)

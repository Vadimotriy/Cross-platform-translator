from PyQt6 import QtCore, QtWidgets


class DesignMainWindow(object):  # дизайн главного окна
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 500)
        MainWindow.setMinimumSize(QtCore.QSize(656, 500))
        MainWindow.setStyleSheet("background-color: rgb(247, 248, 251);")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(656, 336))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.text = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.text.setStyleSheet("font: 18px \"PT Sans\";\n"
                                "background-color: #FFF;")
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 2, 0, 1, 1)

        self.translated_text = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.translated_text.setStyleSheet("font: 18px \"PT Sans\";\n"
                                           "background-color: #FFF;")
        self.translated_text.setReadOnly(True)
        self.translated_text.setObjectName("translated_text")
        self.gridLayout.addWidget(self.translated_text, 2, 1, 1, 1)

        self.translated_text_language = QtWidgets.QComboBox(parent=self.centralwidget)
        self.translated_text_language.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                                    "text-decoration: underline;\n"
                                                    "border: 1px solid  rgb(242, 253, 255);\n"
                                                    "background-color: #FFF;")
        self.translated_text_language.setObjectName("translated_text_language")
        self.gridLayout.addWidget(self.translated_text_language, 1, 1, 1, 1)

        self.text_language = QtWidgets.QComboBox(parent=self.centralwidget)
        self.text_language.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                         "text-decoration: underline;\n"
                                         "border: 1px solid  rgb(242, 253, 255);\n"
                                         "background-color: #FFF;")
        self.text_language.setObjectName("text_language")
        self.gridLayout.addWidget(self.text_language, 1, 0, 1, 1)

        self.label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_1.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.translate_image = QtWidgets.QPushButton(parent=self.centralwidget)
        self.translate_image.setStyleSheet("font: 12pt \"PT Sans\";\n"
                                           "border: 1px solid rgb(214, 214, 214);\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(214, 214, 214);")
        self.translate_image.setObjectName("translate_image")
        self.gridLayout_2.addWidget(self.translate_image, 1, 1, 1, 1)

        self.translate_file = QtWidgets.QPushButton(parent=self.centralwidget)
        self.translate_file.setStyleSheet("font: 12pt \"PT Sans\";\n"
                                          "border: 1px solid rgb(214, 214, 214);\n"
                                          "border-radius: 20px;\n"
                                          "background-color: rgb(214, 214, 214);")
        self.translate_file.setObjectName("translate_file")
        self.gridLayout_2.addWidget(self.translate_file, 1, 0, 1, 1)

        self.translate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.translate.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                     "border: 1px solid rgb(214, 214, 214);\n"
                                     "border-radius: 20px;\n"
                                     "background-color: rgb(214, 214, 214);")
        self.translate.setObjectName("translate")
        self.gridLayout_2.addWidget(self.translate, 0, 0, 1, 2)

        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.settings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.settings.setStyleSheet("font: 12pt \"PT Sans\";\n"
                                    "border: 1px solid rgb(214, 214, 214);\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(214, 214, 214);\n"
                                    "padding: 3px;\n"
                                    "")
        self.settings.setObjectName("settings")
        self.gridLayout_3.addWidget(self.settings, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Текст"))
        self.label_5.setText(_translate("MainWindow", "Переведенный текст"))
        self.translate_image.setText(_translate("MainWindow", "Перевести изображение"))
        self.translate_file.setText(_translate("MainWindow", "Перевести txt"))
        self.translate.setText(_translate("MainWindow", "Перевести"))
        self.settings.setText(_translate("MainWindow", "Поменять язык"))


class DesignFiles(object):  # Дизайн окна перевода txt
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("background-color: rgb(247, 248, 251);")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.translate_language = QtWidgets.QComboBox(parent=self.centralwidget)
        self.translate_language.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                              "text-decoration: underline;\n"
                                              "border: 1px solid  rgb(171, 171, 171);\n"
                                              "background-color: #FFF;")
        self.translate_language.setObjectName("translate_language")
        self.gridLayout.addWidget(self.translate_language, 1, 1, 1, 1)

        self.choose_file = QtWidgets.QPushButton(parent=self.centralwidget)
        self.choose_file.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                       "border: 1px solid rgb(214, 214, 214);\n"
                                       "border-radius: 20px;\n"
                                       "background-color: rgb(214, 214, 214);")
        self.choose_file.setObjectName("choose_file")
        self.gridLayout.addWidget(self.choose_file, 3, 0, 1, 2)

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.original_language = QtWidgets.QComboBox(parent=self.centralwidget)
        self.original_language.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                             "text-decoration: underline;\n"
                                             "border: 1px solid  rgb(171, 171, 171);\n"
                                             "background-color: #FFF;")
        self.original_language.setObjectName("original_language")
        self.gridLayout.addWidget(self.original_language, 1, 0, 1, 1)

        self.original_text_from_file = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.original_text_from_file.setStyleSheet("font: 16px \"PT Sans\";\n"
                                                   "background-color: #FFF;\n"
                                                   "border: 1px solid  rgb(171, 171, 171);")
        self.original_text_from_file.setReadOnly(True)
        self.original_text_from_file.setObjectName("original_text_from_file")
        self.gridLayout.addWidget(self.original_text_from_file, 2, 0, 1, 1)

        self.translated_text_from_file = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.translated_text_from_file.setStyleSheet("font: 16px \"PT Sans\";\n"
                                                     "background-color: #FFF;\n"
                                                     "border: 1px solid  rgb(171, 171, 171);")
        self.translated_text_from_file.setReadOnly(True)
        self.translated_text_from_file.setObjectName("translated_text_from_file")
        self.gridLayout.addWidget(self.translated_text_from_file, 2, 1, 1, 1)

        self.download_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.download_button.setEnabled(False)
        self.download_button.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                           "border: 1px solid rgb(214, 214, 214);\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(214, 214, 214);")
        self.download_button.setCheckable(False)
        self.download_button.setObjectName("download_button")
        self.gridLayout.addWidget(self.download_button, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.settings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.settings.setStyleSheet("font: 12pt \"PT Sans\";\n"
                                    "border: 1px solid rgb(214, 214, 214);\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(214, 214, 214);\n"
                                    "padding: 3px;\n"
                                    "")
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 5, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignRight)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.choose_file.setText(_translate("MainWindow", "Выбрать файл"))
        self.label.setText(_translate("MainWindow", "Оригинальный текст"))
        self.label_2.setText(_translate("MainWindow", "Переведенный файл"))
        self.download_button.setText(_translate("MainWindow", "Скачать"))
        self.settings.setText(_translate("MainWindow", "Поменять язык"))


class DesignPhotoes(object):  # Дизайн окна перевода фото
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 820)
        MainWindow.setMinimumSize(QtCore.QSize(1240, 820))
        MainWindow.setStyleSheet("background-color: rgb(247, 248, 251);")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.translate_photo = QtWidgets.QPushButton(parent=self.centralwidget)
        self.translate_photo.setStyleSheet("font: 18pt \"PT Sans\";\n"
                                           "border: 1px solid rgb(214, 214, 214);\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(214, 214, 214);")
        self.translate_photo.setObjectName("translate_photo")
        self.gridLayout.addWidget(self.translate_photo, 3, 0, 1, 3)

        self.photo_translated_text = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.photo_translated_text.setReadOnly(True)
        self.photo_translated_text.setStyleSheet("font: 16px \"PT Sans\";\n"
                                                 "background-color: #FFF;\n"
                                                 "border: 1px solid  rgb(171, 171, 171);")
        self.photo_translated_text.setObjectName("photo_translated_text")
        self.gridLayout.addWidget(self.photo_translated_text, 2, 2, 1, 1)

        self.photo_text = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.photo_text.setReadOnly(True)
        self.photo_text.setStyleSheet("font: 16px \"PT Sans\";\n"
                                      "background-color: #FFF;\n"
                                      "border: 1px solid  rgb(171, 171, 171);")
        self.photo_text.setObjectName("photo_text")
        self.gridLayout.addWidget(self.photo_text, 2, 1, 1, 1)

        self.photo_language = QtWidgets.QComboBox(parent=self.centralwidget)
        self.photo_language.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                          "text-decoration: underline;\n"
                                          "border: 1px solid  rgb(171, 171, 171);\n"
                                          "background-color: #FFF;")
        self.photo_language.setObjectName("photo_language")
        self.gridLayout.addWidget(self.photo_language, 1, 1, 1, 1)

        self.translate_photo_language = QtWidgets.QComboBox(parent=self.centralwidget)
        self.translate_photo_language.setStyleSheet("font: 16pt \"PT Sans\";\n"
                                                    "text-decoration: underline;\n"
                                                    "border: 1px solid  rgb(171, 171, 171);\n"
                                                    "background-color: #FFF;")
        self.translate_photo_language.setObjectName("translate_photo_language")
        self.gridLayout.addWidget(self.translate_photo_language, 1, 2, 1, 1)

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setStyleSheet("font: 18pt \"PT Sans\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.photo.setMinimumSize(QtCore.QSize(600, 600))
        self.photo.setObjectName("photo")
        self.gridLayout.addWidget(self.photo, 1, 0, 2, 1)

        self.settings = QtWidgets.QPushButton(parent=self.centralwidget)
        self.settings.setStyleSheet("font: 12pt \"PT Sans\";\n"
                                    "border: 1px solid rgb(214, 214, 214);\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(214, 214, 214);\n"
                                    "padding: 3px;\n"
                                    "")
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 4, 0, 2, 3, QtCore.Qt.AlignmentFlag.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.translate_photo.setText(_translate("MainWindow", "Выбрать изображение"))
        self.label_3.setText(_translate("MainWindow", "Текст с изображения"))
        self.label_2.setText(_translate("MainWindow", "Ваше фото"))
        self.label_4.setText(_translate("MainWindow", "Перевод с изображения"))
        self.settings.setText(_translate("MainWindow", "Поменять язык"))

import sqlite3


class MyDict:
    def __init__(self):  # открытие БД (базы данных)
        self.connection = sqlite3.connect('Data/Data.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Languages_def (
        USER_ID INTEGER PRIMARY KEY,
        Language_first TEXT NOT NULL,
        Language_second TEXT NOT NULL)''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Languages_photo (
        USER_ID INTEGER PRIMARY KEY,
        Language_first TEXT NOT NULL,
        Language_second TEXT NOT NULL)''')

    def add_user(self, id):  # добавление человека в БД
        self.cursor.execute('INSERT INTO Languages_def (USER_ID, Language_first, Language_second) VALUES (?, ?, ?)',
                            (id, 'Английский', 'Русский'))
        self.cursor.execute('INSERT INTO Languages_photo (USER_ID, Language_first, Language_second) VALUES (?, ?, ?)',
                            (id, 'Английский', 'Русский'))
        self.connection.commit()

    def get_data(self, id, type='all'):  # выгрузка данных из БД
        all_users = self.cursor.execute('SELECT USER_ID FROM Languages_def').fetchall()
        if (id,) not in all_users:
            self.add_user(id)

        default = self.cursor.execute('SELECT Language_first, Language_second FROM Languages_def '
                                      'WHERE USER_ID = ?', (int(id),)).fetchone()
        photo = self.cursor.execute('SELECT Language_first, Language_second FROM Languages_photo '
                                    'WHERE USER_ID = ?', (int(id),)).fetchone()

        if type == 'all':
            return default + photo
        return photo if type == 'photo' else default

    def change_languages(self, id, first, second, type):  # Изменение языка в БД
        all_users = self.cursor.execute('SELECT USER_ID FROM Languages_def').fetchall()
        if (id,) not in all_users:
            self.add_user(id)

        update = f"""UPDATE Languages_{type} SET Language_first = ? WHERE USER_ID = ?"""
        self.cursor.execute(update, (first, id))
        update = f"""UPDATE Languages_{type} SET Language_second = ? WHERE USER_ID = ?"""
        self.cursor.execute(update, (second, id))
        self.connection.commit()

import sqlite3
import data.config

class DataBaseConnection:
    def __init__(self, login, password, path_to_db=data.config.path_to_database):
        self.login = login
        self.path_to_db = path_to_db
        self.password = password

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    # @staticmethod
    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data


class Users:
    def __init__(self, connection):
        # if not self.try_log_in(login, password):
        #     raise Exception('Пользователя с такими данными не существует! Неверен логин/пароль!')
        self.connection = connection
        self.create_table_of_users()

    def create_table_of_users(self):
        sql = '''
        create table IF NOT EXISTS `users` (
          `user_id` INTEGER PRIMARY KEY AUTOINCREMENT not null,
          `login` varchar(255) not null,
          `password` varchar(255) not null
        )'''
        self.connection.execute(sql, commit=True)


    # @staticmethod
    def is_login_exist(self, login):
        # проверяет существует ли пользователь с указанным логином
        sql = "SELECT * FROM users WHERE login=?"
        result = self.connection.execute(sql, (login,), fetchone=True)

        if result is not None:
            print("Пользователь с таким логином существует")
            return True  # существует
        else:
            print("Пользователя с таким логином не существует")
            return False  # не существует

    # @staticmethod
    def try_log_in(self, login, password):
        # проверяет cуществует ли пользователь с логин/пароль
        sql = "SELECT * FROM users WHERE login=? AND password=?"
        result = self.connection.execute(sql, (login, password), fetchone=True)

        if result is not None:
            print("Пользователь с таким логином и паролем существует")
            return True  # существует
        else:
            print("Пользователя с таким логином и паролем не существует")
            return False  # не существует (Неверен логин/пароль)

    # @staticmethod
    def add_new_user(self, login, password):
        if self.is_login_exist(login):
            print('Пользователя с таким логином уже существует!')
            return False
        # добавляем в бд нового пользователя
        sql_insert = "INSERT INTO users (login, password) VALUES (?, ?)"
        self.connection.execute(sql_insert, (login, password), commit=True)
        print("Пользователь успешно добавлен")
        return True

    # @staticmethod
    def get_user_login_by_id(self, id):
        # возвращает логин пользователя по id
        sql = "SELECT login FROM users WHERE user_id =?"
        result = self.connection.execute(sql, (id,), fetchone=True)
        login = result[0]
        if result is not None:
            # print("Логин пользователя по его id: ")
            return login


    # @staticmethod
    def get_user_id_by_login(self, login):
        # возвращает id пользователя по логину (логин уникален для каждого пользователя)
        sql = "SELECT user_id FROM users WHERE login=?"
        result = self.connection.execute(sql, (login,), fetchone=True)
        id = result[0]
        if result is not None:
            # print("id пользователя по его логину")
            return id


class Desks:
    def __init__(self, connection):
        self.path_to_db = path_to_db
        self.connection = connection
        self.create_desk()

    def create_desk(self, desk_name, desk_type):
        sql = '''
        create table IF NOT EXISTS `desks` (
          "desk_id" INTEGER PRIMARY KEY AUTOINCREMENT not null,
          "desk_name" varchar(255) not null,
          "public" BOOLEAN not null,
          "owner_login" varchar(255) not null
        )'''
        self.connection.execute(sql, commit=True)
        # создаём доску в бд
        # владелец доски self.login
        # False - доска с таким именем уже существует
        # return True  # True - доска успешно создана

    def get_owned_desks(self):
        # список досок которыми владает пользователь (self.login) в формате (desk_id, desk_name, public, owner_login)

        return [(0, 'Доска 1', 0, 'Myself'), (1, 'Доска для 2112', 1, 'Myself')]

    # def get_public_desks(self):
    #     # список публичных досок досок в формате (desk_id, desk_name, public)
    #
    #     return [(33, 'Доска 333', 1, 'Sera'), (222, 'Доска 77', 1, 'Bob')]
    #
    # def can_edit_desk(self, desk_id):
    #     # можем ли мы редактировать доску
    #     # доску может редактировать владелец или пользователь из таблицы "права на редактирования"
    #
    #     return True
    #
    # @staticmethod
    # def get_desk_name_by_desk_id(desk_id):
    #     # desk_name - не уникален
    #
    #     return 'desk_name'
    #
    # @staticmethod
    # def get_column_name_by_column_id(column_id):
    #     # column_name - не уникален
    #
    #     return 'column_name'
    #
    # def change_desk_name(self, desk_id, new_desk_name):
    #     # изменяем имя доски в бд
    #     # True - успешно
    #     # False - доска с таким именем уже существует
    #
    #     return True
if __name__ == '__main__':
    conn = DataBaseConnection("Misha", "Elkin")
    user1 = Users(conn)
    user1.add_new_user("Sasha", "Sanya")
    # ui.add_new_user("Misha", "Elkin")

    # ui.add_new_user("Roma", "Slepchenko")

    # list = ["Misha", "Gleb", "Roma"]
    # for i in list:
    #     print(ui.get_user_id_by_login(i))


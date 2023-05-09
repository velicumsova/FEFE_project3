# сюда нужно импортировать классы бд

class UserInterface:
    def __init__(self, login, password):
        if not self.try_log_in(login, password):
            raise Exception('Пользователя с такими данными не существует! Неверен логин/пароль!')
        self.login = login
        self.password = password

    @staticmethod
    def is_login_exist(login):
        # проверяет существует ли пользователь с указанным логином
        # True - существует
        # False - нет существует
        return True

    @staticmethod
    def try_log_in(login, password):
        # проверяет cуществует ли пользователь с логин/пароль
        # True - существует
        # False - нет существует (Неверен логин/пароль)
        return True

    @staticmethod
    def add_new_user(login, password):
        if UserInterface.is_login_exist(login):
            raise Exception('Пользователя с таким логином уже существует!')
        # добавляем в бд нового пользователя
        return True

    @staticmethod
    def get_user_login_by_id(id):
        # возвращает логин пользователя по id
        return 'login'

    @staticmethod
    def get_user_id_by_login(login):
        # возвращает id пользователя по логину
        return 1

    def create_desk(self, desk_name, desk_type):
        # создаём доску в бд
        # владелец доски self.login
        # True - доска успешно создана
        # False - доска с таким именем уже существует
        return True

    def get_owned_desks(self):
        # список досок которыми владает пользователь (self.login) в формате (desk_id, desk_name)
        return [(0, 'Доска 1'), (1, 'Доска для 2112')]

    def get_public_desks(self):
        # список публичных досок досок
        return [(33, 'Доска 333'), (222, 'Доска 77')]

    def can_edit_desk(self, desk_id):
        # можем ли мы редактировать доску
        # доску может редактировать владелец или пользователь из таблицы "права на редактирования"
        return True

    @staticmethod
    def get_desk_name_by_desk_id(desk_id):
        return 'desk_name'

    @staticmethod
    def get_desk_id_by_desk_name(desk_name):
        return 1

    @staticmethod
    def get_column_name_by_column_id(column_id):
        return 'column_name'

    @staticmethod
    def get_column_id_by_column_name(column_name):
        return 1

    def change_desk_name(self, desk_id, new_desk_name):
        # изменяем имя доски в бд
        # True - успешно
        # False - доска с таким именем уже существует
        return True

    def change_column_name(self, column_id, new_column_name):
        # изменяем имя column в бд
        # True - успешно
        return True

    def del_column(self, column_id):
        # удоляем колонку из бд
        # True - успешно
        return True

    def del_desk(self, desk_id):
        # удоляем desk из бд
        # True - успешно
        return True

    def add_column_to_desk(self, desk_id, column_name):
        # добавляем новый столбец на доску
        return True

    def add_card_to_column(self, card_title, card_status, card_desk_id, card_column_id):
        # добавляем карточку в конец колонки
        return True

    def get_desk_card(self, desk_id):
        # возвращает карточки в desk в формате:
        cards = {
            'название столбца': [
                ('card_id', 'card_title', 'card_status', 'card_number_in_column'),
                ('0', 'Заголовок', '1', '0'),
            ]
        }
        return {
            'Столбец 1': [
                ('0', 'Заголовок 1', '1', '0'),
                ('1', 'Заголовок 2', '1', '1'),
                ('2', 'Заголовок 3', '2', '3'),
            ],
            'Столбец 2': [
                ('33', 'Заголовок 1', '0', '0'),
                ('43', 'Заголовок ttt', '3', '1'),
            ]
        }

    def get_full_card_info(self, card_id):
        return {
            'card_id': '11',
            'card_title': 'Title 555',
            'card_text': 'lorem text',
            'card_status': 2,
            'card_author_login': 'Sergey',
            'card_desk_id': 3,
            'card_column_id': 333,
            'card_number_in_column': 33
        }

    def change_card_title(self, card_id, new_title):
        return True

    def change_card_text(self, card_id, new_text):
        return True

    def change_card_status(self, card_id, new_status):
        return True

    def move_card(self, card_id, current_column_id, new_column_id, card_number_in_new_column):
        # перемещает карточку в новый столбец
        # нужно перезаписать card_number_in_column для всех карточек в current_column_id и new_column_id
        return True


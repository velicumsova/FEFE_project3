from tkinter import *
from tkinter import messagebox
from backend import UserInterface

def Start(window):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем приветственный текст
    label_welcome = Label(window, text="Добро пожаловать в TaskManager!", bg="#D7E3F5", fg="#043C66", font=("Arial Black", 16))

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_login = Button(window, text="Вход", command=lambda: Login(window), **button_style)
    button_register = Button(window, text="Регистрация", command=lambda: SignUp(window), **button_style)

    # задаем размеры кнопок
    button_login.config(width=15, height=1)
    button_register.config(width=15, height=1)

    # располагаем кнопки и текст
    label_welcome.place(relx=0.5, rely=0.3, anchor="center")
    button_login.place(relx=0.5, rely=0.5, anchor="center")
    button_register.place(relx=0.5, rely=0.7, anchor="center")

def Login(window):
    login=''
    password=''
    def try_to_login(login,password):
        if UserInterface.try_log_in(login, password):
            user_interface = UserInterface(login, password)
            Menu(window, user_interface)
        else:
            messagebox.showerror('Ошибка', 'Неверный логин или пароль')
            Login(window)

    # удаляем элементы окна стартового меню
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для текста
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}

    # создаем стиль для полей ввода
    entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}

    # создаем текстовые поля
    label_username = Label(window, text="Логин:", **label_style)
    label_password = Label(window, text="Пароль:", **label_style)

    # создаем поля для ввода
    entry_username = Entry(window, textvariable=login, **entry_style)
    entry_password = Entry(window, show="*", textvariable=password, **entry_style)

    # располагаем текст и поля для ввода
    label_username.place(relx=0.38, rely=0.4, anchor="e")
    entry_username.place(relx=0.4, rely=0.4, anchor="w")
    label_password.place(relx=0.38, rely=0.5, anchor="e")
    entry_password.place(relx=0.4, rely=0.5, anchor="w")

    # создаем стиль для кнопки
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_login = Button(window, text="Вход", command = lambda: try_to_login(login,password),  **button_style)
    button_back = Button(window, text="Назад", command = lambda: Start(window), **button_style)

    # задаем размеры кнопок
    button_login.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_login.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def SignUp(window):
    login = StringVar()
    password = StringVar()
    password2 = StringVar()

    def try_to_signup(login, password, password2):
        if not (UserInterface.is_login_exist(login)) and (password.get() == password2.get()):
            UserInterface.add_new_user(login.get(), password.get())
            user_interface = UserInterface(login.get(), password.get())
            Menu(window, user_interface)
        elif password.get() != password2.get():
            messagebox.showerror('Ошибка', 'Пароли не совпадают')
            SignUp(window)
        elif UserInterface.is_login_exist(login):
            messagebox.showerror('Ошибка', 'Пользователь с таким логином уже существует')
            SignUp(window)

    # удаляем элементы окна стартового меню
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для текста
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}

    # создаем стиль для полей ввода
    entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}

    # создаем текстовые поля
    label_login = Label(window, text="Логин:", **label_style)
    label_password = Label(window, text="Пароль:", **label_style)
    label_password2 = Label(window, text="Повторите пароль:", **label_style)

    # создаем поля для ввода
    entry_login = Entry(window, textvariable=login, **entry_style)
    entry_password = Entry(window, textvariable=password, show="*", **entry_style)
    entry_password2 = Entry(window, textvariable=password2, show="*", **entry_style)

    # располагаем текст и поля для ввода
    label_login.place(relx=0.42, rely=0.35, anchor="e")
    entry_login.place(relx=0.45, rely=0.35, anchor="w")
    label_password.place(relx=0.42, rely=0.45, anchor="e")
    entry_password.place(relx=0.45, rely=0.45, anchor="w")
    label_password2.place(relx=0.42, rely=0.55, anchor="e")
    entry_password2.place(relx=0.45, rely=0.55, anchor="w")

    # создаем стиль для кнопки
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_signup = Button(window, text="Зарегистрироваться", command=lambda: try_to_signup(login, password, password2), **button_style)
    button_back = Button(window, text="Назад", command=lambda: Start(window), **button_style)
    button_signup.config(width=20, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_signup.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def Menu(window, user_interface):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_mytasks = Button(window, text="Мои доски", command=lambda: TasksList(window, user_interface, user_interface.get_owned_desks()), **button_style)
    button_commontasks = Button(window, text="Общие доски", command=lambda: TasksList(window, user_interface, user_interface.get_public_desks()), **button_style)
    button_newtask = Button(window, text="Создать доску", command=lambda: NewTask(window, user_interface), **button_style)
    button_back = Button(window, text="Выйти", command = lambda: Start(window), **button_style)

    # задаем размеры кнопок
    button_mytasks.config(width=15, height=1)
    button_commontasks.config(width=15, height=1)
    button_newtask.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_mytasks.place(relx=0.5, rely=0.3, anchor="center")
    button_commontasks.place(relx=0.5, rely=0.5, anchor="center")
    button_newtask.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def TasksList(window, user_interface, tasks):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    tasks = [(0, 'Доска 1', 0, 'Myself'), (1, 'Доска для 2112', 1, 'Myself')]

    if len(tasks) > 0:
        # создаем кнопки
        button_back = Button(window, text="Назад", command=lambda: Menu(window, user_interface), **button_style)
        button_tasks = []

        # создаем контейнер для кнопок с возможностью прокрутки
        canvas = Canvas(window, bg='#D7E3F5')
        scrollbar = Scrollbar(window, orient=VERTICAL, command=canvas.yview)
        frame = Frame(canvas)
        frame.config(bg='#D7E3F5')

        # привязываем фрейм к канвасу и настраиваем прокрутку
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        for task in tasks:
            button_tasks.append(Button(frame, text=f"{task[1]}", command=lambda: Menu(window, user_interface), **button_style))
            button_tasks[task[0]].config(width=15, height=1)
            button_tasks[task[0]].pack(padx=45, pady=5)

            # обновляем геометрию фрейма и канваса
            frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        # задаем размеры кнопок
        button_back.config(width=10, height=1)

        # располагаем кнопки
        button_back.place(relx=0.15, rely=0.05, anchor="center")
        canvas.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.8, anchor='center')
        scrollbar.place(relx=0.8, rely=0.5, relheight=0.8, anchor='center', relwidth=0.05)
    else:
        # создаем кнопки
        button_create = Button(window, text="Создать доску", command=lambda: NewTask(window), **button_style)
        button_back = Button(window, text="Назад", command=lambda: Menu(window, user_interface), **button_style)

        label = Label(window, text="Здесь еще нет досок", bg="#D7E3F5", fg="#043C66", font=("Calibri", 16))

        # задаем размеры кнопок
        button_create.config(width=15, height=1)
        button_back.config(width=10, height=1)

        # располагаем текст и кнопки
        label.place(relx=0.5, rely=0.5, anchor="center")
        button_create.place(relx=0.5, rely=0.7, anchor="center")
        button_back.place(relx=0.15, rely=0.05, anchor="center")

def NewTask(window, user_interface):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    desk_name=StringVar()
    desk_type=0
    type_owned=0
    type_common=0

    # создаем стиль для текста
    label_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Calibri", 14)}

    # создаем стиль для полей ввода
    entry_style = {"bg": "white", "fg": "#043C66", "font": ("Calibri", 14), "width": 20, "bd": 0}

    # создаем стиль для радиокнопок
    radiobutton_style = {"bg": "#D7E3F5", "fg": "#043C66", "font": ("Arial Black", 11), "bd": 0, "activebackground": "#304D63"}

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем текстовые поля
    label_taskname = Label(window, text="Имя доски:", **label_style)
    label_tasktype = Label(window, text="Тип:", **label_style)

    # создаем поля для ввода
    entry_taskname = Entry(window, textvariable = desk_name, **entry_style)

    # создаем RadioButton
    desk_type = StringVar()
    rb_personal = Radiobutton(window, text="Личная", variable=desk_type, value=0, **radiobutton_style)
    rb_shared = Radiobutton(window, text="Общая", variable=desk_type, value=1, **radiobutton_style)
    
    # создаем кнопки
    button_create = Button(window, text="Создать доску", command = lambda: (user_interface.create_desk(desk_name, desk_type), messagebox.showinfo('Создание доски', 'Доска успешно создана!'), NewTask(window, user_interface)),  **button_style)
    button_back = Button(window, text="Назад", command = lambda: Menu(window, user_interface), **button_style)

    # задаем размеры кнопок
    button_create.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем текст, поле для ввода, радиокнопки и кнопки
    label_taskname.place(relx=0.38, rely=0.4, anchor="e")
    entry_taskname.place(relx=0.4, rely=0.4, anchor="w")
    label_tasktype.place(relx=0.38, rely=0.5, anchor="e")
    rb_personal.place(relx=0.4, rely=0.5, anchor="w")
    rb_shared.place(relx=0.6, rely=0.5, anchor="w")
    button_create.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def Task(window):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()


window = Tk()
window.geometry("450x550")
window.title("TaskManager")
window.config(bg="#D7E3F5")

Start(window)
window.mainloop()

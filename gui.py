from tkinter import *
from tkinter import messagebox

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
    entry_username = Entry(window, **entry_style)
    entry_password = Entry(window, show="*", **entry_style)

    # располагаем текст и поля для ввода
    label_username.place(relx=0.38, rely=0.4, anchor="e")
    entry_username.place(relx=0.4, rely=0.4, anchor="w")
    label_password.place(relx=0.38, rely=0.5, anchor="e")
    entry_password.place(relx=0.4, rely=0.5, anchor="w")

    # создаем стиль для кнопки
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    #button_login = Button(window, text="Вход", command = lambda: messagebox.showerror('Ошибка', 'Неверный логин или пароль'), **button_style)
    button_login = Button(window, text="Вход", command = lambda: Menu(window),  **button_style)
    button_back = Button(window, text="Назад", command = lambda: Start(window), **button_style)

    # задаем размеры кнопок
    button_login.config(width=15, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_login.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def SignUp(window):
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
    label_password2 = Label(window, text="Повторите пароль:", **label_style)

    # создаем поля для ввода
    entry_username = Entry(window, **entry_style)
    entry_password = Entry(window, show="*", **entry_style)
    entry_password2 = Entry(window, show="*", **entry_style)

    # располагаем текст и поля для ввода
    label_username.place(relx=0.42, rely=0.35, anchor="e")
    entry_username.place(relx=0.45, rely=0.35, anchor="w")
    label_password.place(relx=0.42, rely=0.45, anchor="e")
    entry_password.place(relx=0.45, rely=0.45, anchor="w")
    label_password2.place(relx=0.42, rely=0.55, anchor="e")
    entry_password2.place(relx=0.45, rely=0.55, anchor="w")

    # создаем стиль для кнопки
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_signup = Button(window, text="Зарегистрироваться", command = lambda: messagebox.showerror('Ошибка', 'Пользователь с таким логином уже существует'), **button_style)
    #button_signup = Button(window, text="Зарегистрироваться", command=lambda: Menu(window), **button_style)
    button_back = Button(window, text="Назад", command=lambda: Start(window), **button_style)
    button_signup.config(width=20, height=1)
    button_back.config(width=10, height=1)

    # располагаем кнопки
    button_signup.place(relx=0.5, rely=0.7, anchor="center")
    button_back.place(relx=0.15, rely=0.05, anchor="center")

def Menu(window):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

    # создаем стиль для кнопок
    button_style = {"bg": "#6DB0E3", "fg": "#043C66", "font": ("Arial Black", 12), "bd": 0, "activebackground": "#304D63"}

    # создаем кнопки
    button_mytasks = Button(window, text="Мои доски", command=lambda: MyTasks(window), **button_style)
    button_commontasks = Button(window, text="Общие доски", command=lambda: CommonTasks(window), **button_style)
    button_newtask = Button(window, text="Создать доску", command=lambda: NewTask(window), **button_style)
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

def MyTasks(window):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

def CommonTasks(window):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

def NewTask(window):
    # удаляем элементы окна
    for widget in window.winfo_children():
        widget.destroy()

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
    entry_taskname = Entry(window, **entry_style)

    # создаем RadioButton
    selected_tasktype = StringVar()
    rb_personal = Radiobutton(window, text="Личная", variable=selected_tasktype, value="Личная", **radiobutton_style)
    rb_shared = Radiobutton(window, text="Общая", variable=selected_tasktype, value="Общая", **radiobutton_style)

    # создаем кнопки
    button_create = Button(window, text="Создать доску", command = lambda: Menu(window),  **button_style)
    button_back = Button(window, text="Назад", command = lambda: Menu(window), **button_style)

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


window = Tk()
window.geometry("450x550")
window.title("TaskManager")
window.config(bg="#D7E3F5")

Start(window)

window.mainloop()

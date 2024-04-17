import tkinter as tk  # Импорт модуля tkinter для создания графического интерфейса
from tkinter import messagebox  # Импорт модуля messagebox для вывода диалоговых окон

# Функция для регистрации нового пользователя
def register_user(username, password, repeat_password):
    if password == repeat_password:
        # Здесь должна быть логика сохранения пользователя в базу данных
        messagebox.showinfo("Успех", "Пользователь успешно зарегистрирован.")
    else:
        messagebox.showerror("Ошибка", "Пароли не совпадают.")

# Функция, вызываемая при нажатии кнопки "Зарегистрироваться"
def create_account():
    username = username_entry.get()  # Получаем имя пользователя из поля ввода
    password = password_entry.get()  # Получаем пароль из поля ввода
    repeat_password = repeat_password_entry.get()  # Получаем повторный пароль из поля ввода
    register_user(username, password, repeat_password)  # Вызываем функцию регистрации пользователя

# Создание главного окна
root = tk.Tk()
root.title("Регистрация пользователя")  # Установка заголовка окна

# Создание и размещение элементов интерфейса
username_label = tk.Label(root, text="Имя пользователя:")  # Создание метки для имени пользователя
username_label.grid(row=0, column=0, sticky="w")  # Размещение метки на сетке

username_entry = tk.Entry(root)  # Создание поля ввода для имени пользователя
username_entry.grid(row=0, column=1)  # Размещение поля ввода на сетке

password_label = tk.Label(root, text="Пароль:")  # Создание метки для пароля
password_label.grid(row=1, column=0, sticky="w")  # Размещение метки на сетке

password_entry = tk.Entry(root, show="*")  # Создание поля ввода для пароля с отображением символов "*"
password_entry.grid(row=1, column=1)  # Размещение поля ввода на сетке

repeat_password_label = tk.Label(root, text="Повторите пароль:")  # Создание метки для повторного ввода пароля
repeat_password_label.grid(row=2, column=0, sticky="w")  # Размещение метки на сетке

repeat_password_entry = tk.Entry(root, show="*")  # Создание поля ввода для повторного ввода пароля с отображением символов "*"
repeat_password_entry.grid(row=2, column=1)  # Размещение поля ввода на сетке

register_button = tk.Button(root, text="Зарегистрироваться", command=create_account)  # Создание кнопки для регистрации
register_button.grid(row=3, column=0, columnspan=2)  # Размещение кнопки на сетке

# Запуск главного цикла обработки событий
root.mainloop()  # Запуск основного цикла обработки событий для работы с графическим интерфейсом

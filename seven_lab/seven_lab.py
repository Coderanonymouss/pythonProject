import tkinter as tk
from seven_lab_register import create_account

# Создание главного окна
root = tk.Tk()
root.title("Регистрация пользователя")

# Создание и размещение элементов интерфейса
username_label = tk.Label(root, text="Имя пользователя:")
username_label.grid(row=0, column=0, sticky="w")

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Пароль:")
password_label.grid(row=1, column=0, sticky="w")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

repeat_password_label = tk.Label(root, text="Повторите пароль:")
repeat_password_label.grid(row=2, column=0, sticky="w")

repeat_password_entry = tk.Entry(root, show="*")
repeat_password_entry.grid(row=2, column=1)

register_button = tk.Button(root, text="Зарегистрироваться", command=lambda: create_account(username_entry, password_entry, repeat_password_entry))
register_button.grid(row=3, column=0, columnspan=2)

# Запуск главного цикла обработки событий
root.mainloop()

from tkinter import messagebox


def register_user(username, password, repeat_password):

    if password == repeat_password:
        messagebox.showinfo("Успех", "Пользователь " + username + " успешно зарегистрирован.")
    else:
        messagebox.showerror("Ошибка", "Пароли не совпадают.")

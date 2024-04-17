from seven_lab_terminal_auth import register_user


def create_account():

    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    repeat_password = input("Повторите пароль: ")
    register_user(username, password, repeat_password)

create_account()

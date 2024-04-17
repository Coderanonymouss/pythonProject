from seven_lab_terminal_while_auth import register_user


def create_account():
    while True:
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        repeat_password = input("Повторите пароль: ")
        if register_user(username, password, repeat_password):
            print(f"Пользователь '{username}' успешно зарегистрирован.")
            break
        else:
            print("Повторите попытку.")


create_account()

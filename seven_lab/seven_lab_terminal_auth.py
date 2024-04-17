def register_user(username, password, repeat_password):

    if password == repeat_password:
        print("Пользователь", username, "успешно зарегистрирован.")
        return True
    else:
        print("Пароли не совпадают.")
        return False


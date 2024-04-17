def register_user(username, password, repeat_password):

    if password == repeat_password:
        return True
    else:
        print("Пароли не совпадают.")
        return False


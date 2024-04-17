from seven_lab_register_user import register_user


def create_account(username_entry, password_entry, repeat_password_entry):

    username = username_entry.get()
    password = password_entry.get()
    repeat_password = repeat_password_entry.get()
    register_user(username, password, repeat_password)

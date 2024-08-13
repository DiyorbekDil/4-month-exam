import hashlib
from logging_file import log_decorator
from jsonManager import user_manager


super_name = '00'
super_password = '00'


class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.password = password
        self.phone = phone
        self.active = False

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def active_user():
        all_users = user_manager.read()
        idx = 0
        while idx < len(all_users):
            if all_users[idx]['active'] is True:
                return all_users[idx]
            idx += 1


@log_decorator
def login() -> int:
    # This function belongs to auth_menu()
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    if name == super_name and password == super_password:
        return 1
    password = User.hash_password(password)
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['name'] == name and all_users[idx]['password'] == password:
            all_users[idx]['active'] = True
            user_manager.write(all_users)
            if all_users[idx]['kind'] == 'teacher':
                return 2
            elif all_users[idx]['kind'] == 'admin':
                return 3
            else:
                return 4
        idx += 1
    else:
        return 5


@log_decorator
def logout():
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['active'] is True:
            all_users[idx]['active'] = False
            user_manager.write(all_users)
        idx += 1

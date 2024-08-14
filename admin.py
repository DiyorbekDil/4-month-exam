from user import User
from logging_file import log_decorator
from jsonManager import user_manager


class Admin(User):
    def __init__(self, name, password, email):
        super().__init__(name, password, email)
        self.kind = 'admin'


@log_decorator
def add_admin():
    name = input('Enter admin name: ')
    password = User.hash_password(input('Enter admin password: '))
    email = input('Enter admin email: ')
    admin = Admin(name, password, email)
    user_manager.add(admin.__dict__)
    print('Added successfully!')
    return


@log_decorator
def delete_admin():
    name = input('Enter admin name: ')
    password = User.hash_password(input('Enter admin password: '))
    all_users = user_manager.read()
    i = 0
    while i < len(all_users):
        if all_users[i]['name'] == name and all_users[i]['password'] == password and\
                                    all_users[i]['kind'] == 'admin':
            del all_users[i]
            user_manager.write(all_users)
            print('Deleted!')
            return
        i += 1
    print('No such a admin!')


@log_decorator
def show_all_admins():
    all_users = user_manager.read()
    print('Admin name - email')
    for user in all_users:
        if user['kind'] == 'admin':
            print(f'{user["name"]} - {user["email"]}')

from user import User
from logging_file import log_decorator
from jsonManager import admin_manager


class Admin(User):
    def __init__(self, name, password, email):
        super().__init__(name, password, email)
        self.kind = 'admin'


@log_decorator
def add_admin():
    name = input('Enter admin name: ')
    password = input('Enter admin password: ')
    email = input('Enter admin email: ')
    hashed = User.hash_password(password)
    admin = Admin(name, hashed, email)
    admin_manager.add(admin.__dict__)
    print('Added successfully!')
    return


@log_decorator
def delete_admin():
    name = input('Enter admin name: ')
    password = User.hash_password(input('Enter admin password: '))
    all_admin = admin_manager.read()
    i = 0
    while i < len(all_admin):
        if all_admin[i]['name'] == name and all_admin[i]['password'] == password:
            del all_admin[i]
            admin_manager.write(all_admin)
            print('Deleted!')
            return
        i += 1


@log_decorator
def show_all_admins():
    all_admins = admin_manager.read()
    print('Admin name - email')
    for admin in all_admins:
        print(f'{admin["name"]} - {admin["email"]}')

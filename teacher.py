from user import User
from jsonManager import user_manager, group_manager
from message_config import send_mail
import threading


class Teacher(User):
    def __init__(self, name, password, email, subject, experience):
        super().__init__(name, password, email)
        self.subject = subject
        self.experience = experience
        self.kind = 'teacher'


def add_teacher():
    try:
        name = input('Enter teacher name: ')
        password = input('Teacher password: ')
        email = input('Teacher email: ')
        subject = input('Teacher subject: ')
        experience = int(input('Teacher experience: '))
        data = {'login': name, 'parol': password}
        threading.Thread(target=send_mail, args=(email, 'login vs parol', data)).start()
        password = User.hash_password(password)
        teacher = Teacher(name, password, email, subject, experience)
        user_manager.add(teacher.__dict__)
        print('Added!')
        return True
    except ValueError:
        print('Experience must be a whole number!')
        return False


def delete_teacher():
    name = input('Enter teacher name: ')
    password = User.hash_password(input('Teacher password: '))
    all_users = user_manager.read()
    i = 0
    while i < len(all_users):
        if all_users[i]['name'] == name and all_users[i]['password'] == password and\
                            all_users[i]['kind'] == 'teacher':
            del all_users[i]
            user_manager.write(all_users)
            print('Deleted!')
            return
        i += 1
    print('No such a teacher!')


def show_all_teachers():
    all_users = user_manager.read()
    print('Teacher name - email - subject - experience')
    for user in all_users:
        if user['kind'] == 'teacher':
            print(f"{user['name']} - {user['email']} - {user['subject']} - {user['experience']}")


def find_teacher(email):
    all_users = user_manager.read()
    for user in all_users:
        if user['email'] == email and user['kind'] == 'teacher':
            return user
    else:
        return False


def show_my_groups():
    teacher = User.active_user()
    all_groups = group_manager.read()
    print('Group name - start time - number of students')
    for group in all_groups:
        if group['teacher']['name'] == teacher['name']:
            print(f'{group["name"]} - {group["start"]} - {len(group["students"])}')

from user import User
from datetime import datetime as dt
from jsonManager import group_manager, lesson_manager, user_manager
from typing import Union
from logging_file import log_decorator
from decimal import Decimal


class Student(User):
    def __init__(self, name, password, email, gender):
        super().__init__(name, password, email)
        self.balance = 0
        self.gender = gender
        self.kind = 'student'


@log_decorator
def add_student():
    name = input('Enter student name: ')
    password = input('Enter student password: ')
    email = input('Enter student email: ')
    gender = input('Student gender: ')
    hashed = User.hash_password(password)
    admin = Student(name, hashed, email, gender)
    user_manager.add(admin.__dict__)
    print('Added successfully!')
    return


@log_decorator
def delete_student():
    name = input('Enter student name: ')
    password = User.hash_password(input('Enter student password: '))
    alls = user_manager.read()
    i = 0
    while i < len(alls):
        if alls[i]['name'] == name and alls[i]['password'] == password\
                     and alls[i]['kind'] == 'student':
            del alls[i]
            user_manager.write(alls)
            print('Deleted!')
            return
        i += 1
    print('No such a student!')


@log_decorator
def show_all_students():
    all_users = user_manager.read()
    print('Student name - email - balance')
    for user in all_users:
        if user['kind'] == 'student':
            print(f'{user["name"]} - {user["email"]} - {user["balance"]}')


@log_decorator
def search_by_login():
    name = input('Enter student name: ')
    all_users = user_manager.read()
    print('Student name - email - balance')
    for user in all_users:
        if user['kind'] == 'student' and user['name'] == name:
            print(f'{user["name"]} - {user["email"]} - {user["balance"]}')


@log_decorator
def find_student(name, email):
    all_users = user_manager.read()
    for user in all_users:
        if user['name'] == name and user['email'] == email and user['kind'] == 'student':
            return user
    else:
        return False


@log_decorator
def accept_payment():
    name = input('Student name: ')
    email = input('Student email: ')
    r = find_student(name, email)
    if not r:
        print('No such a student')
        return
    payment = Decimal(input('Enter amount of payment: '))
    all_users = user_manager.read()
    idx = 0
    while idx < len(all_users):
        if all_users[idx]['name'] == name and all_users[idx]['email'] == email:
            current = Decimal(all_users[idx]['balance'])
            new = current + payment
            all_users[idx]['balance'] = float(new)
            user_manager.write(all_users)
            print('Success!')
            return
        idx += 1


def show_student_groups():
    active = User.active_user()
    all_groups = group_manager.read()
    print('Group name - teacher - period - price')
    for group in all_groups:
        for student in group['students']:
            if student['email'] == active['email']:
                print(f'{group["name"]} - {group["teacher"]["name"]} - '
                      f'{group["period"]} - {group["price"]}')


def show_my_balance():
    active = User.active_user()
    print(f'{active["email"]} - {active["balance"]}')

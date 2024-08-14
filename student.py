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


# def find_student_group() -> Union[str, bool]:
#     student = User.active_user()['name']
#     groups = group_manager.read()
#     for group in groups:
#         for stud in group['students']:
#             if stud['name'] == student:
#                 return group['name']
#     else:
#         return False
#
#
# def return_student_lessons() -> Union[list, bool]:
#     result = find_student_group()
#     if result:
#         temp = []
#         lessons = lesson_manager.read()
#         for lesson in lessons:
#             if lesson["group"] == result:
#                 temp.append(lesson)
#         return temp
#     else:
#         return False
#
#
# def show_actual_student_lessons():
#     current = dt.now().strftime("%H:%M %d/%m/%Y")
#     now_datetime = dt.strptime(current, "%H:%M %d/%m/%Y")
#     temp = return_student_lessons()
#     flag = False
#     if temp:
#         for lesson in temp:
#             lesson_date = dt.strptime(lesson['start_time'], "%H:%M %d/%m/%Y")
#             if lesson_date > now_datetime:
#                 print(f'{lesson["group"]} - {lesson["subject"]} - {lesson["start_time"]}')
#                 flag = True
#         if not flag:
#             print('You do not have any actual lesson')
#     else:
#         print('You do not have any lesson')
#
#
# def return_my_ended_lessons() -> Union[list, bool]:
#     current = dt.now().strftime("%H:%M %d/%m/%Y")
#     now_datetime = dt.strptime(current, "%H:%M %d/%m/%Y")
#     temp = return_student_lessons()
#     result = []
#     if temp:
#         for lesson in temp:
#             lesson_date = dt.strptime(lesson['end_time'], "%H:%M %d/%m/%Y")
#             if lesson_date < now_datetime:
#                 result.append(lesson)
#         return result
#     else:
#         return False
#
#
# def show_my_grades():
#     result = return_my_ended_lessons()
#     active = User.active_user()['name']
#     if result:
#         print('Subject - Grade')
#         for lesson in result:
#             for student in lesson['grades']:
#                 if student["student_name"] == active:
#                     print(f'{lesson["subject"]} - {student["student_grade"]}')
#     else:
#         print('You do not have any grade yet')
#
#
# def show_my_grades_by_subject():
#     subject = input('Enter subject: ')
#     result = return_my_ended_lessons()
#     active = User.active_user()['name']
#     if result:
#         print('Subject - Grade - Teacher')
#         for lesson in result:
#             for student in lesson['grades']:
#                 if student["student_name"] == active and lesson['subject'] == subject:
#                     print(f'{lesson["subject"]} - {student["student_grade"]} - {lesson["teacher"]}')
#     else:
#         print('You do not have any grade yet')
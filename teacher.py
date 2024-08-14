from user import User
from typing import Union
from jsonManager import user_manager, group_manager
from datetime import datetime as dt


class Teacher(User):
    def __init__(self, name, password, email, subject, experience):
        super().__init__(name, password, email)
        self.subject = subject
        self.experience = experience
        self.kind = 'teacher'


def add_teacher():
    try:
        name = input('Enter teacher name: ')
        password = User.hash_password(input('Teacher password: '))
        email = input('Teacher email: ')
        subject = input('Teacher subject: ')
        experience = int(input('Teacher experience: '))
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

#
#
# def find_lessons():
#     active = User.active_user()['name']
#     lessons = lesson_manager.read()
#     temp = []
#     for lesson in lessons:
#         if lesson['teacher'] == active:
#             temp.append(lesson)
#     return temp
#
#
# def show_actual_lessons():
#     current = dt.now().strftime("%H:%M %d/%m/%Y")
#     now_datetime = dt.strptime(current, "%H:%M %d/%m/%Y")
#     temp = find_lessons()
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
# def show_ended_lessons():
#     current = dt.now().strftime("%H:%M %d/%m/%Y")
#     now_datetime = dt.strptime(current, "%H:%M %d/%m/%Y")
#     temp = find_lessons()
#     flag = False
#     if temp:
#         for lesson in temp:
#             lesson_date = dt.strptime(lesson['end_time'], "%H:%M %d/%m/%Y")
#             if lesson_date < now_datetime:
#                 print(f'{lesson["group"]} - {lesson["subject"]} - {lesson["start_time"]}')
#                 flag = True
#         if not flag:
#             print('You do not have any ended lesson')
#     else:
#         print('You do not have any lesson')
#
#
# def return_students(group) -> Union[list, bool]:
#     groups = group_manager.read()
#     for grou in groups:
#         if grou['name'] == group:
#             return grou['students']
#     return False
#
#
# def grade_students():
#     group = input('Enter group name: ')
#     start_time = input('Enter lesson\'s start time: ')
#     students = return_students(group)
#     lessons = lesson_manager.read()
#     if students:
#         idx = 0
#         while idx < len(lessons):
#             if lessons[idx]['group'] == group and lessons[idx]['start_time'] == start_time:
#                 for student in students:
#                     grade = input(f'Grade {student["name"]}>>> ')
#                     pair = {"student_name": student["name"],
#                             "student_grade": grade}
#                     lessons[idx]['grades'].append(pair)
#             idx += 1
#         lesson_manager.write(lessons)
#         print('Added!')
#     else:
#         print('No such a group or lesson!')
from random import randint
from logging_file import log_decorator
from jsonManager import group_manager, user_manager
from decimal import Decimal as D
from teacher import find_teacher


class Group:
    def __init__(self, name, start, end, period, price, teacher):
        self.name = name
        self.start = start
        self.end = end
        self.period = period
        self.price = price
        self.teacher = teacher
        self.iden_num = randint(0, 1_000_000)
        self.students = []


@log_decorator
def create_group():
    try:
        name = input('Enter group name: ')
        start = input('Start time (dd/mm/yyyy): ')
        end = input('End time (dd/mm/yyyy): ')
        period = int(input('Period (month): '))
        price = int(input('Price per month: '))
        teacher_mail = input('Teacher email: ')
        teacher = find_teacher(teacher_mail)
        if not teacher:
            print('No such a teacher!')
            return
        group = Group(name, start, end, period, price, teacher)
        group_manager.add(group.__dict__)
        print('Successfully created')
        return
    except ValueError:
        print('You entered something wrong!')
        return


@log_decorator
def add_student_group():
    try:
        group = int(input('Enter identity number: '))
        all_groups = group_manager.read()
        i = 0
        while i < len(all_groups):
            if all_groups[i]['iden_num'] == group:
                name = input('Student name: ')
                email = input('Student email: ')
                all_users = user_manager.read()
                idx = 0
                while idx < len(all_users):
                    if all_users[idx]['name'] == name and all_users[idx]['email'] == email and\
                                                    all_users[idx]['kind'] == 'student':
                        student = {'name': name, 'email': email}
                        all_groups[i]['students'].append(student)
                        group_manager.write(all_groups)
                        print('Added')
                        return
                    idx += 1
                else:
                    print('No such a student')
                    return
            i += 1
        else:
            print('No such a group')
    except ValueError:
        print('Identity number must be a number!')
        return add_student_group()


@log_decorator
def del_group():
    try:
        group = int(input('Enter identity number: '))
        all_groups = group_manager.read()
        i = 0
        while i < len(all_groups):
            if all_groups[i]['iden_num'] == group:
                del all_groups[i]
                group_manager.write(all_groups)
                print('Deleted')
                return
            i += 1
        else:
            print('No such a group')
    except ValueError:
        print('Identity number must be a number!')
        return del_group()


@log_decorator
def show_groups():
    all_groups = group_manager.read()
    print('Name - Identity number - Number of students')
    for group in all_groups:
        print(f'{group["name"]} - {group["iden_num"]} - {len(group["students"])}')


@log_decorator
def find_group(name):
    all_groups = group_manager.read()
    for group in all_groups:
        if group['name'] == name:
            return True
    else:
        return False

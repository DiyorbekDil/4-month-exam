from random import randint
from logging_file import log_decorator
from jsonManager import group_manager, user_manager


class Group:
    def __init__(self, name):
        self.name = name
        self.iden_num = randint(0, 1_000_000)
        self.students = []


@log_decorator
def create_group():
    name = input('Enter group name: ')
    group = Group(name)
    group_manager.add(group.__dict__)
    print('Successfully created')


@log_decorator
def add_student_group():
    group = input('Enter group name: ')
    all_groups = group_manager.read()
    i = 0
    while i < len(all_groups):
        if all_groups[i]['name'] == group:
            name = input('Student name: ')
            try:
                phone = int(input("Phone: "))
            except ValueError:
                print('Phone number must be a whole number!')
                return add_student_group()
            all_users = user_manager.read()
            idx = 0
            while idx < len(all_users):
                if all_users[idx]['name'] == name and all_users[idx]['phone'] == phone and\
                                                all_users[idx]['kind'] == 'student':
                    student = {'name': name, 'phone': phone}
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


@log_decorator
def del_group():
    group = input('Enter group name: ')
    all_groups = group_manager.read()
    i = 0
    while i < len(all_groups):
        if all_groups[i]['name'] == group:
            del all_groups[i]
            group_manager.write(all_groups)
            print('Deleted')
            return
        i += 1
    else:
        print('No such a group')


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

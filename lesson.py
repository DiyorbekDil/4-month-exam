from jsonManager import lesson_manager
from teacher import find_teacher
from group import find_group
from logging_file import log_decorator


class Lesson:
    def __init__(self, group, start_time, end_time):
        self.group = group
        self.start_time = start_time
        self.end_time = end_time
        self.grades = []


@log_decorator
def add_lesson():
    group = input('Enter group name: ')
    start_time = input('Start (hour:min dd/mm/yyyy): ')
    end_time = input('End (hour:min dd/mm/yyyy): ')
    if find_group(group):
        lesson = Lesson(group, start_time, end_time)
        lesson_manager.add(lesson.__dict__)
        print('Added')
        return
    else:
        print('You have entered something wrong')
        return


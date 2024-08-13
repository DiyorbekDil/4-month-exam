# from fileManager import lesson_manager
# from subject import find_subject
# from teacher import find_teacher
# from group import find_group
#
#
# class Lesson:
#     def __init__(self, group, subject, teacher, start_time, end_time):
#         self.group = group
#         self.subject = subject
#         self.teacher = teacher
#         self.start_time = start_time
#         self.end_time = end_time
#         self.grades = []
#
#
# def add_lesson():
#     # This function belongs to admin_menu()
#     group = input('Enter group name: ')
#     subject = input('Subject name: ')
#     teacher = input('Teacher name: ')
#     start_time = input('Start (hour:min dd/mm/yyyy): ')
#     end_time = input('End (hour:min dd/mm/yyyy): ')
#     if find_group(group) and find_subject(subject) and find_teacher(teacher):
#         lesson = Lesson(group, subject, teacher, start_time, end_time)
#         lesson_manager.add(lesson.__dict__)
#         print('Added')
#         return
#     else:
#         print('You have entered something wrong')
#         return
#
#
# def show_lessons():
#     # This function belongs to admin_menu()
#     lessons = lesson_manager.read()
#     print('Group - subject - teacher - start time - end time')
#     for lesson in lessons:
#         print(f'{lesson["group"]} - {lesson["subject"]} - {lesson["teacher"]} - {lesson["start_time"]}'
#               f' - {lesson["end_time"]}')

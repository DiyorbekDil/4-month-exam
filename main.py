from logging_file import log_decorator


@log_decorator
def auth_menu():
    text = """
    1.Log-in
    2.Exit
    """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        return
    else:
        print('Unexpected character!')
        return auth_menu()


@log_decorator
def super_admin_menu():
    text = """
        1.Manage teachers
        2.Manage admins
        3.Send email
        4.Log-out
        """
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        return manage_teachers()
    elif user_input == '2':
        return manage_admins()
    elif user_input == '2':
        return send_email()
    elif user_input == '2':
        return auth_menu()
    else:
        print('Unexpected character!')
        return super_admin_menu()


@log_decorator
def manage_teachers():
    # This function belongs to super_admin_menu()
    text = '''
        1.Create teacher
        2.Delete teacher
        3.Show all teachers
        4.Back super admin menu
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        return super_admin_menu()
    else:
        print('Unexpected character!')
        return manage_teachers()


@log_decorator
def manage_admins():
    # This function belongs to super_admin_menu()
    text = '''
        1.Create admin
        2.Delete admin
        3.Show all admins
        4.Back super admin menu
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        return super_admin_menu()
    else:
        print('Unexpected character!')
        return manage_admins()


@log_decorator
def send_email():
    # This function belongs to super_admin_menu()
    text = '''
        1.Send all a email
        2.Send boys a email
        3.Send girls a email
        4.Back to super admin menu
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        return super_admin_menu()
    else:
        print('Unexpected character!')
        return send_email()


@log_decorator
def admin_menu():
    text = '''
    1.Group (CRUD)
    2.Student (CRUD)
    3.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        return manage_groups()
    elif user_input == '2':
        return manage_students()
    elif user_input == '3':
        pass
    else:
        print('Unexpected character!')
        return admin_menu()


@log_decorator
def manage_groups():
    # This function belongs to admin_menu()
    text = '''
        1.Create group
        2.Delete group
        3.Show all groups
        4.Add a student to a group
        5.Back
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        return admin_menu()
    else:
        print('Unexpected character!')
        return manage_groups()


@log_decorator
def manage_students():
    # This function belongs to admin_menu()
    text = '''
        1.Create student
        2.Delete student
        3.Search student by log-in
        4.Show all students
        5.Accept payment from a student
        6.Back
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        return admin_menu()
    else:
        print('Unexpected character!')
        return manage_students()


@log_decorator
def teacher_menu():
    text = '''
    1.Show my groups
    2.Start lesson
    3.Show my ended lessons
    4.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        return start_lesson()
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    else:
        print('Unexpected character!')
        return teacher_menu()


@log_decorator
def start_lesson():
    # This function belongs to teacher_menu()
    text = '''
        1.Grade students
        2.End lesson
        3.Back teacher menu
        '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        return teacher_menu()
    else:
        print('Unexpected character!')
        return start_lesson()


@log_decorator
def student_menu():
    text = '''
    1.Show my groups
    2.Show my balance
    3.Show my grades by group
    4.Log-out
    '''
    print(text)

    user_input = input('Enter a number: ')
    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    else:
        print('Unexpected character!')
        return student_menu()


auth_menu()

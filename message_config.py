from datetime import datetime as dt
from jsonManager import user_manager, message_manager
from user import User
import smtplib


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'isoqovdiyorbek742@gmail.com'
smtp_password = 'zguu kqct xtzn jnkb'


class Message:
    def __init__(self, subject, text):
        self.subject = subject
        self.text = text
        self.to_who = None
        self.created_at = dt.now().strftime("%H:%M %d-%m-%Y")


def send_users_message(to_who):
    subject = input('Enter message subject: ')
    text = input('Enter message text: ')
    message = Message(subject, text)
    message.to_who = to_who
    message_manager.add(message.__dict__)
    all_users = user_manager.read()
    for user in all_users:
        if user['kind'] == 'student':
            if to_who == 'all':
                send_mail(user['email'], subject, text)
            elif to_who == 'boys':
                if user['gender'] == 'male':
                    send_mail(user['email'], subject, text)
            elif to_who == 'girls':
                if user['gender'] == 'female':
                    send_mail(user['email'], subject, text)
    print('Sent successfully!')
    return


def send_mail(to_user, subject, message):
    email = f"Subject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
        return True
    except smtplib.SMTPException as e:
        return False, e

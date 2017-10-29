from flask_mail import Mail, Message

from flask import current_app

app = current_app._get_current_object()
mail = Mail(app)


def send_email(subject):
    from flask_mail import Mail, Message
    from flask import current_app
    app = current_app._get_current_object()
    mail = Mail(app)
    msg = Message(subject,sender='tjulyw2015@163.com', recipients=['tjulyw2015@163.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    with app.app_context():
        mail.send(msg)


def send_email2(subject):
    from flask_mail import Mail, Message
    from flask import current_app
    app = current_app._get_current_object()
    mail = Mail(app)
    msg = Message(subject,sender='327801253@qq.com', recipients=['tjulyw2015@163.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    with app.app_context():
        mail.send(msg)

def send_email3(subject):
    mail = Mail(app)
    msg = Message(subject,sender='327801253@qq.com', recipients=['tjulyw2015@163.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    with app.app_context():
        mail.send(msg)
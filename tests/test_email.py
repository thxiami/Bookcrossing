from flask_mail import Mail, Message

from flask import current_app

app = current_app._get_current_object()
mail = Mail(app)


def send_email(subject):
    from flask_mail import Mail, Message
    mail = Mail(app)
    msg = Message(subject,sender='tjulyw2015@163.com', recipients=['tjulyw2015@163.com'])
    msg.body = 'text body'
    msg.html = '<b>HTML</b> body'
    with app.app_context():
        mail.send(msg)
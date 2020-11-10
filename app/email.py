from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, body):
    msg = Message(subject, sender='aras@condatus.com', recipients=['arasged@gmail.com'])
    msg.body = body
    msg.html = 'This is <b>HTML</b>'
    thr = Thread(target=send_async_email, args=[app,msg])
    thr.start()
    return thr

import smtplib
from email.message import EmailMessage

def send_email(message, sender, password, receiver, smtp_server):
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = 'Testing Python SMTP'
    msg['From'] = sender
    msg['To'] = receiver

    s = smtplib.SMTP(smtp_server)
    s.login('testpython123', password)
    s.send_message(msg)
    s.quit()
    print('An email has been sent!')

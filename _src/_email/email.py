import smtplib
from email.mime.text import MIMEText

# can do kwargs['subject'] provided **kwargs here and subject=settings.subject outside
# dont need to use **kwargs here... structure is defined and strict

def build_email(text, subject, sender, recipient):
    message = MIMEText(text, 'html')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient
    return message

def send_email(message, gmail_user, gmail_password, sender, recipient):
    '''one time connection, not expecting pipe to hold as long as a week'''
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sender, recipient, message.as_string())
    server.close()
    print('Email sent!')


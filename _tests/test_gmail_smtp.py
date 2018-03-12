import smtplib
from _settings import settings

def test_gmail_login():
    '''only testing if you can connect to gmail smtp server'''
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(settings.gmail_user, settings.gmail_password)
    server.close()
    assert True

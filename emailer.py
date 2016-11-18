import smtplib

from config.config import config

config = config['email']

FROM = config['from-login']
PASSWORD = config['from-password']
TO = config['to-email-address']
SUBJECT = config['default-subject']


def send_email(message):
    if config['disable-sending']:
        return

    try:
        email_content = """From: %s\nTo: %s\nSubject: %s\n\n%s 
        """ % (FROM, TO, SUBJECT, message)

        server = smtplib.SMTP_SSL("poczta.o2.pl", 465)
        print 'lenrok-bot'
        server.login(FROM, PASSWORD)
        server.sendmail(FROM, TO, email_content)
        server.close()
        print ('Successfuly send email to [{}] with content [{}]'.format(TO, message))
    except Exception as e:
        print ('Unable to send emial message={}'.format(e))

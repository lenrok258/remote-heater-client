import smtplib
import json

from logger import Logger 

logger = Logger(__name__)

FROM = 'lenrok.bot@o2.pl'
TO= 'kornelzemla@gmail.com'

def send_email(subject, message):
    try:
        email_content = """From: %s\nTo: %s\nSubject: %s\n\n%s 
        """ % (FROM, TO, subject, message)

        server = smtplib.SMTP_SSL("poczta.o2.pl", 465)
        print 'lenrok-bot'
        server.login(FROM, 'ZAQwsx123')
        server.sendmail(FROM, TO, email_content)
        server.close()
        logger.info('Successfuly send email to [{}] with content [{}]'.format(TO, message))
    except Exception as e:
        logger.error('Unable to send emial message={}'.format(e))


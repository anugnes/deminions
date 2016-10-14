import smtplib
import base64
from email.mime.text import MIMEText
from datetime import datetime

__author__ = 'anugnes'


# def send_email(status):
#     """formats and sends the email"""
#
#     from_addr = "nugnes.alberto@gmail.com"
#     to_addr = "eclipsehv@gmail.com"
#
#     email_time = '{:%d-%m-%Y %H:%M:%S}'.format(datetime.now())
#     email_body = "It's %s and cmile is %s" % (email_time, status)
#     email_body += "\n\n"
#
#     msg = MIMEText(email_body)
#     msg['Subject'] = 'Cmile status report: {:%d-%m-%Y %H:%M:%S}'.format(datetime.now())
#     msg['From'] = from_addr
#     msg['To'] = from_addr
#
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_addr, "N4r4st1l3goo")
#
#     text = msg.as_string()
#     server.sendmail(from_addr, to_addr, text)
#     server.quit()


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string())}

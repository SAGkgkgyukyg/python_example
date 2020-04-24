from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

sender = ''
passwd = ''



def send_email(Subject, Message, Receivers):
    emails = [elem.strip().split(',') for elem in Receivers]
    msg = MIMEMultipart()
    msg['Subject'] = Subject
    msg['From'] = sender
    msg['To'] = ','.join(Receivers)

    msg.preamble = 'Multipart massage.\n'
    part = MIMEText(Message)
    msg.attach(part)

    smtp = smtplib.SMTP("smtp.gmail.com:587")
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, passwd)
    smtp.sendmail(msg['From'], emails, msg.as_string())
    print('Send mails to', msg['To'])


# function test
send_email("Message Subject", "Hello World!", ['example@gmail.com'])

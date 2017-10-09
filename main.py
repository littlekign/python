# coding=UTF-8

import csv
import re

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os


gmail_user = "xxx"
gmail_pwd = "xxx"

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text, 'html'))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   mailServer.close()



with open("path/to/file.csv", "r") as creader:
    csvReader = csv.reader(creader, delimiter=',')
    for row in csvReader:
        print row[1]
        mail(row[1], "Title", "Message", "path/to/file.pdf")
        
        
#Original code to send emails: http://kutuma.blogspot.pt/2007/08/sending-emails-via-gmail-with-python.html

#I've used this script to send batch emails to users from a CSV list

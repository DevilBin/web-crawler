#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

def send_email(SMTP_host, from_addr, password, to_addrs, subject, content):
    email_client = SMTP(SMTP_host)
    email_client.login(from_addr, password)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')#subject
    msg['From'] = '<{0}>'.format(from_addr)
    msg['To'] = '{0}'.format(to_addrs)
    email_client.sendmail(from_addr, to_addrs, msg.as_string())

    email_client.quit()

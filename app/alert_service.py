import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
import smtplib
import configparser
import logging
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import warnings
from email.mime.text import MIMEText
from io import StringIO 
from pathlib import Path
warnings.filterwarnings("ignore")

BASE_DIR = Path(__file__).parent

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

API_KEY = "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"

class Alerter:

    def __init__(self):
        self.email_config = configparser.ConfigParser()

    def send_emails(self, html):
        #print("hi")
        self.email_config.read(
            '{}/config_files/email_config.ini'.format(BASE_DIR))
        email_list = self.email_config.get('LIST', 'emails').strip().split(',')
        print(email_list)
        COMMASPACE = ', '

        message = Mail(
            from_email='watttdean@gmail.com',
            to_emails=email_list,
            subject='Prototype - Training',
            html_content=f'<strong>{html}</strong>')
        try:
            sg = SendGridAPIClient(API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            response = e.message
            print(e.message)

    # def main(self):
    #     print("Sending E-Mails... ")
    #     print('')

    #     string = "Test Email" 
    #     self.send_emails(string)

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import path


html = Template(path('index.html').read_text())
email = EmailMessage()
email['from'] = '# your name here'
email['to'] = '# Delivery email address here'
email['subject'] = '# Subject of email here'

email.set_content('# body of the email here')

email.set_content(html.substitute({'name': 'Aniket'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port= 587 ) as smtp:
    smtp.ehlo()
    smtp.starttls()  # for secure encrypted connection
    smtp.login('#your email address', 'password ')
    smtp.send_message(email)
    print('Email Sent ')
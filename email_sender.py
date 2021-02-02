import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template



html = Template(Path(#'pathtothehtmfile'#).read_text())
email = EmailMessage()
email['from'] = #name#
email['to'] = #email to#
email['subject'] = #message#


email.set_content(html.substitute({'name': <'insertname'>}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<your email adress>', '<emailpassword>')
    smtp.send_message(email)
    print('SENT!')

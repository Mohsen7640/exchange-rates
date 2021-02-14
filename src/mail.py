import smtplib
from email.mime.text import MIMEText
from src.local_config import sender, receiver


def send_smtp_mail(subject: str, body: str):
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['From'] = sender['email']
    msg['To'] = receiver['email']

    try:
        # Send mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(
                sender['email'], sender['password']
            )
            server.sendmail(
                msg['From'], msg['To'], msg.as_string()
            )
        print('successfully sent the mail')
    except Exception:
        print('failed to send mail')

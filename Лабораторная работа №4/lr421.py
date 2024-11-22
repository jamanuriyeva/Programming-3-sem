import smtplib
from email.mime.text import MIMEText
from email.header import Header


SMTP_SERVER = 'smtp.mail.ru'
SMTP_PORT = 465
SENDER_EMAIL = 'mati.nurieva@mail.ru'
RECIPIENT_EMAIL = 'mati.nurievaog@gmail.com'
PASSWORD = '0n7tpzjihyshbaFn3RJ2'

#сообщения
msg = MIMEText('Джекпот апнул хостел хоуми я мой солд аут несет не зло главное чтоб была семья вера в чудо не мое.', 'plain', 'utf-8')
msg['Subject'] = Header('важно', 'utf-8')  # Заголовок письма
msg['From'] = SENDER_EMAIL
msg['To'] = RECIPIENT_EMAIL

#отправка письма
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
    server.login(SENDER_EMAIL, PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    print("Письмо успешно отправлено!")
import smtplib
from email.message import EmailMessage
import os

class Email():  
    
    def envia_email(email_cadastrado):
        # configurar email, senha
        EMAIL_ADDRESS = os.environ['EMAIL']
        EMAIL_PASSWORD = os.environ['SENHA']

        msg = EmailMessage()
        msg['Subject'] = 'Web Service Hub ©'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'mateus.brandeburski92@gmail.com', email_cadastrado
        msg.set_content('Sua conta no Web Service Hub foi criada com sucesso!')


        # envia o email
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)





# from validate_email import validate_email
# from email.message import EmailMessage
# import os
# import smtplib

# class Email():  
    
#     def envia_email(email_cadastrado, mensagem='Sua conta no Web Service Hub © foi criada com sucesso!'):
#         # configurar email, senha
#         EMAIL_ADDRESS = os.environ['EMAIL']
#         EMAIL_PASSWORD = os.environ['SENHA']
        

#         msg = EmailMessage()
#         msg['Subject'] = 'Web Service Hub ©'
#         msg['From'] = EMAIL_ADDRESS
#         msg['To'] = 'mateus.brandeburski92@gmail.com', email_cadastrado
#         msg.set_content(mensagem)


#         # envia o email
#         with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
#             smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#             smtp.send_message(msg)
            
#     def valida_email(email_cadastro):
#         is_valid = validate_email(email_cadastro)
        

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os

# Configurar email, senha
class Email:

    def envia_email(email_cadastrado, senha):
        
        EMAIL_ADDRESS = os.environ['EMAIL']
        EMAIL_PASSWORD = os.environ['SENHA']

        # Cria uma mensagem multipart (para enviar o corpo do email com formatação HTML)
        msg = MIMEMultipart()

        # Configura os campos de endereço de email e assunto
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email_cadastrado
        msg['Subject'] = 'Web Service Hub ©'

        # Adiciona o corpo do email em formato HTML
        corpo_email = f"""
        <html>
        <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@500&display=swap');
        </style>
        </head>
        <body>
            <p style="font-family: Arial, sans-serif; font-size: 28px;">
            Sua senha acaba de ser recuperada no Web Service Hub ©!
            <br>
            </p> 
            <div style=""   
            <p style="font-size: 30px; font-family: 'Roboto Mono', monospace;"><strong>Sua senha é: {senha} </strong></p>
            </div>
            </p>
            <p style="font-family: 'Roboto Mono', monospace; font-size: 50px; background-color: black; color: white;  text-align: center;">Web Service Hub © </p>
        </body>
        </html>
        """
        # <img src="cid:imagem_hub">   PARA COLOCAR IMAGEM
        msg.attach(MIMEText(corpo_email, 'html'))

        # # Carrega a imagem a ser anexada
        # with open("static/image/email_logo.jpg", "rb") as arquivo_imagem:
        #     imagem = MIMEImage(arquivo_imagem.read())
        #     imagem.add_header('Content-ID', '<imagem_hub>')
        #     msg.attach(imagem)

        # Envia o email
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.sendmail(EMAIL_ADDRESS, email_cadastrado, msg.as_string())




Email.envia_email('mateus.brandeburski92@gmail.com', senha="D3v3lo034r@")
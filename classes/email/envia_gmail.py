from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import os

css_personalizado = """
           <style>
            body {
            font-family: 'Open Sans', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #333;
            }

            h1, h2, h3, h4, h5, h6 {
            font-family: 'Open Sans', sans-serif;
            font-weight: 600;
            }

            .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            }

            .btn-primary {
            background-color: #007bff;
            border-color: #007bff;
            font-weight: 600;
            }

            .btn-primary:hover {
            background-color: #0069d9;
            border-color: #0062cc;
            }

            .btn-primary:focus {
            box-shadow: none;
            }

            .card {
            border-radius: 5px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            }

            .card-header {
            background-color: #007bff;
            color: #fff;
            padding: 15px;
            border-radius: 5px 5px 0 0;
            }

            .card-body {
            padding: 30px;
            }

            .mt-4 {
            margin-top: 40px;
            }

            .mb-4 {
            margin-bottom: 40px;
            }
        </style>"""
        
# Configurar email, senha
class Email:

    def envia_email(email_cadastrado, nome_usuario, css_personalizado=css_personalizado):
        
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
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redefinir Senha</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
        {css_personalizado}
        </head>
        <body>
        <div class="container">
            <div class="row">
            <div class="col-md-8 offset-md-2">
                   
                <div class="card mt-4">
                <div class="card-header">
                    <h4>Redefinir Senha</h4>
                </div>
                <div class="card-body">
                    <p>Olá, {nome_usuario}!</p>
                    <p>Recebemos uma solicitação para redefinir a senha da sua conta.</p>
                    <p>Para redefinir sua senha, clique no link abaixo:</p>
                    

                    <p>Se você não solicitou a redefinição da senha, não é necessário realizar nenhuma ação.</p>
                    <p>Caso tenha alguma dúvida ou necessite de ajuda, entre em contato com nossa equipe de suporte.</p>
                    <p>Obrigado, <br>Equipe de Suporte</p>
                </div>
                </div>

            </div>
            </div>
        </div>
        </body>
        </html>"""

        
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


# Email.envia_email('mateus.brandeburski92@gmail.com', 'Mateus')
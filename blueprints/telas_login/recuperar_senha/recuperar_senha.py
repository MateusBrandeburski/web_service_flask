from flask import Blueprint, render_template, request, redirect, url_for, flash
from classes.database.database import Usuarios, db
from classes.email.envia_gmail import Email
import secrets


recupera = Blueprint('recupera', __name__, template_folder='template')


# renderiza a página que recupera a senha.
@recupera.route('/recuperar-senha')
def index():  
    return render_template('login/recuperar_senha/recuperar_senha.html')


# precessa a recuperação de senha.
@recupera.route('/processa-recuperacao-senha', methods=['POST'])
def get_email():
    
    email = request.form['email']
    user = db.session.query(Usuarios).filter_by(email=email).first()
    
    if user:
           
        # envia um email com um link para criação de novo hash de Senha.
        token = secrets.token_hex(10)
        Email.envia_email(email_cadastrado=request.form['email'], token=token, nome_usuario=user.nickname)
        
        return render_template('login/recuperar_senha/recuperar_senha.html', recuperar_senha=True)
        
    else:
        return render_template('login/recuperar_senha/recuperar_senha.html', recuperar_senha=False)
    
    

@recupera.route('/nova-senha/<token>', methods=['GET', 'POST'])
def nova_senha(token):
    
    
    return render_template('login/recuperar_senha/recuperar_senha.html')
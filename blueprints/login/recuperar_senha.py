from flask import Blueprint, render_template, request, redirect, url_for, flash
from classes.database.database import Usuarios, db
from classes.envia_gmail import Email


recupera = Blueprint('recupera', __name__, template_folder='template')


# renderiza a página que recupera a senha.
@recupera.route('/recuperar-senha')
def index():  
    return render_template('login/recuperar_senha.html')


# precessa a recuperação de senha.
@recupera.route('/processa-recuperacao-senha', methods=['POST'])
def get_email():
    
    email = request.form['email']
    user = db.session.query(Usuarios).filter_by(email=email).first()
    if user:
        Email.envia_email(request.form['email'], mensagem=('Seu usuário é: {}.\nSua senha é: {}'.format(user.nickname, user.senha)))
        return render_template('login/recuperar_senha.html', recuperar_senha=True)
        
    else:
        return render_template('login/recuperar_senha.html', recuperar_senha=False)
    
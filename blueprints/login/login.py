from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from classes.database.database import Usuarios

login = Blueprint('login', __name__, template_folder='templates')

# Renderiza
@login.route('/', methods=['GET'])
def index():
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return render_template('login/login.html')  
     
    return render_template('web_scraping/web_scraping.html')
 
# Processa o login
@login.route('/autenticar', methods=['POST'])
def autenticar():
    
    nickname = request.form['usuario']
    senha = request.form['senha']

    usuario = Usuarios.query.filter_by(nickname=nickname, senha=senha).first()

    if usuario is not None:
        session['usuario_logado'] = usuario.nickname
        session['eh_admin'] = usuario.eh_admin # adiciona se o usuário é adm ou não na sessão 
        return redirect(url_for('web_scraping.index'))

    flash('Username ou password inválidos')
    return redirect(url_for('login.index'))
   
  
@login.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('login.index'))
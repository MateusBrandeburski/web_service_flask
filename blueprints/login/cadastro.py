from flask import Blueprint, render_template, request, redirect, url_for, flash
from classes.database.database import Usuarios, db
from classes.envia_gmail import Email
from validate_email import validate_email
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
cadastro = Blueprint('cadastro', __name__, template_folder='template')


@cadastro.route('/cadastro')
def register():
    
    return render_template ('login/cadastro.html')


@cadastro.route('/processa-cadastro', methods=['GET' ,'POST'])
def processa_cadastro():

    if request.method == 'POST':     
        # Verifica se todos os campus foram preenchidos
        try:
            # captura os dados do input
            nome = request.form['nickname']
            senha = request.form['senha']
            email = request.form['email']
            
            # verifica se o email é valido, se for, ele faz o trampo todo.
            is_valid = validate_email(email)
            if is_valid:
                hashed_password = bcrypt.generate_password_hash(senha).decode('utf-8')
                novo_usuario = Usuarios(nickname=nome, senha=hashed_password, email=email)
          
                db.session.add(novo_usuario)
                db.session.commit()
                
            else:
                flash('Email inválido...')
             
        except:
            flash('Todos os campos precissam ser preenchidos.')
            return redirect(url_for('cadastro.processa_cadastro'))
        
        
        # envia um email para o usuário que cadastrou
        try:
            # verifica se o email é válido para enviar confirmação
            is_valid = validate_email(request.form['email'])
            if is_valid:
                Email.envia_email(request.form['email']) 
                return redirect(url_for('login.index'))   
        except:
            return redirect(url_for('login.index')) 
        
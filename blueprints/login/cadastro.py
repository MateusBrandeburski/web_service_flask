from flask import Blueprint, render_template, request, redirect, url_for, flash
from classes.database.database import Usuarios, db
from classes.envia_gmail import Email
from validate_email import validate_email


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
            usuario = Usuarios(request.form['nickname'], request.form['senha'], request.form['email'])
            # verifica se o email é válido para criar conta
            is_valid = validate_email(request.form['email'])
            if is_valid:
                db.session.add(usuario)
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
        
    return render_template ('login/cadastro.html')
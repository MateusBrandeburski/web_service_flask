from flask import Blueprint, render_template, request, redirect, url_for, flash
from classes.database.database import Usuarios, db
from classes.envia_gmail import Email


cadastro = Blueprint('cadastro', __name__, template_folder='template')


@cadastro.route('/cadastro')
def register():
    
    return render_template ('login/cadastro.html')


@cadastro.route('/processa-cadastro', methods=['GET' ,'POST'])
def processa_cadastro():

    if request.method == 'POST':
        
        # Verifica se todos os campus foram preenchidos
        try:
            usuario = Usuarios(request.form['nickname'], request.form['senha'], request.form['email'])
                
            db.session.add(usuario)
            db.session.commit()
        except:
            flash('Todos os campus precissam ser preenchidos.')
            return redirect(url_for('cadastro.processa_cadastro'))
        
        # envia um email para o usuário que cadastrou
        try:
            Email.envia_email(request.form['email'])
        except:
            pass    
        return redirect(url_for('login.index'))
        
    return render_template ('login/cadastro.html')
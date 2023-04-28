from flask import Blueprint, render_template, request, redirect, url_for, flash
from classes.database.database import Usuarios, db
from classes.envia_gmail import Email
from validate_email import validate_email
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

cadastro = Blueprint('cadastro', __name__, template_folder='template')

# rotae que renderiza a página do cadastro.
@cadastro.route('/cadastro')
def register():
    return render_template ('login/cadastro.html')


# rota que processa o cadastro.
@cadastro.route('/processa-cadastro', methods=['POST'])
def processa_cadastro():
    
    bcrypt = Bcrypt()
    
    if request.method == 'POST':     
        
        # Verifica se todos os campus foram preenchidos
        try:
   
            # captura os dados do input
            nome = request.form['nickname']
            senha = request.form['senha']
            confirma_senha = request.form['confirma_senha']
            email = request.form['email']
            
            # verifica a confirmção de senha
            if confirma_senha == senha:
            
                # transforma a senha em hash
                hashed_password = bcrypt.generate_password_hash(senha).decode('utf-8')
                
                # verifica se o email é valido. É uma verificação superficial (verifica se tem @ no email)
                is_valid = validate_email(email)
                if is_valid:
                    
                    # cria a query e commita no DB
                    novo_usuario = Usuarios(nickname=nome, senha=hashed_password, email=email)  
                    db.session.add(novo_usuario)
                    db.session.commit() 
                    
                    return redirect(url_for('login.index'))
                
                else:
                    flash('Email inválido.')
                    return redirect(url_for('cadastro.register'))
            
            else:
                flash('As senhas precisam ser idênticas.')
                return redirect(url_for('cadastro.register'))

        # esse erro acontece quando já existem um usuário o email cadastrado no DB
        except IntegrityError:
            flash('Usuário ou Email já cadastrados.')
            return redirect(url_for('cadastro.register'))
        
        # essa erro acontece quando nenhum campo é preenchido
        except ValueError:
            flash('Todos os campos precissam ser preenchidos.')
            return redirect(url_for('cadastro.register'))
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from classes.database.database import db, Endereco, Usuarios


crud = Blueprint('crud', __name__, template_folder='template')


@crud.route('/crud')
def index():
    
    endereco = Endereco.query.all()
    if session.get('usuario_logado') and session.get('eh_admin'):
        return render_template('api/crud/tabela.html', endereco=endereco, is_admin=True)
    else:
        return render_template('api/crud/tabela.html', endereco=endereco)
     

@crud.route('/add', methods=['GET','POST'])
def add():   
    
    if request.method == 'POST':
        endereco = Endereco(request.form['nome'], request.form['email'], request.form['cidade'])
        print(endereco)
        db.session.add(endereco) #salva no DB
        db.session.commit()
        
        return redirect(url_for('crud.index'))
    
    return render_template('api/crud/add.html')


# rota PUT/atualizar
@crud.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    
    
    endereco = Endereco.query.get(id)
    if session.get('usuario_logado') and session.get('eh_admin'):
     
        if request.method == 'POST':
            endereco.nome = request.form['nome']
            endereco.email = request.form['email']
            endereco.cidade = request.form['cidade']
            db.session.commit()
            
            return redirect(url_for('crud.index'))
        
    else:
        flash('Somente um usuário ADMIN pode atualizar dados no Data Base.')  
    
    return render_template('api/crud/edit.html', endereco=endereco) 
    

@crud.route('/delete/<int:id>')
def delete(id):
    
    if session.get('usuario_logado') and session.get('eh_admin'):     
        endereco = Endereco.query.get(id)
        db.session.delete(endereco)
        db.session.commit()
        return redirect(url_for('crud.index'))
    
    else:
        return redirect(url_for('crud.index'))
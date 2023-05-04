from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from classes.database.database import db, Endereco, Usuarios

crud = Blueprint('crud', __name__, template_folder='template')

# redenderiza tabela que mostra os dados no banco de dados.
@crud.route('/crud', methods=['GET'])
def index():
    
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
      
    else:      
        # verifica se o usuário logado é ADM 
        endereco = Endereco.query.all()
        if session.get('usuario_logado') and session.get('eh_admin'):
            return render_template('api/crud/tabela.html', endereco=endereco, is_admin=True)
        else:
            return render_template('api/crud/tabela.html', endereco=endereco)
   
     
# renderiza add
@crud.route('/add-itens', methods=['GET'])
def add_itens():
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
    
    else:
        return render_template('api/crud/add.html')


    
# rota POST/adicionar
@crud.route('/add', methods=['POST'])
def add():   
    
    if request.method == 'POST':
        endereco = Endereco(request.form['nome'], request.form['email'], request.form['cidade'])

        db.session.add(endereco) #salva no DB
        db.session.commit()
        
        return redirect(url_for('crud.index'))
    
    return redirect(url_for('crud.add_itens'))


# rota PUT/atualizar
@crud.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
    
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
    

@crud.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    
    if session.get('usuario_logado') and session.get('eh_admin'):     
        endereco = Endereco.query.get(id)
        db.session.delete(endereco)
        db.session.commit()
        return redirect(url_for('crud.index'))
    
    else:
        return redirect(url_for('crud.index'))
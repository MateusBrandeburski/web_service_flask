from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from .database import db

crud = Blueprint('crud', __name__, template_folder='template')

class Endereco(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150))
    cidade = db.Column(db.String(20))

    
    def __init__(self, nome, email, cidade):
        self.nome = nome
        self.email = email
        self.cidade = cidade

        
         
@crud.route('/crud')
def index():
    endereco = Endereco.query.all()
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


@crud.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    endereco = Endereco.query.get(id)
    if request.method == 'POST':
        endereco.nome = request.form['nome']
        endereco.email = request.form['email']
        endereco.cidade = request.form['cidade']
        db.session.commit()
        return redirect(url_for('crud.index'))
    return render_template('api/crud/edit.html', endereco=endereco) 
        

@crud.route('/delete/<int:id>')
def delete(id):
    endereco = Endereco.query.get(id)
    db.session.delete(endereco)
    db.session.commit()
    return redirect(url_for('crud.index'))


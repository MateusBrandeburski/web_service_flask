from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from .database import db


crud = Blueprint('crud', __name__, template_folder='template')

class Estudantes(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


@crud.route('/crud')
def index():
    estudantes = Estudantes.query.all()
    return render_template('api/crud/tabela.html', estudantes=estudantes)
     

@crud.route('/add', methods=['GET','POST'])
def add():   
    if request.method == 'POST':
        estudante = Estudantes(request.form['nome'], request.form['idade'])
        db.session.add(estudante) #salva no DB
        db.session.commit()
        return redirect(url_for('crud.index'))
    return render_template('api/crud/add.html')


@crud.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    estudante = Estudantes.query.get(id)
    if request.method == 'POST':
        estudante.nome = request.form['nome']
        estudante.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('crud.index'))
    return render_template('api/crud/edit.html', estudante=estudante) 
        

@crud.route('/delete/<int:id>')
def delete(id):
    estudante = Estudantes.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('crud.index'))

def init_app(app):
     db.init_app(app)
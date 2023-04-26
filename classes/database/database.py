from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Endereco(db.Model):
    
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150))
    cidade = db.Column(db.String(20))

    def __init__(self, nome, email, cidade):
        self.nome = nome
        self.email = email
        self.cidade = cidade


class Usuarios(db.Model):
    
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    eh_admin = db.Column(db.Boolean, default=False)
    
    def __init__(self, nickname, senha, email):
        self.nickname = nickname
        self.senha = senha
        self.email = email
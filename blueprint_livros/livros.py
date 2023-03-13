from flask import Blueprint, render_template, request, redirect
livros = Blueprint('livros', __name__, template_folder='templates')


class Livro:
    
    def __init__(self, nome, editora, ano):
        self.nome = nome
        self.editora = editora
        self.ano = ano
        
livro1 = Livro('Fundação', 'Azimov', 'Aleph')
livro2 = Livro('A Surpreendente Ciência do Sucesso', 'Erik Barker', 'Ultimato')
livro3 = Livro('Bíblia', 'Variado', 'Variado')
lista = [livro1, livro2, livro3]


@livros.route('/lista')
def index():
    return render_template('livros_tudo.html', livros=lista)

@livros.route('/novo')
def renderiza_formulario():
    return render_template('livros.html', titulo='Testando')


@livros.route('/criar', methods=['POST'])
def pega_dados_do_formulario():
    nome = request.form['nome'] 
    autor = request.form['categoria']
    editora = request.form['console']
    livro = Livro(nome, autor, editora)
    lista.append(livro)
    
    return redirect('/lista')







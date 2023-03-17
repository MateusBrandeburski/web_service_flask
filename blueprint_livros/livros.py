from flask import Blueprint, render_template, request, redirect, session, flash


livros = Blueprint('livros', __name__, template_folder='livros')


class Livro:
      
    def __init__(self, nome, editora, ano):
        self.nome = nome
        self.editora = editora
        self.ano = ano
        
livro1 = Livro('Mateus Brandeburski', '00248088809', 'Negativo')
livro2 = Livro('Fernandinho Beiramar', '77754698745', 'Positivo')
livro3 = Livro('Raul Leopordo da Silva', '12365478921', 'Negativo')
livro4 = Livro('Suzana Vieira', '12365478921', 'Positivo')
livro5 = Livro('Renato Oliveira', '77754698745', 'Negativo')
livro6 = Livro('Paulo de Tarso', '12365478921', 'Positivo')
livro7 = Livro('Olavo de Carvalho', '74185296335', 'Negativo')
lista = [livro1, livro2, livro3, livro4, livro5, livro6, livro7]


# @livros.route('/lista')
# def index():
#     if 'usuario_logado' not in session or session['usuario_logado'] == None:
#         return redirect('/login')
    
#     return render_template('livros/lista_dados.html', livros=lista)



@livros.route('/novo')
def renderiza_formulario():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    
    return render_template('livros/cadastro_dados.html', titulo='Atena')



@livros.route('/criar', methods=['POST'])
def pega_dados_do_formulario():
    

    nome = request.form['nome'] 
    autor = request.form['categoria']
    editora = request.form['console']
    livro = Livro(nome, autor, editora)
    lista.append(livro)
    
    return redirect('/lista')



# @livros.route('/login')
# def login():
#     return render_template('livros/login.html')



# @livros.route('/autenticar', methods=['POST'])
# def autenticar():
#     if 'developer' in request.form['senha']:
#         session['usuario_logado'] = request.form['usuario']
#         flash('Usuário ' + session['usuario_logado'] + ' logado com sucesso') #mensagem rápida e única
#         return redirect('/lista')
#     else:
#         flash('Username ou password inválidos')
#         return redirect('/login')
  
  
    
@livros.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/login')
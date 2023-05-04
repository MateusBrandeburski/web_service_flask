from flask import Blueprint, render_template, redirect, session, url_for

sobre = Blueprint('sobre', __name__, template_folder='template')

@sobre.route('/sobre-o-projeto')
def index():
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
    return render_template('sobre_o_projeto/sobre_o_projeto.html')
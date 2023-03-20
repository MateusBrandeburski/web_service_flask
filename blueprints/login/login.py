from flask import Blueprint, render_template, request, redirect, session, flash, url_for


login = Blueprint('login', __name__, template_folder='login')


# Renderiza
@login.route('/login', methods=['GET'])
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return render_template('login/login.html')   
    return render_template('calculadora_grafica/calculadora_de_pitagoras.html')
 
   
@login.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('login.index'))

# Processa o login
@login.route('/autenticar', methods=['POST'])
def autenticar():
    if 'developer' in request.form['senha'] and 'MateusTI' in request.form['usuario']:
        session['usuario_logado'] = request.form['usuario']
        flash('Usuário ' + session['usuario_logado'] + ' logado com sucesso') #mensagem rápida e única
        return redirect(url_for('calculadora_grafica.index'))
    else:
        flash('Username ou password inválidos')
        return redirect(url_for('login.index'))
    
    


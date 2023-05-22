from flask import Blueprint, render_template, redirect, session, url_for


home = Blueprint('home', __name__, template_folder='template')


@home.route('/home', methods=['GET'])
def index():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
     else:
        return render_template('home/home.html')



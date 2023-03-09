from flask import Blueprint, request, render_template, redirect, url_for

limpa_email = Blueprint('limpa_email', __name__, template_folder='templates')

@limpa_email.route('/limpa_email', methods=['GET', 'POST'])
def robo_limpa_email():
    try:
        if request.form['action'] == 'teste':
            resposta = 'rota funcionando'
            return render_template('limpa_email.html', resposta=resposta)
        
    except:    
        return render_template('limpa_email.html')
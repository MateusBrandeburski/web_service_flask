from flask import Blueprint, request, render_template
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


limpa_email = Blueprint('limpa_email', __name__, template_folder='templates')









##########################################
# rota de teste (ainda em construção)
##########################################
@limpa_email.route('/limpa_email', methods=['GET', 'POST'])
def index():
    try:
        if request.form['action'] == 'teste':
            resposta = 'rota funcionando'

            return render_template('limpa_email.html', resposta=resposta)
        
    except:    
        return render_template('limpa_email.html')

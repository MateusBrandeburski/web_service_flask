from flask import Blueprint, render_template, request, redirect, session, flash, url_for


regra_3 = Blueprint('regra_3', __name__, template_folder='templates')

@regra_3.route('/calculadoras', methods=['GET'])
def index():
    return render_template('calculadoras/regra_de_3_simples/regra_de_3_simples.html')


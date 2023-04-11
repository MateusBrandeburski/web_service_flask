from flask import Blueprint, render_template, redirect, session, url_for

sobre = Blueprint('sobre', __name__, template_folder='template')

@sobre.route('/sobre-mim')
def index():
    return render_template('sobre_mim/sobre_mim.html')
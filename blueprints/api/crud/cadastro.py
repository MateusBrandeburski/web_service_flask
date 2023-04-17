from flask import Blueprint, render_template, request, redirect, url_for



cadastro = Blueprint('cadastro', __name__, template_folder='template')


@cadastro.route('/cadastro')
def register():
    
    return render_template ('login/cadastro.html')

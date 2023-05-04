from flask import Blueprint, render_template, request, redirect, url_for, flash
from classes.database.database import Usuarios, db
from classes.email.envia_gmail import Email


redefinir = Blueprint('redefinir', __name__, template_folder='template')


@redefinir.route('/redefinir-senha')
def index():

    return render_template('login/recuperar_senha/redefinir_senha.html')
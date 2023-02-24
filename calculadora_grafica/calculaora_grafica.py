from flask import Blueprint, request, render_template, redirect, url_for
from classes.gmail import Email
import os

calculadora_grafica = Blueprint('calculadora_grafica', __name__, template_folder='templates')


enviar = Email(os.environ["EMAIL"], os.environ["SENHA"])


@calculadora_grafica.route("/calculadora", methods=['GET'])
def calculadora():
     #hipo
     #ca
     #co
    pass

from flask import Blueprint, request, render_template, redirect, url_for
from classes.gmail import Email
from classes.formula_pitagoras import TeoremaDePitagoras
import os

calculadora_grafica = Blueprint('calculadora_grafica', __name__, template_folder='templates')
enviar = Email(os.environ["EMAIL"], os.environ["SENHA"])


@calculadora_grafica.route("/", methods=['GET'])
def index():
     
     try:
          return render_template('back_html.html', resposta=resposta)
     
     except NameError: # if resposta is not defined
          return render_template('back_html.html')

@calculadora_grafica.route("/", methods=['GET','POST'])
def calculadora():
      

     if request.form['action'] == 'calcular':
          
          if request.form.get('hipotenusa') != "":
               """
               Passando os 3 parâmetros, porque ele receber qualquer um dos lados do cateto para calcular o outro lado.
               """
               teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'),
                                            catetoO=request.form.get('cO'), 
                                            hipotenusa=request.form.get('hipotenusa'))
              
               global resposta
               resposta = round(teorema.calcular_catetos(), 2)
               return redirect(url_for('calculadora_grafica.index'))
  
               
          elif request.form.get('hipotenusa') == "":
               teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'), catetoO=request.form.get('cO'))
               resposta = teorema.calcular_hipotenusa()
               return redirect(url_for('calculadora_grafica.index'))

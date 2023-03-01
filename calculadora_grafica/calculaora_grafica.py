from flask import Blueprint, request, render_template, redirect, url_for
from classes.gmail import Email
from classes.formula_pitagoras import TeoremaDePitagoras
import os

calculadora_grafica = Blueprint('calculadora_grafica', __name__, template_folder='templates')
enviar = Email(os.environ["EMAIL"], os.environ["SENHA"])


# Rota index para protrocolo HTTPS GET. Ou seja, é a rota que renderiza a calculadora na tela.
@calculadora_grafica.route("/calculadora", methods=['GET'])
def index():
     
     global resposta
     if 'resposta' in globals() and resposta != "":
          return render_template('back_html.html', resposta=resposta)
     
     else:
          return render_template('back_html.html')
     
     
# Rota POST que serve apenas as ações da Calculadora de Pitágoras 
@calculadora_grafica.route("/calculadora", methods=['POST'])
def calculadora():
      
     if request.form['action'] == 'calcular':
          
          if  (request.form.get('hipotenusa') == "") and (request.form.get('cA') == "") and  (request.form.get('cO') == "") or (request.form.get('hipotenusa') == "") and (request.form.get('cA') == "") or  (request.form.get('hipotenusa') == "") and (request.form.get('cO') == "") or (request.form.get('cA') == "") and (request.form.get('cO') == "") or (request.form.get('cA') != "") and (request.form.get('cO') != "") and  (request.form.get('hipotenusa') != ""):
               
                   global resposta
                   resposta = TeoremaDePitagoras.strings_teorema(name="falta_parametros")
                   return redirect(url_for('calculadora_grafica.index'))
          
          
          else:
                          
               if request.form.get('hipotenusa') != "":
                    """
                    Passando os 3 parâmetros, porque ele receber qualquer um dos lados do cateto para calcular o outro lado.
                    """
                    
                    teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'),
                                             catetoO=request.form.get('cO'), 
                                             hipotenusa=request.form.get('hipotenusa'))
                    
                    
                    resposta = round(teorema.calcular_catetos(), 2)
                    return redirect(url_for('calculadora_grafica.index'))
     
                    
               elif request.form.get('hipotenusa') == "":
                    
                    teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'), catetoO=request.form.get('cO'))
                    resposta = round(teorema.calcular_hipotenusa(), 2)
                    return redirect(url_for('calculadora_grafica.index'))
               

               
          
         # erros para tratar. Número negativo, 1 campo preenchido, 3 campos prenchido, 3 campos não preenchidos
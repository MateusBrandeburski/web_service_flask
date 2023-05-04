from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from classes.calculadoras.regra_3.regra_3_formula import RegraDeTres
from classes.formula_pitagoras import TeoremaDePitagoras

calculadora = Blueprint('calculadora', __name__, template_folder='templates')


# index
@calculadora.route('/calculadoras', methods=['GET'])
def index():
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
    
    return render_template('calculadoras/calculadoras.html')

# Regra de Três
@calculadora.route('/regra3', methods=['GET','POST'])
def processa_regra_3():
    
    try:
        if 'regra_3' in request.form:
            resposta = RegraDeTres(A=request.form['A'], B=request.form['B'], C=request.form['C']).calcula_equivalencia_regra_de_3()
            
            return render_template('calculadoras/calculadoras.html', resposta_regra3=resposta)
    
    except ValueError:
         flash('Você precisa preencher os 3 campus para calcular Regra de Três')
         return render_template('calculadoras/calculadoras.html')
         
 
 
# Teorema de Pitágras        
@calculadora.route('/pitagoras', methods=['GET','POST'])   
def pitagoras():
    
        
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
          
    if 'hipotenusa' in request.form:     

          # Tramento de erro para número negativo, se é calculado um lado de um retângulo retângulo, número negativo é impossível.
          try: 
               # verifica 3 ou 2 campos foram deixados em branco, além de verificar se os 3 campos foram preenchidos.
               if  (request.form.get('hipotenusa') == "") and (request.form.get('cA') == "") and  (request.form.get('oposto') == "") or (request.form.get('hipotenusa') == "") and (request.form.get('cA') == "") or  (request.form.get('hipotenusa') == "") and (request.form.get('oposto') == "") or (request.form.get('cA') == "") and (request.form.get('oposto') == "") or (request.form.get('cA') != "") and (request.form.get('oposto') != "") and  (request.form.get('hipotenusa') != ""):   
                    
                    
                    flash('Apenas 2 lados devem ser prenchidos para calcular usando o Teorema de Pitágoras.')
                    return render_template('calculadoras/calculadoras.html')
               
               # Se 2 campos forem preenchidos corretamente:
               else:
                                   
                    # calcula os catetos
                    if request.form.get('hipotenusa') != "":   
                        # passando os 3 parâmetros, porque ele receber qualquer um dos lados do cateto para calcular o outro lado.
                        teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'),  # type: ignore
                                                catetoO=request.form.get('oposto'),   # type: ignore
                                                hipotenusa=request.form.get('hipotenusa'))  # type: ignore
                        resposta = teorema.calcular_catetos()
                        return render_template('calculadoras/calculadoras.html', resposta=resposta)
                    
                                
                    # calcula a hipotenusa
                    elif request.form.get('hipotenusa') == "":   
                        teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'), catetoO=request.form.get('oposto'))  # type: ignore
                        resposta = teorema.calcular_hipotenusa()
                        return render_template('calculadoras/calculadoras.html', resposta=resposta)
                     
          # Tramento de erro para número negativo, se é calculado um lado de um triângulo retângulo, número negativo é impossível.         
          except TypeError:
            
            flash('O valor da hipotenusa precisa ser maior do que o valor do cateto. Isso porque a fórmula calcula um triângulo retângulo, e nessa caso a hipotenusa é SEMPRE o maior lado.')
            
            return render_template('calculadoras/calculadoras.html')   

        
          

          
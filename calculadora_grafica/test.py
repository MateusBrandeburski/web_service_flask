@calculadora_grafica.route("/", methods=['GET'])
def index():
     
     try:
          return render_template('back_html.html', resposta=resposta)
     
     except NameError: # if resposta is not defined
          return render_template('back_html.html')

@calculadora_grafica.route("/", methods=['POST'])
def calculadora():
      

     if request.form['action'] == 'calcular':
          if request.form.get('hipotenusa') is not "":
               """
               Passando os 3 parâmetros, porque ele receber qualquer um dos lados do cateto para calcular o outro lado.
               """
               teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'),
                                            catetoO=request.form.get('cO'), 
                                            hipotenusa=request.form.get('hipotenusa'))
              
               # declarodo
               global resposta
               resposta = round(teorema.calcular_catetos(), 2)
               return redirect(url_for('calculadora_grafica.index'))
  
               
          if request.form.get('hiponenusa') is "":
               teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'), catetoO=request.form.get('cO'))
               


               
               return render_template('back_html.html', resposta=round(teorema.calcular_hipotenusa(), 2))


---------------------------------------------------------------

@calculadora_grafica.route("/", methods=['GET', 'POST'])
def calculadora():
   
   try:   
     if request.form['action'] == 'calcular':
          if request.form.get('hipotenusa') is not None:
               """
               Passando os 3 parâmetros, porque ele receber qualquer um dos lados do cateto para calcular o outro lado.
               """
               teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'),
                                            catetoO=request.form.get('cO'), 
                                            hipotenusa=request.form.get('hipotenusa'))
              
               return render_template('back_html.html', resposta=round(teorema.calcular_hipotenusa(), 2))

  
               
          if request.form.get('hiponenusa') is "":
               teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'), catetoO=request.form.get('cO'))
               
               
               return render_template('back_html.html', resposta=round(teorema.calcular_hipotenusa(), 2))
   except:
        return render_template('back_html.html')
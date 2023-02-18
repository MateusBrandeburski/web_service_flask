from flask import Blueprint, request, render_template, redirect, url_for
from classes.gmail import Email
import os

calculadora_grafica = Blueprint('calculadora_grafica', __name__, template_folder='templates')


enviar = Email(os.environ["EMAIL"], os.environ["SENHA"])


@calculadora_grafica.route("/", methods=['GET', 'POST'])
def index():

    try:
        if request.form['action'] == 'hipotenusa':
            return render_template('hipotenusa.html')
        
        elif request.form['action'] == 'adjacente':    
            return render_template('cateto_adjacente.html') 
        
        elif request.form['action'] == 'info':
            return render_template('infos.html')
        elif request.form['action'] == 'oposto':
           
            return render_template('cateto_oposto.html')
        
    except:
        pass
    
    return render_template('index.html')

# @calculadora_grafica.route("/info", methods=['GET'])
# def info():
#     enviar.envia_email()
#     return render_template('infos.html')

    
@calculadora_grafica.route("/hipotenusa", methods=['GET', 'POST'])
def hipotenusa():
    
    try:            
        if request.form['action'] == 'form_hipotenusa':
                    
            catetoB = float(request.form.get('catetoB'))
            catetoC = float(request.form.get('catetoC'))
            quadrado_da_hipotenusa = catetoB**2 + catetoC**2
            hipotenusa = quadrado_da_hipotenusa ** (1/2)
            
            return render_template('hipotenusa_resposta.html', catetoB=catetoB, catetoC=catetoC, quadrado_da_hipotenusa=quadrado_da_hipotenusa, hipotenusa=hipotenusa)
        else:
            return render_template('index.html')
    except:
        return render_template('hipotenusa.html')


    
@calculadora_grafica.route("/cateto_adjacente", methods=['GET', 'POST'])
def cateto_adjacente():
    
    try:            
        if request.form['action'] == 'form_adjacente':
                    
            cateto_oposto = float(request.form.get('cateto_oposto'))
            hipotenusa = float(request.form.get('hipotenusa'))
            # co² + x² = h²
            quadrado_do_cateto = cateto_oposto**2
            quadrado_da_hipotenusa = hipotenusa**2
            # x² = h² - co²
            passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto
            print(passa_subtraindo)
            cateto_adjacente_final = passa_subtraindo ** (1/2) # ou 0,5
                       
            return render_template('cateto_adjacente_resposta.html', cateto_oposto=cateto_oposto, hipotenusa=hipotenusa, cateto_adjacente_final=cateto_adjacente_final)
        else:
            return render_template('index.html')
    except:
        return render_template('cateto_adjacente.html')
        
    
        
@calculadora_grafica.route("/cateto_oposto", methods=['GET', 'POST'])
def cateto_oposto():
    
    try:            
        if request.form['action'] == 'form_oposto':
                    
            cateto_adjacente = float(request.form.get('cateto_adjacente'))
            hipotenusa = float(request.form.get('hipotenusa'))
            # ca² + x² = h²
            quadrado_do_cateto_adjacente = cateto_adjacente**2
            quadrado_da_hipotenusa = hipotenusa**2
            # x² = h² - ca²
            passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto_adjacente
            print(passa_subtraindo)
            cateto_oposto_final = passa_subtraindo ** (1/2) # ou 0,5
                       
            return render_template('cateto_oposto_resposta.html', cateto_adjacente=cateto_adjacente, hipotenusa=hipotenusa, cateto_oposto_final=cateto_oposto_final)
        else:
            return render_template('index.html')
    except:
        return render_template('cateto_oposto.html')
from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import requests


consulta_veiculo_df = Blueprint('consulta_veiculo_df', __name__, template_folder='template')

@consulta_veiculo_df.route('/consulta-veiculo-df') # type: ignore
def index():
  
    
    try:      
        url = 'https://api.infosimples.com/api/v2/consultas/detran/df/veiculo/mobile'
        args = {
        "placa":  placa, 
        "renavam": renavam, 
        "token":   "ezg57QOEI76knEGX5i0JvvU-W7kUp_PjpE_q7LFn",
        "timeout": 300
        }

        detran_df_situacao = requests.post(url, args)
        dic = detran_df_situacao.json()
     
        situacao = dic['data'][0]['gravame']['situacao']
        nome = dic['data'][0]['gravame']['financiado_nome']
        banco = dic['data'][0]['gravame']['agente_nome']
        data = dic['data'][0]['gravame']['datahora']
        
   
    except:
        return render_template("api/consulta_veiculo/consulta_veiculo.html")

    return render_template("api/consulta_veiculo/consulta_veiculo.html", situacao=situacao, data=data, banco=banco, nome=nome )


@consulta_veiculo_df.route('/processa-dados-detran-df', methods=['POST']) # type: ignore
def processa_dados_detran_df(): 
    global placa, renavam
    placa = request.form['placa']
    renavam = request.form['renavam']
    return redirect(url_for('consulta_veiculo_df.index'))
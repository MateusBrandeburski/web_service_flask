from flask import Flask
from blueprints.calculadora_grafica.calculaora_grafica import calculadora_grafica
from blueprints.calculadora_query.calculadora_query import calcularora_query
from blueprints.login.login import login
from blueprints.home.home import home
from blueprints.calculadora_grafica.regra_de_3_simples.regra_de_3_simples import regra_3
from blueprints.limpa_email.limpa_email import limpa_email
from blueprints.RPA.rpa import rpa


app = Flask(__name__)

# secret_key é para o cookie do navegador
app.secret_key = ['M4T3us']

app.register_blueprint(calculadora_grafica)
app.register_blueprint(calcularora_query)
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(regra_3)
app.register_blueprint(limpa_email)
app.register_blueprint(rpa)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
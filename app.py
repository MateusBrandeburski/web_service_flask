from flask import Flask
from blueprints.calculadoras.teorema_de_pitagoras.calculadora_grafica import calculadora_grafica
from blueprints.calculadoras.teorema_de_pitagoras.calculadora_query import calcularora_query
from blueprints.login.login import login
from blueprints.home.home import home
from blueprints.calculadoras.regra_de_3_simples.regra_de_3_simples import regra_3
from blueprints.web_scraping.web_scraping import web_scraping


app = Flask(__name__)
# secret_key é para o cookie do navegador
app.secret_key = ['M4T3us']

app.register_blueprint(calculadora_grafica)
app.register_blueprint(calcularora_query)
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(regra_3)
app.register_blueprint(web_scraping)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
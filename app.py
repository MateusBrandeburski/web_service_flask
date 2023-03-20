from flask import Flask
from blueprints.calculadora_grafica.calculaora_grafica import calculadora_grafica
from blueprints.calculadora_query.calculadora_query import calcularora_query
from blueprints.login.login import login

app = Flask(__name__)
# secret_key é para o cookie do navegador
app.secret_key = ['mateus']

app.register_blueprint(calculadora_grafica)
app.register_blueprint(calcularora_query)
app.register_blueprint(login)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
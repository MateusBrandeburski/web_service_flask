from flask import Flask
from blueprint_calculadora_grafica.calculaora_grafica import calculadora_grafica
from blueprint_calculadora_query.calculadora_query import calcularora_query
from blueprint_livros.livros import livros

app = Flask(__name__)
app.secret_key = ['mateus']

app.register_blueprint(calculadora_grafica)
app.register_blueprint(calcularora_query)
app.register_blueprint(livros)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
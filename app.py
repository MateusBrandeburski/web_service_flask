from flask import Flask
from blueprint_calculadora_grafica.calculaora_grafica import calculadora_grafica
from blueprint_calculadora_query.calculadora_query import calcularora_query
from blueprint_limpa_email.limpa_email import limpa_email
from blueprint_keyclock.keyclock import keyclock


app = Flask(__name__)

app.register_blueprint(calculadora_grafica)
app.register_blueprint(calcularora_query)
app.register_blueprint(limpa_email)


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
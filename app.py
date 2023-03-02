from flask import Flask, Blueprint, url_for
from calculadora_grafica.calculaora_grafica import calculadora_grafica
from calculadora_query.calculadora_query import calcularora_query
import asyncio

app = Flask(__name__)
app.register_blueprint(calculadora_grafica)
app.register_blueprint(calcularora_query)


if __name__ == '__main__':
    asyncio.get_event_loop()
    app.run( host='0.0.0.0', port=8000, debug=True)
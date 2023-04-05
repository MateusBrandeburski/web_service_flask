from flask import Flask
from blueprints.calculadoras.teorema_de_pitagoras.calculadora_grafica import calculadora_grafica
from blueprints.calculadoras.teorema_de_pitagoras.calculadora_query import calcularora_query
from blueprints.login.login import login
from blueprints.home.home import home
from blueprints.calculadoras.regra_de_3_simples.regra_de_3_simples import regra_3
from blueprints.web_scraping.web_scraping import web_scraping
from blueprints.api.crud.crud import crud
from blueprints.api.detran_df.consulta_veiculo import consulta_veiculo_df
from blueprints.api.crud.database import db
import os

# instancia do Flask
app = Flask(__name__)

# conexão com DB por meio do SQLALchemy
def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_TESTES_MATEUS']
    db.init_app(app)
    return app

# secret_key é para o cookie do navegador
app.secret_key = ['M4T3us']

# instancias de todas as rotas blueprints
app.register_blueprint(calculadora_grafica)
app.register_blueprint(calcularora_query)
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(regra_3)
app.register_blueprint(web_scraping)
app.register_blueprint(crud)
app.register_blueprint(consulta_veiculo_df)


if __name__ == '__main__':
    app = create_app()
    app.run( host='0.0.0.0', port=8000, debug=True)


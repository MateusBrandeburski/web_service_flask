from flask import Flask
from blueprints.home.home import home
from blueprints.calculadoras.calculadora import calculadora
from blueprints.web_scraping.web_scraping import web_scraping
from blueprints.api.crud.crud import crud
from blueprints.api.detran_df.consulta_veiculo import consulta_veiculo_df
from blueprints.sobre_mim.sobre_mim import sobre
from blueprints.telas_login.cadastro.cadastro import cadastro
from blueprints.telas_login.login.login import login
from blueprints.telas_login.recuperar_senha.recuperar_senha import recupera
from blueprints.telas_login.cadastro.redefinir_senha.redefinir_senha import redefinir

from classes.database.database import db
import os

# instancia do Flask
app = Flask(__name__)
# secret_key é para o cookie do navegador
app.secret_key = ['M4T3usBrand']

# instancias de todas as rotas blueprints
app.register_blueprint(login)
app.register_blueprint(recupera)
app.register_blueprint(cadastro)
app.register_blueprint(home)
app.register_blueprint(calculadora)
app.register_blueprint(web_scraping)
app.register_blueprint(crud)
app.register_blueprint(consulta_veiculo_df)
app.register_blueprint(sobre)
app.register_blueprint(redefinir)

# conexão com DB por meio do SQLALchemy, coloquei aqui porque eu preciso passar o 'app' como parâmetro e não posso gerar 'cirule_import'.
def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_TESTES_MATEUS']
    db.init_app(app)
    return app

app = create_app()
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8000, debug=True)
from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from bs4 import BeautifulSoup
import requests


rpa = Blueprint('rpa', __name__, template_folder='templates')

response = requests.get('https://g1.globo.com/')
content = response.content


@rpa.route('/rpa')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
          return redirect(url_for('login.index'))
      
    else:
        site = BeautifulSoup(content, 'html.parser')
        noticias = site.find_all('div', attrs={'class': 'feed-post-body'})
        listas = []
        for noticia in noticias:
            resumo = noticia.find('a', attrs={'class':'feed-post-link'}).text
            listas.append(resumo)
            
        return render_template('rpa/rpa.html', listas=listas)


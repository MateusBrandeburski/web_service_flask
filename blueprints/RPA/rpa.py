from flask import Blueprint, render_template, request, redirect, session, flash, url_for, Flask
from classes.web_scraping import WebScrapingBS4


rpa = Blueprint('rpa', __name__, template_folder='templates')


@rpa.route('/rpa')
def index():
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
      
    else:      
        return render_template('rpa/rpa.html')


@rpa.route('/minera-dados')
def minera_dados():
    
        scraping1 = WebScrapingBS4(link="https://spacetoday.com.br/")
        noticias = scraping1.perga_texto(elementoFILHO='a', elementoPAI='h2', tipoPAI='class', descricaoPAI='entry-title h2')
        links = scraping1.pega_url(elementoFILHO='a', elementoPAI='h2', tipoPAI='class', descricaoPAI='entry-title h2')
        
        itens_scraping1=zip(noticias, links)


        scraping2 = WebScrapingBS4(link='https://anmtv.com.br/')
        noticias = scraping2.perga_texto(elementoPAI='h3', tipoPAI='class', descricaoPAI='post__title typescale-2_5 line-limit-child line-limit-3', elementoFILHO='a')
        links = scraping2.pega_url(elementoPAI='h3', tipoPAI='class', descricaoPAI='post__title typescale-2_5 line-limit-child line-limit-3', elementoFILHO='a')
        
        itens_scraping2=zip(noticias, links)
        
        return render_template('rpa/rpa.html',  itens_scraping1=itens_scraping1, itens_scraping2=itens_scraping2)
        

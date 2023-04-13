from flask import Blueprint, render_template, request, redirect, session, flash, url_for, Flask
from classes.web_scraping import WebScrapingBS4
from classes.envia_gmail import Email
import os

web_scraping = Blueprint('web_scraping', __name__, template_folder='templates')

@web_scraping.route('/web-scraping')
def index():
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))

    else:      
        return render_template('web_scraping/web_scraping.html')


@web_scraping.route('/minera-dados')
def minera_dados():

    
        """ bloco de scraping
        Aqui todos os elementos html são passados como parâmetro das suas respectivas funções. Na classe, passa-se apenas o link do scraping.
        """
        scraping1 = WebScrapingBS4(link="https://revistagalileu.globo.com/")
        noticias = scraping1.perga_texto(elementoFILHO='a', elementoPAI='div', tipoPAI='class', descricaoPAI='highlight__title theme-title-element')
        links = scraping1.pega_url(elementoFILHO='a', elementoPAI='div', tipoPAI='class', descricaoPAI='highlight__title theme-title-element') 
        itens_scraping1=zip(noticias, links)

        scraping2 = WebScrapingBS4(link='https://anmtv.com.br/')
        noticias = scraping2.perga_texto(elementoPAI='h3', tipoPAI='class', descricaoPAI='post__title typescale-2_5 line-limit-child line-limit-3', elementoFILHO='a')
        links = scraping2.pega_url(elementoPAI='h3', tipoPAI='class', descricaoPAI='post__title typescale-2_5 line-limit-child line-limit-3', elementoFILHO='a') 
        itens_scraping2=zip(noticias, links)
        
        Email(os.environ['EMAIL'], os.environ['SENHA']).envia_email()
      
        return render_template('web_scraping/web_scraping.html',  itens_scraping1=itens_scraping1, itens_scraping2=itens_scraping2)   
    
    
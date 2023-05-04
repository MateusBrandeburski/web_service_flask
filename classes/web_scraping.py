from bs4 import BeautifulSoup
import requests


class WebScrapingBS4:
    
    """ Função contrutora. Ela pega e armazena os dados que são passados por aqui."""
    def __init__(self, link):
        self.link = link

     
    def perga_texto(self, elementoPAI, elementoFILHO, tipoPAI='', descricaoPAI='',tipoFILHO='', descricaoFILHO=''):
        #response
        response = requests.get(f'{self.link}') # Space Today
        content = response.content
        site = BeautifulSoup(content, 'html.parser')
        
        
        elementos_pai = site.find_all(f'{elementoPAI}', attrs={f'{tipoPAI}':f'{descricaoPAI}'})
        textos = []
        for texto in elementos_pai :
            texto_extraido = texto.find(f'{elementoFILHO}', attrs={f'{tipoFILHO}':f'{descricaoFILHO}'}).text
            textos.append(texto_extraido)
        
        return textos  
     
    def pega_url(self,  elementoPAI, elementoFILHO, tipoPAI='', descricaoPAI='',tipoFILHO='', descricaoFILHO=''):
        response = requests.get(f'{self.link}') # Animes
        content = response.content
        site = BeautifulSoup(content, 'html.parser')

        links = []
        elementos_pai = site.find_all(f'{elementoPAI}', attrs={f'{tipoPAI}':f'{descricaoPAI}'})  
        for elementos_filho in elementos_pai :
            link = elementos_filho.find(f'{elementoFILHO}', attrs={f'{tipoFILHO}':f'{descricaoFILHO}'})
            url = link.get('href')
            links.append(url)
            
        return links
    

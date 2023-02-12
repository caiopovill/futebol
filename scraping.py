import requests
from bs4 import BeautifulSoup

class Requester:
    def __init__(self) -> None:
        self.__url = 'https://www.placardefutebol.com.br/'

    def request_from_page(self):
        response = requests.get(self.__url)
        return response.text


class HtmlCollectorLinks:
    pass

class HtmlCollectorStats:
    pass

a = Requester()
html = a.request_from_page()
print(html)
soup = BeautifulSoup(html, 'html.parser')

list_campeonatos = soup.find('div', {'id': 'livescore'})
campeonatos = list_campeonatos.find_all('div',{'class':'container content'})

links_ativos = []

for campeonato in campeonatos:
    for jogo in campeonato.find_all('a'):
        if jogo.find('span'):
            if jogo.find('span').text == 'INTERVALO' or jogo.find('span').text == 'ENCERRADO' or jogo.find('span').text == 'INTERVALO':
                if not jogo['href'].startswith("https"):
                    link = 'https://www.placardefutebol.com.br'+jogo['href']
                links_ativos.append({
                    'link':link
                })

for link in links_ativos:
    print(link)


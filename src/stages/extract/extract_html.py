from typing import Type,Dict,List
from datetime import date
from bs4 import BeautifulSoup
import requests
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

class ExtractHtml:
    
    def __init__(self, html_collector) -> None:
        self.__html_collector = html_collector

    def request_from_page_links(self):
        response = requests.get('https://www.placardefutebol.com.br/')
        return {
            "status_code": response.status_code,
            "html": response.text
        }

    def request_from_page_stats(self, link):
        response = requests.get(link)
        return {
            "status_code": response.status_code,
            "html": response.text
        }

    def extract(self):
        extract_data = {}
        try:
            html_information_links = self.request_from_page_links()
            links = self.__html_collector.collect_links(html_information_links['html'])

            essential_info = []
            for link in links:

                html_link = self.request_from_page_stats(link['link'])
                essential_info.append(self.__html_collector.collect_stats(html_link['html']))
            extract_data['stats_info'] = essential_info
            extract_data['extraction_date'] = date.today()
            return extract_data
        except Exception as exception:
            raise ExtractError(str(exception)) from exception




class HtmlCollector():


    def collect_links(self, html: str) -> List[Dict[str,str]]:
        soup = BeautifulSoup(html, 'html.parser')

        list_campeonatos = soup.find('div', {'id': 'livescore'})
        campeonatos = list_campeonatos.find_all('div',{'class':'container content'})

        links_ativos = []
        
        for campeonato in campeonatos:
            for jogo in campeonato.find_all('a'):
                if jogo.find('span'):
                    if jogo.find('span').text == 'INTERVALO' or jogo.find('span').text == 'INTERVALO' or jogo.find('span').text == 'ENCERRADO':
                        if not jogo['href'].startswith("https"):
                            link = 'https://www.placardefutebol.com.br'+jogo['href']
                        links_ativos.append({
                            'link':link
                        })
        return links_ativos


    def collect_stats(self, html_link):
        from lxml import etree
        from bs4 import BeautifulSoup

        stats_ativos = []

        soup = BeautifulSoup(html_link, 'html.parser')
        dom = etree.HTML(str(soup))
        home_team = dom.xpath('//*[@id="livescore"]/div[1]/div[1]/div/div[2]/div[1]/a/h4')[0].text
        away_team = dom.xpath('//*[@id="livescore"]/div[1]/div[1]/div/div[2]/div[3]/a/h4')[0].text
        date = dom.xpath('//*[@id="livescore"]/div[1]/div[2]/p[1]/text()')[0]
        stage = dom.xpath('//*[@id="livescore"]/div[1]/div[1]/div/div[1]/div[2]/span[1]')[0].text

        stats = soup.find_all('td', {'class':'standing-table text-center stats-category'})
        stats_home = soup.find_all('td', {'class':'standing-table text-center stats-home-team'})
        stats_away = soup.find_all('td', {'class':'standing-table text-center stats-away-team'})

        dic = {}

        for n in range(len(stats)):
            dic[f'{stats[n].text} home_team'] = stats_home[n].text
            dic[f'{stats[n].text} away_team'] = stats_away[n].text

        dic = {k.strip().replace('\n', ''): v.strip() for k, v in dic.items()}

        stats = ['Posse de bola (%) home_team','Posse de bola (%) away_team',
                 'Total de passes home_team','Total de passes away_team',
                 'Passes corretos (%) home_team','Passes corretos (%) away_team',
                 'Total de chutes home_team','Total de chutes away_team',
                 'Chutes no gol home_team','Chutes no gol away_team',
                 'Escanteios home_team','Escanteios away_team',
                 'Faltas cometidas home_team','Faltas cometidas away_team']
        for stat in stats:
            try:
                dic[stat]
            except:
                dic[stat]='None'       



        stats_ativos.append({
            'home_team':home_team,
            'away_team':away_team,
            'date':date,
            'stage':stage,
            # 'referee':referee,
            # 'stadium':stadium,
            # 'grandstand': grandstand,
            # 'live':live,
            'posse_bola_home':dic['Posse de bola (%) home_team'],
            'posse_bola_away':dic['Posse de bola (%) away_team'],
            'passes_home':dic['Total de passes home_team'],
            'passes_away':dic['Total de passes away_team'],
            'passes_corretos_home':dic['Passes corretos (%) home_team'],
            'passes_corretos_away':dic['Passes corretos (%) away_team'],
            'total_chutes_home':dic['Total de chutes home_team'],
            'total_chutes_away':dic['Total de chutes away_team'],
            'chutes_no_gol_home':dic['Chutes no gol home_team'],
            'chutes_no_gol_away':dic['Chutes no gol away_team'],
            'escanteios_home':dic['Escanteios home_team'],
            'escanteios_away':dic['Escanteios away_team'],
            'faltas_cometidas_home':dic['Faltas cometidas home_team'],
            'faltas_cometidas_away':dic['Faltas cometidas away_team']
        })
        return stats_ativos
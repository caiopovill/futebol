from typing import Dict
import requests
from .interfaces.http_requester import HttpRequesterLinksInterface,HttpRequesterStatsInterface

class HttpRequesterLinks(HttpRequesterLinksInterface):
    def __init__(self) -> None:
        self.__url = 'https://www.placardefutebol.com.br/'

    def request_from_page_links(self):
        response = requests.get(self.__url)
        return {
            "status_code": response.status_code,
            "html": response.text
        }



class HttpRequesterStats(HttpRequesterStatsInterface):

    @classmethod
    def request_from_page_stats(cls, link):
        response = requests.get(link)
        return {
            "status_code": response.status_code,
            "html": response.text
        }

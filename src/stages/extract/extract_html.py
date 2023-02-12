from typing import Type
from datetime import date
from src.drivers.interfaces.http_requester import HttpRequesterLinksInterface, HttpRequesterStatsInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

class ExtractHtml:

    def __init__(self, http_requester_links: Type[HttpRequesterLinksInterface],
                        http_requester_stats: Type[HttpRequesterStatsInterface],
                        html_collector: Type[HtmlCollectorInterface]) -> None:
        self.__http_requester_links = http_requester_links
        self.__http_requester_stats = http_requester_stats
        self.__html_collector = html_collector


    def extract(self) -> ExtractContract:
        try:
            html_information_links = self.__http_requester_links.request_from_page_links()
            links = self.__html_collector.collect_links(html_information_links['html'])

            essential_info = []
            for link in links:

                html_link = self.__http_requester_stats.request_from_page_stats(link['link'])
                essential_info.append(self.__html_collector.collect_stats(html_link['html']))
            return ExtractContract(
                raw_information_content=essential_info,
                extraction_date=date.today()
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception

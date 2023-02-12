from abc import ABC, abstractmethod


class HttpRequesterLinksInterface(ABC):

    @abstractmethod
    def request_from_page_links(self):
        pass




class HttpRequesterStatsInterface(ABC):

    @abstractmethod
    def request_from_page_stats(self, link):
        pass

from abc import ABC, abstractmethod
from typing import List, Dict

class HtmlCollectorInterface(ABC):

    def collect_links(self, html: str) -> List[Dict[str,str]]:
        pass
    

    def collect_stats(self, links):
        pass


from typing import Dict
from abc import ABC, abstractmethod

class DatabaseRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_jogos(cls, data: Dict) -> None:
        pass
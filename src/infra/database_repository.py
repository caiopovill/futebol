from typing import Dict
from .database_connector import DatabaseConnector
from .interfaces.database_repository import DatabaseRepositoryInterface

class DatabaseRepository(DatabaseRepositoryInterface):
    
    @classmethod
    def insert_jogos(cls, data: Dict) -> None:
        query = """
            INSERT INTO jogos
                (home_team, away_team, date,stage, posse_bola_home,
                posse_bola_away, passes_home, passes_away,
                passes_corretos_home, passes_corretos_away,
                total_chutes_home, total_chutes_away,
                chutes_no_gol_home, chutes_no_gol_away,
                escanteios_home, escanteios_away,
                faltas_cometidas_home, faltas_cometidas_away,
                extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()

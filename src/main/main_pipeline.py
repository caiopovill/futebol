from src.stages.extract.extract_html import ExtractHtml, HtmlCollector
from src.stages.transform.transform_raw_data import TransformRawData
from src.stages.load.load_data import LoadData
from src.infra.database_connector import DatabaseConnector
from src.infra.database_repository import DatabaseRepository

class MainPipeline:
    def __init__(self) -> None:
        self.__extract_html = ExtractHtml(HtmlCollector())
        self.__transform_raw_data = TransformRawData()
        self.__load_data = LoadData(DatabaseRepository())
        
    def run_pipeline(self) -> None:
        DatabaseConnector.connect()
        extract_contract = self.__extract_html.extract()
        transformed_data_contract = self.__transform_raw_data.transform(extract_contract)
        self.__load_data.load(transformed_data_contract)
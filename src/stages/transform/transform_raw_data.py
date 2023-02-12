from typing import List, Dict
from src.errors.transform_error import TransformError

class TransformRawData:

    def transform(self, extract_data):

        try:
            transformed_information = self.__filter_and_transform_data(extract_data)
            return transformed_information
        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter_and_transform_data(self, extract_data) -> List[List[Dict]]:
        extraction_date = extract_data['extraction_date']
  
        data_content = extract_data['stats_info']
        data_content = [dict for sublist in data_content for dict in sublist]

        transformed_information = []

        for data in data_content:
            transformed_data = None
            passes_corretos = data['passes_corretos_home']
            faltas_cometidas = data['faltas_cometidas_away']

            #ADICIONAR CONDIÇÕES AQUI
            # if passes_corretos != 'None' and faltas_cometidas != 'None': continue

            transformed_data = data
            transformed_data['extraction_date'] = extraction_date

            transformed_information.append(transformed_data)
        return transformed_information
    
from src.stages.contracts.mocks.extract_contract import extract_contract_mock
from src.stages.contracts.transform_contract import TransformContract
from .transform_raw_data import TransformRawData
from src.errors.transform_error import TransformError

def test_transform():
    transform_raw_data = TransformRawData()

    transformed_data_contract  = transform_raw_data.transform(extract_contract_mock)
    print(transformed_data_contract)
    assert isinstance(transformed_data_contract, TransformContract)
    assert 'home_team' in transformed_data_contract.load_content[0]
    assert 'away_team' in transformed_data_contract.load_content[0]
    assert 'passes_corretos_home' in transformed_data_contract.load_content[0]
    assert 'posse_bola_away' in transformed_data_contract.load_content[0]
    assert 'passes_away' in transformed_data_contract.load_content[0]


def test_transform_error():
    transform_raw_data = TransformRawData()

    try:
        transform_raw_data.transform('Entrada com erro')
    except Exception as exception: # pylint: disable=broad-except
         assert isinstance(exception, TransformError)

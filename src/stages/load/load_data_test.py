from src.stages.contracts.mocks.transform_contract import transform_contract_mock
from src.errors.load_error import LoadError
from .load_data import LoadData

class RepositorySpy:
    def __init__(self) -> None:
        self.insert_jogos_attributes = []

    def insert_jogos(self, data):
        self.insert_jogos_attributes.append(data)

def test_load():
    repo = RepositorySpy()
    load_data = LoadData(repo)

    load_data.load(transform_contract_mock)
    assert repo.insert_jogos_attributes == transform_contract_mock.load_content

def test_load_error():
    repo = RepositorySpy()
    load_data = LoadData(repo)

    try:
        load_data.load('Entrada com erro')
    except Exception as exception:
        assert isinstance(exception, LoadError)

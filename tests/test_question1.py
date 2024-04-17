import pytest
from src.question1 import Contract, Contracts


@pytest.fixture
def contracts_instance():
    return Contracts()

def test_get_top_n_open_contracts(contracts_instance):
    open_contracts = [
        Contract(id=1, debt=100),
        Contract(id=2, debt=200),
        Contract(id=3, debt=150),
        Contract(id=4, debt=50),
        Contract(id=5, debt=300)
    ]
    renegotiated_contracts = [2, 4]
    top_n = 3

    expected_result = [5, 3, 1]  

    assert contracts_instance.get_top_n_open_contracts(open_contracts, renegotiated_contracts, top_n) == expected_result

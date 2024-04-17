import pytest
from src.question2 import Orders


@pytest.fixture
def orders_instance():
    return Orders()

def test_combine_orders_specific_example(orders_instance):
    requests = [70, 30, 10]
    n_max = 100
    limit_per_trip = 2
    expected_order = 2
    assert orders_instance.combine_orders(requests, n_max, limit_per_trip) == expected_order

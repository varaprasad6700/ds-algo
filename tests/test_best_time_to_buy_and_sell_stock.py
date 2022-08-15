import pytest

from src.ds.best_time_to_buy_and_sell_stock import max_profit


@pytest.mark.parametrize("inp, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0)
])
def test_max_profit(inp, expected):
    assert max_profit(inp) == expected

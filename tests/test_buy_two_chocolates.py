from typing import List

import pytest

from src.ds.buy_two_chocolates import buy_choco


@pytest.mark.parametrize("prices, money, expected", [
    ([1, 2, 2], 3, 0),
    ([3, 2, 3], 3, 3),

])
def test_buy_choco(prices: List[int], money: int, expected: int):
    assert buy_choco(prices, money) == expected

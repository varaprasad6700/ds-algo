from typing import List

import pytest

from src.ds.generate_parenthesis import generate_parenthesis


@pytest.mark.parametrize("inp, expected", [
    (3, ['()()()', '()(())', '(())()', '(()())', '((()))'])
])
def test_generate_parenthesis(inp: int, expected: List[str]):
    assert generate_parenthesis(inp) == expected

import pytest

from src.ds.split_array_to_consec_subseq import split_array_to_consec_subseq_possible


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 3, 3, 4, 5], True),
    ([1, 2, 3, 3, 4, 4, 5, 5], True),
    ([1, 2, 3, 4, 4, 5], False)
])
def test_split_array_to_consec_subseq_possible(inp, expected):
    assert split_array_to_consec_subseq_possible(inp) == expected

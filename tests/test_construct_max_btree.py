import pytest

from src.ds.maximum_binary_tree import construct_maximum_binary_tree
from src.helper.TreeNode import TreeNode


@pytest.mark.parametrize("nums, expected_pre, expected_post, expected_in", [
    ([3, 2, 1, 6, 0, 5], [6, 3, 2, 1, 5, 0], [1, 2, 3, 0, 5, 6], [3, 2, 1, 6, 0, 5]),
    ([3, 2, 1], [3, 2, 1], [1, 2, 3], [3, 2, 1])
])
def test_construct_max_btree(nums, expected_pre, expected_post, expected_in):
    temp = TreeNode.get_pre_post_in_orders(construct_maximum_binary_tree(nums))
    assert temp[0] == expected_pre
    assert temp[1] == expected_post
    assert temp[2] == expected_in

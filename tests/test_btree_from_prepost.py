import pytest

from src.ds.binary_tree_from_pre_post import construct_from_pre_post
from src.helper.TreeNode import TreeNode


@pytest.mark.parametrize("preorder, postorder, expected_pre, expected_post, expected_in", [
    ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1], [4, 2, 5, 1, 6, 3, 7])
])
def test_bt_from_pre_in(preorder, postorder, expected_pre, expected_post, expected_in):
    temp = TreeNode.get_pre_post_in_orders(construct_from_pre_post(preorder, postorder))
    assert temp[0] == expected_pre
    assert temp[1] == expected_post
    assert temp[2] == expected_in

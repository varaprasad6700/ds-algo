import pytest

from src.ds.binary_tree_from_pre_in_order import build_tree_pre_in
from src.helper.TreeNode import TreeNode


@pytest.mark.parametrize("inorder, preorder, expected_pre, expected_post, expected_in", [
    ([9, 3, 15, 20, 7], [3, 9, 20, 15, 7], [3, 9, 20, 15, 7], [9, 15, 7, 20, 3], [9, 3, 15, 20, 7])
])
def test_bt_from_pre_in(inorder, preorder, expected_pre, expected_post, expected_in):
    temp = TreeNode.get_pre_post_in_orders(build_tree_pre_in(preorder, inorder))
    assert temp[0] == expected_pre
    assert temp[1] == expected_post
    assert temp[2] == expected_in

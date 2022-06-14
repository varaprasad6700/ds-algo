import pytest

from src.ds.binary_tree_from_in_post import build_tree_in_post
from src.helper.TreeNode import TreeNode


@pytest.mark.parametrize("inorder, postorder, expected_pre, expected_post, expected_in", [
    ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, 15, 7], [9, 15, 7, 20, 3], [9, 3, 15, 20, 7])
])
def test_bt_from_in_post(inorder, postorder, expected_pre, expected_post, expected_in):
    temp = TreeNode.get_pre_post_in_orders(build_tree_in_post(inorder, postorder))
    assert temp[0] == expected_pre
    assert temp[1] == expected_post
    assert temp[2] == expected_in

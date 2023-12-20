from typing import Optional

import pytest

from src.ds.range_sum_of_BST import range_sum_bst
from src.helper.TreeNode import TreeNode


@pytest.mark.parametrize("tree, low, high, expected", [
    (TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15, 32)
])
def test_range_sum_bst(tree: Optional[TreeNode], low: int, high: int, expected: int):
    assert range_sum_bst(tree, low, high) == expected

from typing import Optional

import pytest

from src.ds.leaf_similar_trees import leaf_similar
from src.helper.TreeNode import TreeNode


@pytest.mark.parametrize("tree1, tree2, expected", [
    (TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8))),TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8)))), True),
    (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(2)), False)
])
def test_leaf_similar(tree1: Optional[TreeNode], tree2: Optional[TreeNode], expected: bool):
    assert leaf_similar(tree1, tree2) == expected

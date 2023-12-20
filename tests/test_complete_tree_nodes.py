from typing import Optional

import pytest

from src.ds.complete_tree_nodes import count_nodes
from src.helper.TreeNode import TreeNode


@pytest.mark.parametrize("inp, expected", [
    (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))), 6),
    (None, 0),
    (TreeNode(1), 1)
])
def test_count_nodes(inp: Optional[TreeNode], expected: int):
    assert count_nodes(inp) == expected

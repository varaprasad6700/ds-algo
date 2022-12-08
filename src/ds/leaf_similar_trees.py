"""
https://leetcode.com/problems/leaf-similar-trees/description/
"""
from typing import Optional, List

from src.helper.TreeNode import TreeNode


def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if root1 is None or root2 is None:
        return root1 is None and root2 is None
    leaf1 = get_leaf_nodes(root1)
    leaf2 = get_leaf_nodes(root2)
    return leaf1 == leaf2


def get_leaf_nodes(q: TreeNode) -> List[int]:
    stack = [q]
    leaf = []
    while stack:
        node = stack.pop()
        if node.left is None and node.right is None:
            leaf.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return leaf


if __name__ == '__main__':
    tree1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
    tree2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
    print(leaf_similar(tree1, tree2))


"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from typing import List, Optional

from src.helper.TreeNode import TreeNode


def build_tree_pre_in(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    val = preorder[0]
    val_pos = inorder.index(val)
    left = build_tree_pre_in(preorder[1: 1 + val_pos], inorder[:val_pos])
    right = build_tree_pre_in(preorder[1 + val_pos:], inorder[val_pos + 1:])
    return TreeNode(val, left, right)


if __name__ == '__main__':
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    temp = build_tree_pre_in(pre, ino)
    print(TreeNode.get_pre_post_in_orders(temp))

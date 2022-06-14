"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
from typing import List, Optional

from src.helper.TreeNode import TreeNode


def build_tree_in_post(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if len(postorder) == 0 or len(inorder) == 0:
        return None
    val = postorder[-1]
    val_pos = inorder.index(val)
    left = build_tree_in_post(inorder[:val_pos], postorder[0: val_pos])
    right = build_tree_in_post(inorder[val_pos + 1:], postorder[val_pos:-1])
    return TreeNode(val, left, right)


if __name__ == '__main__':
    ino = [9, 3, 15, 20, 7]
    post = [9, 15, 7, 20, 3]
    temp = build_tree_in_post(ino, post)
    print(TreeNode.pre_order(temp), TreeNode.in_order(temp), TreeNode.post_order(temp))

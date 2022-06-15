"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""
from typing import List, Optional

from src.helper.TreeNode import TreeNode


def construct_from_pre_post(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) == 0 or len(postorder) == 0:
        return None
    elif len(preorder) == 1 or len(postorder) == 1:
        return TreeNode(preorder[0])
    else:
        left = construct_from_pre_post(preorder[1: 2 + postorder.index(preorder[1])],
                                       postorder[:1 + postorder.index(preorder[1])])
        right = construct_from_pre_post(preorder[2 + postorder.index(preorder[1]):],
                                        postorder[1 + postorder.index(preorder[1]):-1])
        return TreeNode(preorder[0], left, right)


if __name__ == '__main__':
    temp = construct_from_pre_post([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    print(TreeNode.get_pre_post_in_orders(temp))

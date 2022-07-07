"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
from collections import deque
from typing import Optional

from src.helper.TreeNode import TreeNode


def min_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        if root.left is None:
            return 1 + min_depth(root.right)
        if root.right is None:
            return 1 + min_depth(root.left)
        return 1 + min(min_depth(root.left), min_depth(root.right))


def min_depth_queue_appr(root: Optional[TreeNode]) -> int:
    if root is None: return 0
    q = deque([root])
    h = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node.left is None and node.right is None:
                return h
        h += 1


if __name__ == '__main__':
    print(min_depth(TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5))))))
    print(min_depth_queue_appr(TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5))))))

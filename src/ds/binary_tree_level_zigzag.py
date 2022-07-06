"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from collections import deque
from typing import Optional, List

from src.helper.TreeNode import TreeNode


def zig_zag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    q = deque([root])
    forward = True
    out = []
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.val)
        if forward:
            out.append(level)
        else:
            out.append(level[::-1])
        forward = not forward
    return out


if __name__ == '__main__':
    print(zig_zag_level_order(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

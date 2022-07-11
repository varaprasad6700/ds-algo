"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""
from collections import deque
from typing import Optional, List

from src.helper.TreeNode import TreeNode


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    else:
        q = deque([root])
        out = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level[-1])
        return out


if __name__ == '__main__':
    print(right_side_view(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))

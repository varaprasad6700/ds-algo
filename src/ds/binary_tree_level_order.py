from collections import deque
from queue import Queue
from typing import Optional, List

from src.helper.TreeNode import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    https://leetcode.com/problems/binary-tree-level-order-traversal/
    """
    if root is None:
        return []
    q = Queue()
    q.put(root)
    out = []
    while not q.empty():
        temp = []
        for i in range(q.qsize()):
            curr = q.get()
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
            temp.append(curr.val)
        out.append(temp)
    return out


def binary_tree_level_order_rev(root: Optional[TreeNode]) -> List[List[int]]:
    """
    https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
    """
    if root is None:
        return []
    out = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.val)
        out.append(level)
    return out[::-1]


if __name__ == '__main__':
    print(level_order(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(binary_tree_level_order_rev(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

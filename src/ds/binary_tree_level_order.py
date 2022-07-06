"""

"""
from queue import Queue
from typing import Optional, List

from src.helper.TreeNode import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
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


if __name__ == '__main__':
    print(level_order(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

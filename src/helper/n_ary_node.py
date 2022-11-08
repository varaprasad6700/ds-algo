"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
from typing import List


class NAryNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    @staticmethod
    def preorder(root) -> List[int]:
        if root is None:
            return []
        out = [root.val]
        for i in root.children:
            out += NAryNode.preorder(i)
        return out

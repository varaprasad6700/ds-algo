from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # pre-order traversal
    @staticmethod
    def pre_order(root) -> List[int]:
        if root is None:
            return []
        return [root.val] + TreeNode.pre_order(root.left) + TreeNode.pre_order(root.right)

    # post-order traversal
    @staticmethod
    def post_order(root) -> List[int]:
        if root is None:
            return []
        return TreeNode.post_order(root.left) + TreeNode.post_order(root.right) + [root.val]

    # in-order traversal
    @staticmethod
    def in_order(root) -> List[int]:
        if root is None:
            return []
        return TreeNode.in_order(root.left) + [root.val] + TreeNode.in_order(root.right)

    @staticmethod
    def get_pre_post_in_orders(root) -> List[List[int]]:
        return [TreeNode.pre_order(root), TreeNode.post_order(root), TreeNode.in_order(root)]


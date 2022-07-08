from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # pre-order traversal
    @staticmethod
    def pre_order(root) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-preorder-traversal/
        """
        if root is None:
            return []
        return [root.val] + TreeNode.pre_order(root.left) + TreeNode.pre_order(root.right)

    # post-order traversal
    @staticmethod
    def post_order(root) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-postorder-traversal/
        """
        if root is None:
            return []
        return TreeNode.post_order(root.left) + TreeNode.post_order(root.right) + [root.val]

    # in-order traversal
    @staticmethod
    def in_order(root) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/
        """
        if root is None:
            return []
        return TreeNode.in_order(root.left) + [root.val] + TreeNode.in_order(root.right)

    @staticmethod
    def in_order_with_stack(root) -> List[int]:
        stack = []
        out = []
        while root is not None or len(stack) != 0:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            out.append(root.val)
            root = root.right
        return out

    @staticmethod
    def get_pre_post_in_orders(root) -> List[List[int]]:
        return [TreeNode.pre_order(root), TreeNode.post_order(root), TreeNode.in_order(root)]

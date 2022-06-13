from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # in-order traversal
    @staticmethod
    def convert_tree_to_list(root) -> List[int]:
        if root is None:
            return []
        return [root.val] + TreeNode.convert_tree_to_list(root.left) + TreeNode.convert_tree_to_list(root.right)
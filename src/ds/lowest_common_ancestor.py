"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
from src.helper.TreeNode import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    maxi = max(p.val, q.val)
    mini = min(p.val, q.val)
    if mini <= root.val <= maxi:
        return root
    else:
        if maxi < root.val:
            return lowest_common_ancestor(root.left, p, q)
        else:
            return lowest_common_ancestor(root.right, p, q)


if __name__ == '__main__':
    tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    print(lowest_common_ancestor(tree, TreeNode(2), TreeNode(8)).val)
    print(lowest_common_ancestor(tree, TreeNode(2), TreeNode(4)).val)

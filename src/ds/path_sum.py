from typing import Optional, List

from src.helper.TreeNode import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    """
    https://leetcode.com/problems/path-sum/
    """
    if root is None:
        return False
    elif root.left is None and root.right is None:
        return target_sum == root.val
    else:
        rem = target_sum - root.val
        return has_path_sum(root.left, rem) or has_path_sum(root.right, rem)


def path_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    https://leetcode.com/problems/path-sum-ii/
    """
    if root is None:
        return []
    elif root.left is None and root.right is None:
        if target_sum == root.val:
            return [[root.val]]
        else:
            return []
    else:
        l = path_sum(root.left, target_sum - root.val)
        r = path_sum(root.right, target_sum - root.val)
        out = []
        for i in l:
            out.append([root.val] + i)
        for i in r:
            out.append([root.val] + i)
        return out


if __name__ == '__main__':
    print(has_path_sum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
    print(path_sum(TreeNode(1, TreeNode(2), TreeNode(3)), 3))

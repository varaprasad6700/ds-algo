"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from typing import List, Optional

from src.helper.TreeNode import TreeNode


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0 or nums[0] is None:
        return None
    elif len(nums) == 1:
        return TreeNode(nums[0])
    else:
        mid = len(nums) // 2
        left = sorted_array_to_bst(nums[:mid])
        right = sorted_array_to_bst(nums[mid + 1:])
        return TreeNode(nums[mid], left, right)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    print(TreeNode.pre_order(sorted_array_to_bst(nums)))

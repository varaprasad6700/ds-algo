"""
https://leetcode.com/problems/maximum-binary-tree/
"""
from typing import List, Optional

from src.helper.TreeNode import TreeNode


def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    else:
        m = nums[0]
        ind = 0
        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]
                ind = i
        left = construct_maximum_binary_tree(nums[:ind])
        right = construct_maximum_binary_tree(nums[ind + 1:])
        return TreeNode(m, left, right)


if __name__ == '__main__':
    temp = construct_maximum_binary_tree([3, 2, 1, 6, 0, 5])
    print(TreeNode.get_pre_post_in_orders(temp))

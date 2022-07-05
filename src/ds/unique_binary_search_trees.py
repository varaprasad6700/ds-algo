"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
"""
from typing import List, Optional

from src.helper.TreeNode import TreeNode


def generate_trees(n: int) -> List[Optional[TreeNode]]:
    def create_tree(left, right):
        if left > right:
            return [None]
        else:
            out = []
            for i in range(left, right + 1):
                l_tree = create_tree(left, i - 1)
                r_tree = create_tree(i + 1, right)
                for j in range(len(l_tree)):
                    l = l_tree[j]
                    for k in range(len(r_tree)):
                        r = r_tree[k]
                        temp = TreeNode(i, l, r)
                        out.append(temp)
            return out

    return create_tree(1, n)


dp = {0: 1, 1: 1, 2: 2, 3: 5}


def unique_binary_search_tree_count(n: int):
    if n in dp:
        return dp[n]
    else:
        dp[n] = 0
        for i in range(1, n + 1):
            # cartesian product of left possible and right trees
            dp[n] += unique_binary_search_tree_count(i - 1) * unique_binary_search_tree_count(n - i)
        return dp[n]


if __name__ == '__main__':
    print([TreeNode.pre_order(i) for i in generate_trees(3)])
    print(unique_binary_search_tree_count(5))

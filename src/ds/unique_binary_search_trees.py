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


if __name__ == '__main__':
    print([TreeNode.pre_order(i) for i in generate_trees(3)])

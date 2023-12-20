"""
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
"""
from typing import List


def find_winners(matches: List[List[int]]) -> List[List[int]]:
    won = set()
    lost_once = set()
    lost_more = set()
    for i in matches:
        won.add(i[0])
        if i[1] in lost_once:
            lost_more.add(i[1])
        lost_once.add(i[1])
    return [sorted(won - lost_once), sorted(lost_once - lost_more)]


if __name__ == '__main__':
    print(find_winners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))

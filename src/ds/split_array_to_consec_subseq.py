"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/
"""
from typing import List


def split_array_to_consec_subseq_possible(nums: List[int]) -> bool:
    l = []
    for i in nums[::-1]:
        for j in l[::-1]:
            if j[-1] == i + 1:
                j.append(i)
                break
        else:
            l.append([i])
    return all(len(i) >= 3 for i in l)


if __name__ == '__main__':
    print(split_array_to_consec_subseq_possible([1, 2, 3, 3, 4, 5]))

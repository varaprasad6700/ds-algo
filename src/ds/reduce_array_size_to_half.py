"""
https://leetcode.com/problems/reduce-array-size-to-the-half/
"""
from collections import Counter
from typing import List


def reduce_arr_to_half_min_set(arr: List[int]) -> int:
    store = Counter(arr)
    original_len = len(arr)
    n = len(arr)
    out_ = 0
    for i, count in store.most_common(original_len):
        n = n - count
        out_ += 1
        if n <= original_len // 2:
            break
    return out_


if __name__ == '__main__':
    print(reduce_arr_to_half_min_set([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))

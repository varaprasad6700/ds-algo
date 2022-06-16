from collections import Counter
from typing import List, Dict


def dutch_national_flag(nums: List[int]) -> List[int]:
    store: Dict[int, int] = Counter(nums)
    i: int = 0
    while store[0] != 0:
        nums[i] = 0
        store[0] -= 1
        i += 1
    while store[1] != 0:
        nums[i] = 1
        store[1] -= 1
        i += 1
    while store[2] != 0:
        nums[i] = 2
        store[2] -= 1
        i += 1
    return nums


if __name__ == '__main__':
    print(dutch_national_flag([0, 2, 0, 2, 2, 0]))

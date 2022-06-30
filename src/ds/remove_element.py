from typing import List


def remove_element(nums: List[int], val: int) -> int:
    i = 0
    k = 0
    n = len(nums)
    while i < n - k:
        if nums[i] == val:
            nums[i], nums[n - k - 1] = nums[n-k-1], nums[i]
            k += 1
        else:
            i += 1
    return n - k


if __name__ == '__main__':
    inp = [3,2,2,3]
    print(remove_element(inp, 3))
    print(inp)

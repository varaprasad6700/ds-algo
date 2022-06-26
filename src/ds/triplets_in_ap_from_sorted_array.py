from typing import List


def triplets_in_ap_from_sorted_array(nums: List[int]) -> List[List[int]]:
    out_ = []
    for i in range(1, len(nums) - 1):
        l = i - 1
        r = i + 1
        while l >= 0 and r <= len(nums) - 1:
            if nums[i] - nums[l] == nums[r] - nums[i]:
                out_.append([nums[l], nums[i], nums[r]])
                l -= 1
                r += 1
            elif nums[i] - nums[l] > nums[r] - nums[i]:
                r += 1
            else:
                l -= 1
    return out_


if __name__ == '__main__':
    print(triplets_in_ap_from_sorted_array(
        [2, 6, 9, 12, 17, 22, 31, 32, 35, 42]))

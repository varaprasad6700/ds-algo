"""
https://leetcode.com/problems/jump-game/
"""


def can_jump(nums: List[int]) -> bool:
    dest = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= dest:
            dest = i
    return dest == 0


if __name__ == "__main__":
    print(can_jump([3, 2, 1, 0, 4]))
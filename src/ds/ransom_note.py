"""
https://leetcode.com/problems/ransom-note/
"""


def can_construct(ransom_note: str, magazine: str) -> bool:
    mag_dict: dict = {}
    for i in magazine:
        mag_dict[i] = mag_dict.get(i, 0) + 1
    for i in ransom_note:
        if i not in mag_dict or mag_dict[i] == 0:
            return False
        mag_dict[i] -= 1
    return True


if __name__ == '__main__':
    print(can_construct("aa", "aab"))

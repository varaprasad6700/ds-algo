"""
https://leetcode.com/problems/path-crossing/
"""


def is_path_crossing(path: str) -> bool:
    store = {(0, 0)}
    x = 0
    y = 0
    for i in path:
        if i == 'N':
            y += 1
        elif i == 'S':
            y -= 1
        elif i == 'E':
            x += 1
        else:
            x -= 1
        if (x, y) in store:
            return True
        store.add((x, y))
    return False


if __name__ == '__main__':
    print(is_path_crossing("NESWW"))

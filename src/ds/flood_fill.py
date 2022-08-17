"""
https://leetcode.com/problems/flood-fill/
"""
from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    def helper(image: List[List[int]], sr: int, sc: int, color: int, init_color: int) -> None:
        if image[sr][sc] == color or image[sr][sc] != init_color:
            return
        image[sr][sc] = color
        if sr > 0:
            helper(image, sr - 1, sc, color, init_color)
        if sc > 0:
            helper(image, sr, sc - 1, color, init_color)
        if sr < len(image) - 1:
            helper(image, sr + 1, sc, color, init_color)
        if sc < len(image[0]) - 1:
            helper(image, sr, sc + 1, color, init_color)

    helper(image, sr, sc, color, image[sr][sc])
    return image


if __name__ == '__main__':
    print(flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))

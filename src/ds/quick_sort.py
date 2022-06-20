from typing import List


def quick_sort(arr: List, left: int, right: int) -> None:
    def partition(a: List, l: int, r: int) -> int:
        x = a[r]
        i = l - 1
        for j in range(l, r):
            if a[j] <= x:
                i = i + 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        return i + 1

    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)


if __name__ == '__main__':
    nums = [0, -1, 10, 5, 7, -6]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)

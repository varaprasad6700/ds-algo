from typing import List


def merge(arr, left, mid, right):
    left_array = arr[left:mid + 1]
    right_array = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


if __name__ == '__main__':
    a = nums = [0, -1, 10, 5, 7, -6]
    merge_sort(nums, 0, len(nums) - 1)
    print(a)

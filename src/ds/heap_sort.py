from typing import List


def _heapify(arr: List[int], n: int, i: int):
    large = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[large] < arr[l]:
        large = l
    if r < n and arr[large] < arr[r]:
        large = r
    if large != i:
        arr[i], arr[large] = arr[large], arr[i]
        _heapify(arr, n, large)


def heapify(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)


def heap_sort(arr: List[int]) -> None:
    n = len(arr)
    heapify(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)


if __name__ == '__main__':
    a = [10, 1, 0, -2, 3]
    heap_sort(a)
    print(a)

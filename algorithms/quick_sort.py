"""
Quick Sort (Randomized Pivot)
=============================
Recurrence: T(n) = 2T(n/2) + Theta(n) expected | T(n - 1) + Theta(n) worst-case
Time Complexity: O(n log n) average, O(n^2) worst-case
Space Complexity: O(log n) recursion stack
Stability: Unstable
In-Place: Yes (excluding recursion stack)
"""

import random


def partition(arr: list(int), low: int, high: int) -> int:
    """
    Pick a random pivot, store it at the end.
    Stack the values smaller than the pivot up front.
    Place the pivot at its right index, then return the inex.
    """
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr: list[int], low: int = 0, high: int | None = None):
    if high == None:
        high = len(arr) - 1

    # Base case: 0 or 1 element
    if low < high:
        # Divide
        pivot_idx = partition(arr, low, high)

        # Conquer
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

    return arr


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print(quick_sort(data))

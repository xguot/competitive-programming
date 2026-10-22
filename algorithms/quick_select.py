"""
Quick Select (Randomized Pivot)
===============================
Recurrence: T(n) = T(n/2) + Theta(n) expected | T(n -1) + Theta(n) worst-case
Time Complexity: O(n) average, O(n^2) worst-case
Space Complexity: O(log n) recursion stack
"""

import random


def partition(arr: list[int], low: int, high: int) -> int:
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


def quick_select(
        arr: list[int],
        idx: int,
        low: int = 0,
        high: int | None = None) -> int:
    """
    Quick select find the value of a particular index.
    Leveraging the fact that after parition pivot is at its correct spot.
    """
    if high is None:
        high = len(arr) - 1

    # Base case
    if not (0 <= idx < len(arr)):
        raise IndexError("Index out of bounds")

    # Divide
    pivot_idx = partition(arr, low, high)

    # Conquer
    if idx < pivot_idx:
        return quick_select(arr, idx, low, pivot_idx - 1)
    elif idx > pivot_idx:
        return quick_select(arr, idx, pivot_idx + 1, high)
    else:
        return arr[idx]


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print(quick_select(data, 4))
    print(quick_select(data, 0))

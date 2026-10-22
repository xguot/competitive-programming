"""
Median of Medians (Deterministic Selection)
===========================================
Recurrence: T(n) <= T(n/5) + T(7n/10) + O(n)
Time Complexity: O(n) strict worst-case
Space Complexity: O(n)
"""

def median_of_medians(arr: list[int], k: int) -> int:
    """Returns the k-th smallest element."""
    # Base case
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide
    chunks = [arr[i : i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Conquer 1: find the true median of the medians to use as pivot
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition (at leat 30% discarded)
    lows = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]

    # Conquer 2: prune and recurse on the side containing index k
    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))


if __name__ == "__main__":
    nums = [12, 3, 5, 7, 4, 19, 26, 1, 9, 15, 8, 2]
    print(median_of_medians(nums, 5))  # 7

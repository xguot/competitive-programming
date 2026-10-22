"""
Maximum Subarray Sum (Divde & Conquer)
======================================
Recurrence: T(n) = 2T(n/2) + O(n)
Time Complexity: O(n log n)
Space Complexity: O(log n) recursion stack
"""

def max_crossing_sum(arr: list[int], low: int, mid: int, high: int) -> int:
    """Finds the maximum sum of a subarray that crosses the midpoint."""
    left_sum = -float("inf")
    curr = 0
    for i in range(mid, low - 1, -1):
        curr += arr[i]
        left_sum = max(left_sum, curr)

    right_sum = -float("inf")
    curr = 0
    for i in range(mid + 1, high + 1):
        curr += arr[i]
        right_sum = max(right_sum, curr)

    return int(left_sum + right_sum)


def max_subarray_sum(arr: list[int], low: int = 0, high: int | None = None) -> int:
    if high is None:
        high = len(arr) - 1

    # Base case
    if low == high:
        return arr[low]

    #Divide
    mid = (low + high) // 2

    # Conquer & Combine
    return max(
        max_subarray_sum(arr, low, mid),
        max_subarray_sum(arr, mid + 1, high),
        max_crossing_sum(arr, low, mid, high),
    )


if __name__ == "__main__":
    data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(data))  # 6 (from [4, -1, 2, 1])

"""
Merge Sort
==========
Recurrence: T(n) = 2T(n/2) + Theta(n)
Time Complexity: O(n log n) worst, average, and best case
Space Complexity: O(n)
Stability: Stable
In-Place: No
"""

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr: list[int]) -> list[int]:
    # Base case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    # Conquer
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combine
    return merge(left, right)

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(data))

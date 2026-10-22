"""
Closest Pair of Points in 2D
============================
Recurrence: 2T(n/2) + Theta(n)
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import math

Point = tuple[float, float]


def dist(p1: Point, p2: Point) -> float:
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def brute_force(points: list[Point]) -> float:
    min_d = float("inf")
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            min_d = min(min_d, dist(points[i], points[j]))
    return min_d


def strip_closest(strip: list[Point], d: float) -> float:
    """
    Checks points across the dividing line in O(n) time.
    By the 16-box packing lemma (4x4 grid of d/2 x d/2 squares),
    each point only needs to be compared against the next 15 points
    in the y-sorted strip.
    """
    min_d = d
    n = len(strip)
    for i in range(n):
        for j in range(i+1, min(i + 16, n)):
            min_d = min(min_d, dist(strip[i], strip[j]))
    return min_d


def _closest_rec(px: list[Point], py: list[Point]) -> float:
    # Base case
    if len(px) <= 3:
        return brute_force(px)

    # Divide
    mid = len(px) // 2
    mid_point = px[mid]

    left_set = set(px[:mid])
    py_left = [p for p in py if p in left_set]
    py_right = [p for p in py if p not in left_set]

    # Conquer
    d_left = _closest_rec(px[:mid], py_left)
    d_right = _closest_rec(px[mid:], py_right)
    d = min(d_left, d_right)

    # Combine
    strip = [p for p in px if abs(p[0] - mid_point[0]) < d]
    return min(d, strip_closest(strip, d))


def closest_pair(points: list[Point]) -> float:
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return _closest_rec(px, py)


if __name__ == "__main__":
    pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"{closest_pair(pts):.4f}")  # 1.4142

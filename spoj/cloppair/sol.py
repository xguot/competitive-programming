import sys
import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair_rec(Px, Py):
    n = len(Px)

    # Base case
    if n <= 3:
        min_d = float('inf')
        best_pair = (-1, -1)
        for i in range(n):
            for j in range(i+1, n):
                d = dist(Px[i], Px[j])
                if d < min_d:
                    min_d = d
                    best_pair = (Px[i][2], Px[j][2])
        return min_d, best_pair

    # Divide
    mid = n // 2
    mid_x = Px[mid][0]

    # Set for O(1) lookups
    left_indices = set(p[2] for p in Px[:mid])

    # O(n) linear scan for partition
    Pyl = []
    Pyr = []
    for p in Py:
        if p[2] in left_indices:
            Pyl.append(p)
        else:
            Pyr.append(p)

    # Conquer
    dl, pair_l = closest_pair_rec(Px[:mid], Pyl)
    dr, pair_r = closest_pair_rec(Px[mid:], Pyr)

    if dl < dr:
        min_d, best_pair = dl, pair_l
    else:
        min_d, best_pair = dr, pair_r

    # Combine
    strip = [p for p in Py if abs(p[0] - mid_x) < min_d]

    strip_len = len(strip)
    for i in range(strip_len):
        # A 2d x d search grids holds a max of 8 points.
        # Current occupies 1, leaving 7 ahead to check
        for j in range(i+1, min(i+8, strip_len)):
            if strip[j][1] - strip[i][1] >= min_d:
                break

            d = dist(strip[i], strip[j])
            if d < min_d:
                min_d = d
                best_pair = (strip[i][2], strip[j][2])

    return min_d, best_pair


def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])

    # (x, y, i)
    points = [(int(data[2 * i + 1]), int(data[2 * i + 2]), i) for i in range(n)]

    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])

    min_d, best_pair = closest_pair_rec(Px, Py)

    idx1, idx2 = best_pair
    a, b = min(idx1, idx2), max(idx1, idx2)

    print(f"{a} {b} {min_d:.6f}")

if __name__ == '__main__':
    solve()

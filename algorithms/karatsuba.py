"""
Karatsuba Fast Integer Multiplication
=====================================
Recurrence: T(n) = 3T(n/2) + Theta(n)
Time Complexity: O(n^{log_2(3)}) ~= O(n^{1.585})
Space Complexity: O(n)
"""

def karatsuba(x: int, y: int) -> int:
    # Base case
    if x < 10 or y < 10:
        return x * y

    # Divide
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    base = 10**m

    x_high, x_low = divmod(x, base)
    y_high, y_low = divmod(y, base)

    # Conquer: 3 recursive multiplication instead of 4
    z0 = karatsuba(x_low, y_low)
    z2 = karatsuba(x_high, y_high)
    z1 = karatsuba(x_low + x_high, y_low + y_high) - z0 - z2

    # Combine: x*y = z2 * 10^{2m} + z1 * 10^m + z0
    return (z2 * 10**(2*m) + z1 * 10**m + z0)


if __name__ == "__main__":
    a, b = 12345678, 87654321
    assert karatsuba(a, b) == a * b
    print(karatsuba(a, b))

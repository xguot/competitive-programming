"""
Strassen's Matrix Multiplication
================================
Recurrence: T(n) = 7T(n/2) + O(n^2)
Time Complexity: O(n^{log_2(7)}) ~= O(n^{2.81})
Space Complexity: O(n^2)
"""

Matrix = list[list[int]]


def add(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def sub(A: Matrix, B: Matrix) -> Matrix:
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def split(M: Matrix) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    mid = len(M) // 2
    a11 = [row[:mid] for row in M[:mid]]
    a12 = [row[mid:] for row in M[:mid]]
    a21 = [row[:mid] for row in M[mid:]]
    a22 = [row[mid:] for row in M[mid:]]
    return a11, a12, a21, a22


def strassen(A: Matrix, B: Matrix) -> Matrix:
    # Base case: 1x1 matrix
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide
    a11, a12, a21, a22 = split(A)
    b11, b12, b21, b22 = split(B)

    # Conquer: 7 recursive calles in stead of 8
    m1 = strassen(add(a11, a22), add(b11, b22))
    m2 = strassen(add(a21, a22), b11)
    m3 = strassen(a11, sub(b12, b22))
    m4 = strassen(a22, sub(b21, b11))
    m5 = strassen(add(a11, a12), b22)
    m6 = strassen(sub(a21, a11), add(b11, b12))
    m7 = strassen(sub(a12, a22), add(b21, b22))

    # Combine
    c11 = add(sub(add(m1, m4), m5), m7)
    c12 = add(m3, m5)
    c21 = add(m2, m4)
    c22 = add(sub(add(m1, m3), m2), m6)

    top = [c11[i] + c12[i] for i in range(len(c11))]
    bot = [c21[i] + c22[i] for i in range(len(c21))]
    return top + bot


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print(strassen(A, B))

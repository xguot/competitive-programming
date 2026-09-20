import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    names = data[1:]

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    graph = {c: [] for c in alphabet}
    in_degree = {c: 0 for c in alphabet}

    # Populate the graph
    for i in range(n - 1):
        w1, w2 = names[i], names[i+1]
        found_mismatch = False
        min_len = min(len(w1), len(w2))

        for j in range(min_len):
            if w1[j] != w2[j]:
                u, v = w1[j], w2[j]
                graph[u].append(v)
                in_degree[v] += 1
                found_mismatch = True
                break

        # w2 is prefix of w1
        if not found_mismatch and len(w1) > len(w2):
            print("Impossible")
            return

    # Kahn's algorithm
    # Find topological sort by repetitively removing node with zero
    # dependencies.
    q = deque([c for c in alphabet if in_degree[c] == 0])
    res = []

    while q:
        u = q.popleft()
        res.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(res) == 26:
        print("".join(res))
    else:
        print("Impossible")

if __name__ == "__main__":
    solve()

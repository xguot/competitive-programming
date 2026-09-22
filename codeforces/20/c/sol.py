import sys
import heapq

def solve():
    data = sys.stdin.read().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        graph[u].append((v, w))
        graph[v].append((u, w)) # Undirected

    distances = [float('inf')] * (n+1)
    done = [False] * (n+1)
    parent = [-1] * (n+1)

    src = 1
    pq = []

    heapq.heappush(pq, (0, src))
    distances[src] = 0

    while pq:
        curr_dist, curr = heapq.heappop(pq)

        if done[curr]:
            continue

        done[curr] = True

        if curr == n:
            break

        for v, w in graph[curr]:
            if not done[v]:
                # Edge relaxation
                new_dist = curr_dist + w
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    parent[v] = curr
                    heapq.heappush(pq, (new_dist, v))

    # Output
    if distances[n] == float('inf'):
        print('-1')
    else:
        path = []
        curr = n
        while curr != -1:
            path.append(curr)
            curr = parent[curr]

        print(*(path[::-1]))


if __name__ == '__main__':
    solve()

import heapq
import sys
input = sys.stdin.readline

def dijkstra(i):
    heap = []
    heapq.heappush(heap, (0, i))
    dist = [inf] * (V+1)
    while heap:
        w, n = heapq.heappop(heap)

        if dist[n] < w:
            continue

        dist[n] = w

        if n == P and i == V:
            break

        for new_n, new_w in arr[n]:
            if dist[new_n] > new_w + w:
                dist[new_n] = new_w + w
                heapq.heappush(heap, (new_w + w, new_n))
    return dist

V, E, P = map(int, input().split())

arr = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

inf = float("inf")

dist1 = dijkstra(1)
distV = dijkstra(V)

if dist1[P] + distV[P] == dist1[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
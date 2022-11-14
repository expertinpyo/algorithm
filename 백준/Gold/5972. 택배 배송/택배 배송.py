import heapq
def dijkstra(i):
    heap = [(0, i)]
    while heap:
        w, n = heapq.heappop(heap)
        if dist[n] < w:
            continue
        for new_n, new_w in arr[n]:
            if new_w + w < dist[new_n]:
                dist[new_n] = new_w + w
                heapq.heappush(heap, (new_w + w, new_n))

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
inf = float("inf")
heap = []
ans = 0
dist = [inf] * (N + 1)
dijkstra(1)
print(dist[N])
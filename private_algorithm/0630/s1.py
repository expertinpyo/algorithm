import heapq
def dijkstra(x):
    heap = []
    heapq.heappush(heap, (0, x))
    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[node] = weight
            for new_n, new_w in arr[x]:
                if not visited[new_n]:
                    heapq.heappush(heap, (new_w + weight, new_n))

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
arr = [[] for _ in range(n+1)]
for _ in range(r):
    start, end, weight = map(int, input().split())
    arr[start].append([end, weight])
    arr[end].append([start, weight])
inf = float("inf")
ans = 0
for i in range(1, n+1):
    cnt = 0
    visited = [0] * (n+1)
    dist = [inf] * (n + 1)
    dijkstra(i)
    for j in range(1, n+1):
        if dist[j] != inf and dist[j] <= m:
            cnt += items[j-1]
    ans = max(ans, cnt)
print(ans)

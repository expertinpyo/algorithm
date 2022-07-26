import heapq
import sys
input = sys.stdin.readline

def dijkstra(x):
    heap = [(0, x)]
    while heap:
        weight, node = heapq.heappop(heap)
        if weight > m:
            return
        if not visited[node]:
            visited[node] = 1
            for new_n, new_w in arr[node]:
                if not visited[new_n]:
                    heapq.heappush(heap, (new_w+weight, new_n))


n, m, r = map(int, input().split())
items = list(map(int, input().split()))
arr = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

ans = 0
inf = float('inf')
for i in range(1, n+1):
    visited = [0] * (n+1)
    dijkstra(i)
    cnt = 0
    for j in range(1, n+1):
        if visited[j]:
            cnt += items[j-1]
    ans = max(cnt, ans)
print(ans)
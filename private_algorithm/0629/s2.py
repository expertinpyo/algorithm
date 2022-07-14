import heapq

def dijkstra(x):
    heap = []
    heapq.heappush(heap, (0, x))
    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[x-1][node-1] = weight
            for new_n, new_w in arr[node]:
                if not visited[new_n]:
                    heapq.heappush(heap, (weight+new_w, new_n))

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, rate = map(int, input().split())
    arr[start].append((end, rate))

dist = [[0] * n for _ in range(n)]
for i in range(n):
    visited = [0] * (n+1)
    dijkstra(i+1)
for di in dist:
    for d in di:
        print(d, end=' ')
    print('')
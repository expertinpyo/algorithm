# dijkstra 연습
import heapq
import sys
sys.stdin = open('input.txt')

def dijkstra():
    global ans
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            p[node] = weight
            for n, w in graph[node]:
                if not visited[n]:
                    heapq.heappush(heap, (p[node] + w, n))

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for i in range(e):
    start, end, W = map(int, input().split())
    graph[start].append([end, W])
    graph[end].append([start, W])

p = [10**6] * (v+1)
p[0] = 0
visited = [0] * (v+1)
dijkstra()
print(p)
# v개의 정점
# e개의 간선
# 1부터 v까지 번호 매겨짐
# 시작 정점의 k
# 최단 경로의 경로값을 출력한다.
import heapq
import sys
input = sys.stdin.readline


# i번째 줄에 i번 정점으로의 최단 경로의 경로값 출력

def dijkstra(x):
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[node] = weight
            for nn, ww in group[node]:
                if not visited[nn]:
                    heapq.heappush(heap, (dist[node] + ww, nn))


v, e = map(int, input().split())
k = int(input())
group = [[] for _ in range(v+1)]
for _ in range(e):
    u, vv, w = map(int, input().split())
    group[u].append([vv, w])
visited = [0] * (v+1)
dist = [10**6] * (v+1)
dijkstra(k)
for i in range(1, v+1):
    if dist[i] != 10**6:
        print(dist[i])
    else:
        print('INF')
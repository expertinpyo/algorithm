# prim heap으로 구현하기

import sys
import heapq
sys.stdin = open('input.txt')

def prim():
    global ans
    heap = []
    heapq.heappush(heap, (0, 0)) # 가중치, 노드번호 순

    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            ans += weight
            for n, w in graph[node]:
                if not visited[n]:
                    heapq.heappush(heap, (w, n))


v, e = map(int, input().split())    # v : 노드 수, e : 간선 수
graph = [[] for _ in range(v+1)]
for _ in range(e):
    start, end, w = map(int, input().split())
    graph[start].append([end, w])
    graph[end].append([start, w])

ans = 0
visited = [0] * (v+1)
prim()
print(ans)
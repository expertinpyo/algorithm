# 출력 i번째 줄에 i번 정점으로의 최단 경로의 경로 값을 출력
# 시작점 자신은 0으로 출력, 경로가 없을 시에는 INF로 출력
import heapq
import sys

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, k)) # 가중치, 노드 번호

    while heap: # heap이 비어있지 않다면
        w, node = heapq.heappop(heap)
        if not visited[node]:  # 방문한 적이 없다면
            visited[node] = 1
            p[node] = w
            if p[node] == INF:
                print('INF')
            else:
                print(p[node])
            for i in range(1, v+1):
                if not visited[i]:
                    heapq.heappush(heap, (p[node]+group[node][i], i))

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
k = int(input())
group = [[INF]*(v+1) for _ in range(v+1)]
for _ in range(e):
    start, end, W = map(int, input().split())
    group[start][end] = W


p = [INF] * (v+1)
p[0] = 0
visited = [0] * (v+1)
dijkstra()
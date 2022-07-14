import sys
import heapq
sys.stdin = open('input.txt')

def dijkstra():
    heap = []
    heapq.heappush(heap, (0,0)) # 값(가중치) / 노드 번호(정점)

    while heap:
        am, num = heapq.heappop(heap)
        if not visited[num]:
            visited[num] = 1
            dist[num] = am
            for i in range(n+1):
                if not visited[i]:
                    heapq.heappush(heap, (dist[num]+g[num][i], i))
    return dist[n]

T = int(input())
for tc in range(1, T+1):
    n, e = map(int, input().split())
    g = [[10**6] * (n+1) for _ in range(n+1)]
    dist = [10**6] * (n+1)
    visited = [0] * (n+1)
    for _ in range(e):
        start, end, amount = map(int, input().split())
        g[start][end] = amount
    print(f"#{tc} {dijkstra()}")
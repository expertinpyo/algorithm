# dijkstra
# 최소 문제
import heapq
import sys
sys.stdin = open('input.txt')

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while heapq:
        weight, x, y = heapq.heappop(heap)

        if not visited[x][y]:
            visited[x][y] = 1
            dist[x][y] = weight
            if x == n-1 and y == n-1:
                return
            for d in di:
                nx, ny = x + d[1], y + d[0]
                if 0 <= nx < n and 0 <= ny < n:
                    cost = 1
                    if arr[nx][ny] > arr[x][y]:
                        cost += arr[nx][ny] - arr[x][y]
                    if not visited[nx][ny]:
                        heapq.heappush(heap, (cost+weight, nx, ny))


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[10**6] * n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    dijkstra()
    print(f"#{tc} {dist[-1][-1]}")
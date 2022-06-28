import sys
import heapq

sys.stdin = open('input.txt')

def dikstra():
    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            p[node] = weight
            for i in range(n+1):
                if not visited[i]:
                    heapq.heappush(heap, (p[node]+g[node][i], i))


di = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 동 남 서 북
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    nodes = [[10**6] * 4 for _ in range(n*n+1)]
    num = 1
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni, nj = i+di[k][1], j+di[k][0]
                if 0 <= ni < n and 0 <= nj < n:
                    nodes[num][k] = 1 + abs(arr[i][j] - arr[ni][nj])
            num += 1
    visited = [0] * (n+1)
    p = [10**6] * (n+1)
    # print(f"#{tc} {dijkstra()}")
    print(nodes)
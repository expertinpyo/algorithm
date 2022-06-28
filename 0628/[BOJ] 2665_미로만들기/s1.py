import heapq
def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while heap:
        weight, x, y = heapq.heappop(heap)
        if not visited[x][y]:
            visited[x][y] = 1
            dist[x][y] = weight
            for d in di:
                nx, ny = d[1] + x, d[0] + y
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if arr[nx][ny] == '1':
                        new_w = 0
                    else:
                        new_w = 1
                    heapq.heappush(heap, (weight+new_w, nx, ny))

n = int(input())
arr = [list(input()) for _ in range(n)]

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[0] * n for _ in range(n)]
inf = float('inf')
dist = [[inf] * n for _ in range(n)]
dijkstra()
print(dist[-1][-1])
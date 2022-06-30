from sys import stdin
import heapq

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while heap:
        weight, x, y = heapq.heappop(heap)
        if x == n-1 and y == m-1:
            print(weight)
            break
        for d in di:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if arr[nx][ny]:
                    heapq.heappush(heap, (weight+1, nx, ny))
                else:
                    heapq.heappush(heap, (weight, nx, ny))


m, n = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
dijkstra()
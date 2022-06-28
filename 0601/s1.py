# 1261 알고스팟
# 벽을 부순다는 것이 일종의 가중치 역할을 하는 것 같다
# 시간 초과 발생, 아마도 모든 방향의 가지수를 다 고려해서 그렇지 않을까 하는 생각이 있다
# 최소 가중치를 찾는 문제임
# 각 점에서 이동 가능한 방향은 총 네 곳.
# 현재 풀이한 방법은 프림에 가깝다
# 최단거리 문제가 아니다, 최소로 벽을 부수는 것이 문제이다
# 벽을 부수는 횟수가 가중치가 되는 문제
# 따라서,


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
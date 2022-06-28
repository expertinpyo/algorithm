# 살아있는 꽃의 최댓값을 찾는다
# 날짜가 여러개라면 가장 빠른 날짜를 출력한다
from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        visited[x][y] -= 1
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + arr[nx][ny]
                queue.append([nx, ny])


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    x, y = map(int, input().split()) # 시작점, 이 곳의 비옥함은 0보다 큼
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = arr[x][y]
    # bfs로 해결하면 좋을 것 같음, 같은 날에 여러개로 뻗어 나가므로
    bfs(x, y)
    print(visited)
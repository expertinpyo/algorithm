# mst로 풀면 더 좋지 않을까?
# bfs로 각 지점마다의 경로 길이를 구하고
# 그 경로대비 최종 거리를 구한다면 좋지 않을까 싶다.

from collections import deque

di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    arr = []
    destinations = []
    for _ in range(h):
        ipv = list(input())
        arr.append(ipv)
        if 'o' in ipv:
            start = (_, ipv.index('o')) # 시작점
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                destinations.append((i, j))
    completed = []
    ans = 0
    while len(completed) != len(destinations):
        visited = [[-1]*w for _ in range(h)]
        visited[start[0]][start[1]] = 0
        bfs(start)
        mins = float('inf')
        target = ''
        for des in destinations:
            if des not in completed:
                mins = min(visited[des[0]][des[1]], mins)
                if mins == visited[des[0]][des[1]]:
                    target = des
        if mins == -1:
            ans = -1
            break
        completed.append(target)
        start = target
        ans += mins
    print(ans)
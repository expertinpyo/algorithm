from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx = x + d[1]
            ny = y + d[0]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] not in al_li:
                    al_li.append(arr[nx][ny])
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


r, c = map(int, input().split())
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
arr = [list(input()) for _ in range(r)]
alphabet = [0 for _ in range(26)]

for i in range(r):
    for j in range(c):
        alphabet[ord(arr[i][j])-65] += 1
if max(alphabet) == 1:
    ans = r * c
else:
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    al_li = deque()
    al_li.append(arr[0][0])
    bfs(0, 0)
    print(visited)

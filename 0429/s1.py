# 초기 뱀 길이 1
# 상하좌우에 벽 존재
# 처음에 오른쪽을 향함
from sys import setrecursionlimit
from collections import deque
setrecursionlimit(10**6)
def snake(x, y, dit):
    global cnt, finished, queue

    if not arr[x][y]:
        arr[x][y] = 1
    if cnt in time:
        idx = time.index(cnt)
        d = directions[idx]
        if d == 1:
            if dit < 3:
                dit += 1
            else:
                dit = 0
        else:
            if dit > 0:
                dit -= 1
            else:
                dit = 3
    nx, ny = x + di[dit][1], y + di[dit][0]
    if 0 <= nx < n and 0 <= ny < n and [nx, ny] not in queue:
        if arr[nx][ny] > 0:
            cnt += 1
            finished = True
            return
        else:
            if not arr[nx][ny]:
                arr[nx][ny] = 1
                ds = queue.pop()
                arr[ds[0]][ds[1]] = 0
                queue.appendleft([nx, ny])
                cnt += 1
                snake(nx, ny, dit)
            else: # 사과를 먹었다.
                arr[nx][ny] = 1
                queue.appendleft([nx, ny])
                cnt += 1
                snake(nx, ny, dit)
    else:
        finished = True
        cnt += 1
        return

    if finished:
        return


di = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 방향
n = int(input())    # 보드 크기
k = int(input())    # 사과 개수
arr = [[0] * n for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = -100

l = int(input())    # 뱀의 방향 전환 횟수
time = []
directions = []
for i in range(l):
    sec, direction = input().split()
    if direction == 'D':
        direction = 1
    else:
        direction = 2
    time.append(int(sec))
    directions.append(direction)

finished = False
cnt = 0
queue = deque()
queue.append([0, 0])
snake(0, 0, 0)
print(cnt)


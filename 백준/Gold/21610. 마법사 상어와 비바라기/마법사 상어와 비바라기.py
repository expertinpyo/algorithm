from collections import deque
di = [0, [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int,input().split())) for _ in range(M)]

queue = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])
for d, s in move:
    cloud = set()
    while queue:
        x, y = queue.popleft()
        nx, ny = (x + di[d][0] * s) % N, (y + di[d][1] * s) % N
        cloud.add((nx, ny))
        arr[nx][ny] += 1

    for x, y in cloud:
        for i in range(2, 9, 2):
            nx, ny = x + di[i][0], y + di[i][1]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]:
                arr[x][y] += 1


    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in cloud:
                queue.append([i, j])
                arr[i][j] -= 2
ans = 0
for i in range(N):
    ans += sum(arr[i])
print(ans)
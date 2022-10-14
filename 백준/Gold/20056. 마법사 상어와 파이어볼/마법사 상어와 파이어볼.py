N, M, K = map(int, input().split())
balls = [list(map(int, input().split())) for _ in range(M)]
for ball in balls:
    ball[0] -= 1
    ball[1] -= 1
di = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
for _ in range(K):
    arr = [[[] for _ in range(N)] for _ in range(N)]
    for ball in balls:
        x, y, m, v, d = ball
        dx, dy = v*di[d][0], v*di[d][1]
        nx, ny = (x+dx) % N, (y+dy) % N
        ball[0] = nx
        ball[1] = ny
        arr[nx][ny].append(ball)
    balls.clear()
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) >= 2:
                tm = tv = 0
                odd = even = False
                for ball in arr[i][j]:
                    tm += ball[2]
                    tv += ball[3]
                    if ball[4] % 2:
                        odd = True
                    else:
                        even = True
                if int(tm / 5):
                    if odd and even:
                        direction = [1, 3, 5, 7]
                    else:
                        direction = [0, 2, 4,6]
                    for k in range(4):
                        balls.append([i, j, int(tm/5), int(tv/len(arr[i][j])), direction[k]])
            elif len(arr[i][j]) == 1:
                balls.append(arr[i][j][0])
ans = 0
if balls:
    for ball in balls:
        ans += ball[2]
print(ans)

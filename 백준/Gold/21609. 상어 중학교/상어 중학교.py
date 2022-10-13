from collections import deque
def bfs(a, b):
    queue = deque([(a, b)])
    check = [(a, b)]
    zero = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] in [0, arr[a][b]]:
                visited[nx][ny] = 1
                check.append((nx, ny))
                queue.append((nx, ny))
                cnt += 1
                if arr[nx][ny] == 0:
                    zero += 1
    check.sort(key=lambda x : (x[0], x[1]))
    if cnt >= 2:
        for i in range(len(check)):
            x, y = check[i]
            if arr[x][y] > 0:
                rep = (x, y)
                break
        groups.append((cnt, zero, rep, check))  # 전체 개수 / 무지개 개수 / 기준 블록 좌표 / 모든 좌표

def gravity(ar):
    for j in range(N):
        idx = N-1
        while idx > 0:
            if ar[idx][j] == '':
                for i in range(idx-1, -1, -1):
                    if ar[i][j] != '':
                        if ar[i][j] == -1:
                            idx = i - 1
                        else:
                            ar[idx][j] = ar[i][j]
                            ar[i][j] = ''
                            idx -= 1
                        break
                else:
                    break
            else:
                idx -= 1
    return ar


def rotate(ar):
    rotated_tuples = list(zip(*ar))
    new_ar = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_ar[N-1-i][j] = rotated_tuples[i][j]

    return new_ar


N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
while True:
    raindow = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                raindow.append((i, j))

    groups = []
    visited = [[0] * N for _ in range(N)]
    # 1. 크기가 가장 큰 블록 찾기
    for i in range(N):
        for j in range(N):
            if type(arr[i][j]) == int and arr[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                bfs(i, j)
                for rx, ry in raindow:
                    if visited[rx][ry]:
                        visited[rx][ry] = 0
    if groups:
        groups.sort(key=lambda x:(x[0], x[1], x[2][0], x[2][1]), reverse=True) # 정렬
    else:
        print(ans)
        break
    group = groups[0]
    # 모든 블록 제거 후 점수 획득
    ans += group[0] ** 2
    for gx, gy in group[3]:
        arr[gx][gy] = ''

    # 격자에 중력 작용
    arr = gravity(arr)
    arr = rotate(arr)
    arr = gravity(arr)

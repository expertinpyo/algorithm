import copy

def watch(cctv, view):
    global ans
    if not cctv:
        A = 0
        for i in view:
            A += i.count(0)
        for i in R:
            A -= i.count(6)
        ans = min(ans, A)
        return
    ci, cj = cctv.pop()
    view[ci][cj] = 1
    cctv_n = copy.deepcopy(cctv)
    view_n = copy.deepcopy(view)
    if R[ci][cj] == 1:
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            while 0 <= ni < N and 0 <= nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
            watch(cctv_n, view_n)
            cctv_n = copy.deepcopy(cctv)
            view_n = copy.deepcopy(view)
    if R[ci][cj] == 2:
        for di, dj in ((1, 0), (0, 1)):
            ni, nj = ci+di, cj+dj
            while ni < N and nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
            ni, nj = ci - di, cj - dj
            while 0 <= ni and 0 <= nj:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni -= di
                    nj -= dj
                else:
                    break
            watch(cctv_n, view_n)
            cctv_n = copy.deepcopy(cctv)
            view_n = copy.deepcopy(view)
    if R[ci][cj] == 3:
        for i in range(4):
            di, dj = delta[i][0], delta[i][1]
            ni, nj = ci+di, cj+dj
            while 0 <= ni < N and 0 <= nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
            di, dj = delta[(i+1)%4][0], delta[(i+1)%4][1]
            ni, nj = ci + di, cj + dj
            while 0 <= ni < N and 0 <= nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
            watch(cctv_n, view_n)
            cctv_n = copy.deepcopy(cctv)
            view_n = copy.deepcopy(view)
    if R[ci][cj] == 4:
        for i in range(4):
            di, dj = delta[(i + 1) % 4][0], delta[(i + 1) % 4][1]
            ni, nj = ci + di, cj + dj
            while 0 <= ni < N and 0 <= nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
            di, dj = delta[(i + 2) % 4][0], delta[(i + 2) % 4][1]
            ni, nj = ci + di, cj + dj
            while 0 <= ni < N and 0 <= nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
            di, dj = delta[(i + 3) % 4][0], delta[(i + 3) % 4][1]
            ni, nj = ci + di, cj + dj
            while 0 <= ni < N and 0 <= nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
            watch(cctv_n, view_n)
            cctv_n = copy.deepcopy(cctv)
            view_n = copy.deepcopy(view)
    if R[ci][cj] == 5:
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            while 0 <= ni < N and 0 <= nj < M:
                if R[ni][nj] != 6:
                    view_n[ni][nj] = 1
                    ni += di
                    nj += dj
                else:
                    break
        watch(cctv_n, view_n)

N, M = map(int, input().split())
R = [list(map(int, input().split())) for _ in range(N)]
V = [[0]*M for _ in range(N)]
ans = N * M
delta = ((1, 0), (0, -1), (-1, 0), (0, 1))

C = []
for i in range(N):
    for j in range(M):
        if R[i][j] in (1, 2, 3, 4, 5):
            C += [(i, j)]
watch(C, V)
print(ans)
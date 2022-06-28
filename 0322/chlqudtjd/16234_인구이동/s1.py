import sys
sys.stdin = open('input.txt')

# def move(n):
#     flag = 0
#     for i in range(N):
#         if flag:
#             break
#         for j in range(N):
#             if i+1 < N and L <= abs(A[i][j] - A[i+1][j]) <= R:
#                 flag = 1
#                 break
#             if j+1 < N and L <= abs(A[i][j] - A[i][j+1]) <= R:
#                 flag = 1
#                 break
#     if not flag:
#         return n-1
#     V = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             S = []
#             if not V[i][j]:
#                 S += [(i, j)]
#                 V[i][j] = 1
#                 Q = [(i, j)]
#                 while Q:
#                     ci, cj = Q.pop(0)
#                     for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#                         ni, nj = ci+di, cj+dj
#                         if 0<=ni<N and 0<=nj<N and not V[ni][nj] and L <= abs(A[ci][cj] - A[ni][nj]) <= R:
#                             Q.append((ni, nj))
#                             V[ni][nj] = 1
#                             S += [(ni, nj)]
#                 avg = 0
#                 for mi, mj in S:
#                     avg += A[mi][mj]
#                 avg //= len(S)
#                 for mi, mj in S:
#                     A[mi][mj] = avg
#     return move(n+1)

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    ans += 1
    flag = 0
    for i in range(N):
        if flag:
            break
        for j in range(N):
            if i+1 < N and L <= abs(A[i][j] - A[i+1][j]) <= R:
                flag = 1
                break
            if j+1 < N and L <= abs(A[i][j] - A[i][j+1]) <= R:
                flag = 1
                break
    if not flag:
        break
    V = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not V[i][j]:
                S = [(i, j)]
                V[i][j] = 1
                Q = [(i, j)]
                while Q:
                    ci, cj = Q.pop(0)
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and not V[ni][nj] and L <= abs(A[ci][cj] - A[ni][nj]) <= R:
                            Q.append((ni, nj))
                            V[ni][nj] = 1
                            S += [(ni, nj)]
                if len(S) != 1:
                    avg = 0
                    for mi, mj in S:
                        avg += A[mi][mj]
                    avg //= len(S)
                    for mi, mj in S:
                        A[mi][mj] = avg

print(ans-1)
N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
checks = [
    [[0, 1], [0, 2], [0, 3]], # 일자
    [[1, 0], [2, 0], [3, 0]], # 일자 세로
    [[1, 0], [0, 1], [1, 1]], # 사각형
    [[1, 0], [2, 0], [2, 1]], # ㄴ자
    [[0, 1], [0, 2], [-1, 2]],
    [[-1, 0], [-2, 0], [-2, -1]],
    [[0, -2], [0, -1], [1, -2]],
    [[1, 0], [2, 0], [2, -1]], # ㄴ자 뒤집은 것
    [[0, 1], [0, 2], [1, 2]],
    [[-1, 0], [-2, 0], [-2, 1]],
    [[0, -2], [0, -1], [-1, -2]],
    [[1, 0], [1, 1], [2, 1]], # 번개모양
    [[1, 0], [1, -1], [2, -1]],
    [[0, 1], [-1, 1], [-1, 2]], # 이게 좀 이상
    [[0, 1],[1, 1],[1, 2]],
    [[0, 1], [0, 2], [1, 1]],  # ㅜ자
    [[1, 0], [1, 1], [2, 0]],
    [[0, 1], [-1, 1], [0, 2]],
    [[1, 0], [1, -1], [2, 0]]
]

for check in checks:
    for i in range(N):
        for j in range(M):
            possible = True
            cnt = arr[i][j]
            for k in range(3):
                ni, nj = i + check[k][0], j + check[k][1]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
                    continue
                else:
                    possible = False
                    break
            if possible:
                ans = max(ans, cnt)
print(ans)
c, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
cheese_cnt = 0
for ar in arr:
    cheese_cnt += ar.sum()
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

while cheese_cnt:
    melt = [[0] * c for _ in range(r)]
    melt_cnt = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                for d in di:
                    ni, nj = d[1] + i, d[0] + j
                    if 0 <= ni < r and 0 <= nj < c and not arr[ni][nj]:
                        melt[ni][nj] = 1
                        melt_cnt += 1
                        break
    # 녹는 점 확인
    if melt_cnt == cheese_cnt:
        
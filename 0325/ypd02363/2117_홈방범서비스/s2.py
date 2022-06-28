# 4 방향 최대 점들을 구하고
# 그 점들 사이의 값들을 y = x, y = -x 로 다 갱신
# 그 후 재귀적으로 나머지 점들 채움
# 그리고 각 점 마다 위의 범위 안에서 몇 개나 채울 수 있는지 확인하기

import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    aaa = []
    for k in range(1, n//2+2):
        cost = k**2 + (k-1)**2
        house = cost / m
        cnt = 0
        kk = k-1
        if kk:
            for a in range(len(where_to_visit)):
                nx, ny = where_to_visit[a][0], where_to_visit[a][1]
                if (ny + kk >= nx) and (-ny + kk  >= nx) and (ny - kk <= nx) and (-ny -kk <= nx):
                    cnt += 1
        else:
            cnt = 1
        if cnt >= house:
            aaa.append(cnt)
    if aaa:
        return max(aaa)
    return 0

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    where_to_visit = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                where_to_visit.append([i,j])
    ans_list = []
    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                ans_list.append(dfs(i, j))
    # for i in range(len(where_to_visit)):
    #     ans_list.append(dfs(where_to_visit[i][0], where_to_visit[i][1]))
    # print(ans_list)
    print(f"#{tc} {max(ans_list)}")
    # print(where_to_visit)
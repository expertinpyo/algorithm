# 도시의 치킨 거리 = 모든 치킨 거리의 합
# 치킨 거리 : 가장 가까운 치킨집 사이의 거리
# 가장 수익을 많이 낼 수 있는 치킨집의 개수는 M개
# M개의 치킨집 수를 구하고 도시의 치킨 거리를 최소화 시키기
from itertools import combinations as cb

def chicken(hlist, clist):
    ans = 0
    for x, y in hlist:
        dis = 10**6
        for i in range(m):
            nx, ny = clist[i]
            dis = min((abs(nx-x) + abs(ny-y)), dis)
        ans += dis
    return ans

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 집의 최대 개수 2 * n
clist = []  # 치킨 집 수
hlist = []  # 집 수
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            clist.append([i, j])
        elif arr[i][j] == 1:
            hlist.append([i, j])


if len(clist) == m:
    graph = [0] * len(hlist)
    print(chicken(hlist, clist))
else:
    cbclist = list(cb(clist, m))
    cans = 10 ** 6
    for cbc in cbclist:
        cans = min(cans, chicken(hlist, cbc))
    print(cans)
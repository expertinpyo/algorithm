# 선거구는 총 두개
# bfs로 선거구가 연결되었는지 여부를 판단해보자
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append(x)
    cnt = 1
    while queue:
        x = queue.popleft()
        true_bfs[x] = 1
        for i in range(1, n+1):
            if graph[x][i] and not true_bfs[i]:
                true_bfs[i] = 1
                cnt += 1
                queue.append(i)
    if cnt == n:
        return True
    return False

def connected_case(x):
    global ans
    checked = [0] * (n + 1)
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        cnt = 0
        if not checked[x]:
            checked[x] = 1
        if graph[x].count(1) == n-1:
            return
        for i in range(1, n+1):
            if checked[i]:
                cnt += pnum[i]
        compare = abs(sum(pnum) - 2 * cnt)
        ans = min(ans, compare)


        for i in range(1, n+1):
            if graph[x][i] and not checked[i]:
                queue.append(i)

def bfs2(x):
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        if not checked2[x]:
            checked2[x] = 1
        for i in range(1, n+1):
            if graph[x][i] and not checked2[i]:
                checked2[i] = 1
                queue.append(i)
    asd = []
    for i in range(1, n+1):
        if checked2[i]:
            asd.append(i)
    finds.append(asd)



def disconnected_case():
    # 연결된 구역이 있는지 먼저 확인하고 싶다.
    global ans, n, checked2
    cnt = 0
    if n != 2:  # 두개인 경우는 상관 없음
        for i in range(1, n+1):
            if not graph[i].count(1):   # 구역이 존재하는지 여부 판단
                cnt += 1

        if cnt >= 2:
            ans = -1
            return
        else:
            already = []
            for i in range(1, n+1):
                if i not in already:
                    bfs2(i)
                for cc in range(1, n+1):
                    if checked2[cc]:
                        already.append(cc)
                checked2 = [0] * (n + 1)
            if len(finds) > 2:
                ans = -1
                return
            else:
                cntt = 0
                for f in finds[0]:
                    cntt += pnum[f]
                ans = abs(sum(pnum) - cntt*2)
                return


n = int(input())                        # 구역 수
pnum = [0] + list(map(int, input().split()))  # 구역별 인구 수
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arrs = list(map(int, input().split()))
    for j in range(1, arrs[0]+1):
        graph[i][arrs[j]] = 1
true_bfs = [0]*(n+1)

if bfs(1):  # 모든 지점이 다 연결된 경우
    ans = 10 ** 6
    for i in range(1, n+1):
        connected_case(i)
else:
    # 두 경우로 나눈다, 구역이 총 3구간 이상이거나, 연결된 구역이 없는 경우 ans = -1
    checked2 = [0] * (n + 1)
    finds = []
    disconnected_case()

    # 구역이 2구역인 경우
print(ans)

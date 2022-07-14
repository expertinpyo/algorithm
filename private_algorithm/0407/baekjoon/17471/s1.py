# N개 구역
# 1번부터 N번까지 번호
# 두 개의 선거구로 나눈다
# 구역을 적어도 한 개 포함해야 한다
# 한 선거구 내 모든 구역은 연결되어야 한다
# 첫째 줄 구역의 갯수 N
# 둘째 줄 1번 구역부터 N번 구역까지 구역의 인구
# 셋째 줄 부터 N개 줄에 각 구역과 인접한 구역 정보
# 첫번째 정수 : 구역과 인접한 구역 수
# 나머지 정수 : 인접한 구역 번호
# 갈 수 있는 경우의 수는 주로 2개이다
# 3개 이상일 시에는 모든 점들과 함께 움직이게 된다.
# dfs로 접근 할 예정이다.
# 3개 이상인 경우도 그냥 보낸다 보내서 확인한다


# 0409 접근
# 연결이 되나 안되나 먼저 파악
# 그 후 연결이 되는게 아예 없으면 -1
# 구역별로 나눠지면 그 때 계산
# 연결이 정상적이라면 dfs 진행

import sys
input = sys.stdin.readline

def dfs(x):
    next_part = graph[x]
    visited[x] = 1
    if 0 < next_part.count(1) <= 2:   # 연결된 값이 2일 때
        for j in range(n+1):
            if next_part[j] and not visited[j]:    # 값이 0이 아니라면
                dfs(j)
    else:
        visited[x] = 0

n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    arrs = list(map(int, input().split()))
    for j in range(1, len(arrs)):
        graph[i][arrs[j]] = 1
        graph[arrs[j]][i] = 1

ans_list = []
for i in range(1, n+1):
    visited = [0]*(n+1)
    ans = 10**6
    dfs(i)
    if visited.count(0) == (n+1):
        ans_list.append(-1)
    else:
        ttt = 0
        total_p = sum(population)
        for z in range(1, n+1):
            if visited[z]:
                ttt += population[z]
            ans = min(ans, abs(total_p-2*ttt))
        ans_list.append(ans)

print(min(ans_list))
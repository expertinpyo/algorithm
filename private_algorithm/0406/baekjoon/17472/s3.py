# 컨셉
# 1. dfs로 섬 위치를 파악한다
# 2. 각 섬 별 떨어진 위치를 count 등으로 저장한다 =>
# 가로, 세로 줄을 읽으며 그 곳에 다른 값이 있으면 cnt하는 전략을 세워본다.
# 원래는 graph에 append 했었는데, 리스트로 접근해보는 것도 좋을 것 같다.
# 3. prim, kruskal 중 하나를 사용해서 각 섬을 연결 시킨 후 최단 거리를 출력한다.
import heapq
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def island(x, y):
    for d in di:
        nx = x + d[1]
        ny = y + d[0]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not maps[nx][ny]:
            maps[nx][ny] = cnt
            island(nx, ny)
    return

def distance(lists, n, m):
    number_cnt = 0
    for i in range(n):
        island_list = lists[i]
        for j in range(1, cnt+1):
            if island_list.count(j):
                number_cnt += 1
        if number_cnt >= 2:     # 한 직선에 섬들이 2개 이상 있을 때 => 거리 계산 가능
            idx = -1
            island_num = -1
            for k in range(m):
                if island_list[k]:  # 그 점이 섬일 때
                    if island_num == -1:    # 처음 마주치는 섬일 때
                        idx = k
                        island_num = island_list[k]
                    else:                   # 섬을 마주친 적이 있다면
                        if island_list[k] == island_num:    # 같은 번호의 섬이라면, idx만 갱신
                            idx = k
                        else:               # 다른 섬을 마주했다면
                            if abs(idx-k) - 1 > 1:   # 거리가 1보다 큰 경우에는
                                a = [island_num, island_list[k], abs(idx-k)-1]
                                b = [island_list[k], island_num, abs(idx - k) - 1]
                                if a not in edges:
                                    edges.append(a)
                                if b not in edges:
                                    edges.append(b)
                            idx = k
                            island_num = island_list[k]

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

def kruskal():
    global ans
    edge_cnt = 0
    for i in range(len(edges)):
        if edge_cnt == cnt-1:
            return
        x = edges[i][0]
        y = edges[i][1]
        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[i][2]
    if edge_cnt < cnt - 1:
        ans = -1
        return


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# n * m 격자
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maps = [[0] * m for _ in range(n)]

    cnt = 1             # 섬의 개수, 최대 6까지 될 수 있다.(문제서 정의)
    for i in range(n):
        for j in range(m):
            if not maps[i][j] and arr[i][j]:
                maps[i][j] = cnt
                island(i, j)
                cnt += 1
    edges = []
    maps_reverse = list(zip(*maps))
    distance(maps, n, m)
    distance(maps_reverse, m, n)

    if edges:
        edges.sort(key = lambda x:x[2])
        ans = 0
        p = list(range(cnt+1))
        kruskal()
    else:
        ans = -1
    print(f'#{tc} {ans}')

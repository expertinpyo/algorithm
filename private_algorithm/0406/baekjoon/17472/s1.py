# n*m 크기의 격자
# 격자의 각 칸은 땅이거나 바다이다.
# 섬 : 연결된 땅이 상하좌우로 붙어있는 덩어리
# 색칠되어 있는 칸은 땅임
# 다리는 바다에만 건설 가능
# 다리 길이는 다리가 격자에서 차지하는 칸의 수
# A에서 다리를 통해 B로 갈 때 연결되었다고 한다.
# 2 <= 섬의 갯수 <= 6
import heapq
import sys
input = sys.stdin.readline
sys.stdin = open('input.txt')

def island(r, c):
    for d in di:
        nr, nc = r + d[1], c + d[0]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = cnt
            island(nr, nc)
    return

def minimum_distance(v_list, n, m):
    for i in range(n):
        cntt = 0
        for j in range(1, 7):
            if v_list[i].count(j):
                cntt += 1
        if cntt >= 2:
            a = 0
            for j in range(m):
                if not a:
                    if v_list[i][j]:
                        a = v_list[i][j]
                        idx = j
                else:
                    if v_list[i][j] == a:
                        idx = j
                    else:
                        if v_list[i][j]:
                            if abs(idx - j) - 1 > 1:
                                graph[v_list[i][idx]].append((v_list[i][j], abs(idx - j) - 1))
                                graph[v_list[i][j]].append((v_list[i][idx], abs(idx-j)-1))
                            idx = j
                            a = v_list[i][j]


def prim():
    global ans
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        weight, node = heapq.heappop(heap)
        if not prim_visited[node]:
            prim_visited[node] = 1
            ans += weight
            for new_node, new_weight in graph[node]:
                if not prim_visited[new_node]:
                    heapq.heappush(heap, (new_weight, new_node))
T = int(input())
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    cnt = 1                     # 섬의 개수
    for i in range(n):
        for j in range(n):
            if arr[i][j] and not visited[i][j]:
                visited[i][j] = cnt
                island(i, j)
                cnt += 1

    # 줄마다 카운터를 읽어서 그 숫자가 2 이하인 경우는 제외
    # 3 이상인 경우, max idx 값을 찾아서 거리 계산 후 그래프에 담기
    # 섬의 개수는 총 6개 까지 이므로 6까지만 보면 된다.
    graph = [[] for _ in range(1, cnt+1)]
    visited_reverse = list(zip(*visited))
    minimum_distance(visited, n, m)
    # print(graph)
    minimum_distance(visited_reverse, m, n)
    # print(graph)
    ans = 0
    prim_visited = [0]*(cnt+1)
    prim()
    if not ans:
        ans = -1
    print(f'#{tc} {ans}')
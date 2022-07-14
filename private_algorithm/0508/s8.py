# s 지점에서 출발, 목적지 후보들 중 하나가 목적지임
# 최단 거리로 이동
# 회색 원에서 출발, 두 검은 원 중 하나로 이동

# g와 h 교차로 사이에 있는 도로를 지나갔다.
# 점선으로 표시된 도로에서 냄새를 맡았다.
import heapq


def dijkstra(s):
    inf = 10 ** 8
    visited = [0] * (n + 1)
    dist = [inf] * (n + 1)  # 시작 점에서의 거리
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        amount, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[node] = amount
            for new_n, new_a in arr[node]:
                if not visited[new_n]:
                    heapq.heappush(heap, (new_a + amount, new_n))
    return dist

T = int(input())
for tc in range(T):
    n, m, t = map(int, input().split())
    # 교차로, 도로, 목적지 후보 개수
    arr = [[] for _ in range(n+1)]

    s, g, h = map(int, input().split())
    # 출발지, 교차로들
    for _ in range(m):
        a, b, d = map(int, input().split())
        arr[a].append([b, d])
        arr[b].append([a, d])
        # 양방향 도로
    ob_list = []
    for _ in range(t):
        ob_list.append(int(input()))
        # 목적지가 될 수 있는 도로 목록 리스트
    dists = []
    for i in [s, g, h]:
        dists.append(dijkstra(i))

    for arg in arr[g]:
        if arg[0] == h:
            distance1 = arg[1] + dists[0][g]
            distance2 = arg[1] + dists[0][h]
    ans = []
    for ob in ob_list:
        total = dists[0][ob]
        if dists[1][ob] + distance2 == total or dists[2][ob] + distance1 == total:
            ans.append(ob)
    ans.sort()
    print(*ans)
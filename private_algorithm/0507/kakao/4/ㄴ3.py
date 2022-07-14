# n개의 지점
# 1부터 n까지 번호, 출입구/쉼터/산봉우리

# 양방향 통행 가능
# 등산로별로 이동시간 ㅇ존재
# 쉼터, 산봉우리 방문 시 휴식 가능
# 휴식없이 이동하는 시간 중 가장 긴 시기나 => intensity
# 산 봉우리 중 한 곳 방문
# 출입구 : 처음과 끝 한번씩, 산봉우리 한번
# intensity가 최소가 될 수 있도록 해야함
# 봉우리가 여러개일 때 생각해봐야 함
# 완전탐색 진행해야 함
# 지점 수 n / 등산로 정보 paths [i, j, w] / 출입구 gates / 산봉우리 번호 summits
# gates와 summits 아닌 점은 모두 쉼터
# 산봉우리 번호 and intensity의 최솟값 배출
# intensity가 여러개라면 산봉우리 번호 최소 값 출력
from collections import deque
def solution(n, paths, gates, summits):
    arr = [[] for _ in range(n + 1)]
    for i in range(len(paths)):
        s, e, roads = paths[i][0], paths[i][1], paths[i][2]
        arr[s].append([e, roads])
        arr[e].append([s, roads])

    mins = 10 ** 6  # 최솟값
    tops = 10 ** 6       # tops 최종 값

    for gate in gates:      # 출입구들 중에서
        for e, w in arr[gate]:  # 출입구가 갈 수 있는 경우의 수
            visited = [0]*(n+1)
            queue = deque()
            queue.append([e, w])
            cnt = w
            if e not in summits:
                top = 0
            else:
                top = e
            if not top:
                while queue:
                    start, weight = queue.popleft()
                    for ar in arr[start]:
                        new_start, new_weight = ar[0], ar[1]
                        if new_start not in gates and not visited[new_start]:  # 출발점에 없다면
                            if new_start not in summits:  # 봉우리에 없다면
                                queue.append([new_start, new_weight])
                                if cnt < new_weight:
                                    cnt = new_weight
                                visited[new_start] = 1
                            else:  # 봉우리에 있다면
                                if not top:   # 봉우리 방문한 적 없고, 최솟값이라면
                                    top = new_start
                                    if cnt < new_weight:
                                        cnt = new_weight
                                    queue.append([new_start, new_weight])
                                    visited = [0]*(n+1)
                        else:   # 출발점에 있다면
                            if new_start == gate:   # 출발점과 봉우리가 같다면
                                if top:
                                    break

            if top and cnt <= mins:
                if top < tops:
                    tops = top
                mins = min(cnt, mins)

    answer = [tops, mins]
    print(answer)
    return answer





solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
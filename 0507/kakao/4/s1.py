from collections import deque
def solution(n, paths, gates, summits):
    arr = [[] for _ in range(n + 1)]
    for i in range(len(paths)):
        s, e, roads = paths[i][0], paths[i][1], paths[i][2]
        arr[s].append([e, roads])
        arr[e].append([s, roads])

    mins = 10 ** 6       # 이동 가중치 최솟값
    tops = 10 ** 6       # 봉우리 최종 최솟 값

    for gate in gates:          # 출입구들 중에서
        for start, weight in arr[gate]:
            visited = [0] * (n+1) # 방문체크
            visited[gate] = 1
            top = 0
            cnt = weight
            queue = deque()
            queue.append([start, weight])
            if start in gates: # 방문하려는 산과 동일하다면
                top = start
            else:
                while queue:
                    start, weight = queue.popleft()
                    for new_start, new_weight in arr[start]:
                        if new_start in gates:      # 도착했을 때
                            if new_start == gate and top:
                                break
                        elif new_start in summits:
                            if not top: # 아직 봉우리 방문 안했을 경우
                                top = new_start
                                if cnt < new_weight:
                                    cnt = new_weight
                                queue.append([new_start, new_weight])
                                visited = [0] * (n+1)   # visited 갱신
                        else:   # 그냥 일반 점인 경우
                            if not visited[new_start]:  # 방문하지 않은 점인 경우
                                visited[new_start] = 1  # 방문체크
                                if cnt < new_weight:
                                    cnt = new_weight
                                queue.append([new_start, new_weight])
            if top:
                if cnt < mins:
                    tops = top
                    mins = min(cnt, mins)
                elif cnt == mins:
                    tops = min(top, tops)

    answer = [tops, mins]
    print(answer)
    return answer

solution(
6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
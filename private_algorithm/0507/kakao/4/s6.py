from collections import deque
def solution(n, paths, gates, summits):
    arr = [[] for _ in range(n + 1)]
    for i in range(len(paths)):
        s, e, roads = paths[i][0], paths[i][1], paths[i][2]
        arr[s].append([e, roads])
        arr[e].append([s, roads])
    mins = 10 ** 6       # 이동 가중치 최솟값
    tops = 10 ** 6       # 봉우리 최종 최솟 값
    for gate in gates:
        for summit in summits:
            ans = find(gate, summit, arr, n, summits, gates)
            print(ans)
            for a in ans:
                if a[1] < mins:
                    tops = a[0]
                    mins = min(mins, a[1])
                elif a[1] == mins:
                    tops = min(tops, a[0])

    answer = [tops, mins]
    print(answer)
    return answer

def find(start, end, arr, n, summits, gates):
    ans_list = []
    for r in arr[start]:
        stack = [[r[0], r[1], r[1]]]
        visited = [0]*(n+1)
        while stack:
            start, weight, cnt = stack.pop()
            visited[start] = 1
            if start == end:
                if cnt:
                    visited[end] = 0
                    ans_list.append([end, cnt])
            for new_start, new_weight in arr[start]:
                if not visited[new_start]:  # 방문한 적 없다면
                    if new_start not in gates:  # 출발점 아니라면
                        if new_start not in summits or new_start == end:  # 산 봉우리 아니라면
                            if cnt < new_weight:
                                stack.append([new_start, new_weight, new_weight])
                            else:
                                stack.append([new_start, new_weight, cnt])
                            visited[new_start] = 1
    return ans_list

solution(
5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5])
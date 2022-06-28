import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    anss = []                                       # 빈 리스트
    visited = [0]*(n*2-1)                           # 빈 리스트
    for spot in where_to_visit:                     # 집의 좌표 탐색
        distance = abs(x-spot[0]) + abs(y-spot[1])  # 점들 사이 거리 계산
        visited[distance] += 1                      # visited에 해당 거리를 인덱스로 하여 추가
    for v in range(n*2-1):
        cost = (v+1)**2 + v**2                      # 거리 별 가격
        if sum(visited[:v+1])*m >= cost:            # 해당 인덱스까지의 모든 점들의 비용이 거리 별 가격보다 크다면
            anss.append(v)                          # 해당 인덱스 리스트에 추가
    if anss:
        max_idx = max(anss)                         # 맥스 인덱스값 추출
        return sum(visited[:max_idx+1])             # 맥스 인덱스까지의 sum returm
    return 0                                        # 해당 사항 없으면 0 리턴

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())                            # n 배열 크기, m 비용
    arr = [list(map(int, input().split())) for _ in range(n)]   # 전체 리스트
    where_to_visit = []                                         # 빈 리스트
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                where_to_visit.append([i,j])                    # 해당 좌표에 집이 있으면 where to visit에 추가
    ans_list = []                       # 빈 리스트
    for i in range(n):                  # 전체 범위 탐색 dfs
        for j in range(n):
            if dfs(i, j):               # 값이 있다면
                ans_list.append(dfs(i, j))  # 정답 리스트에 추가
    print(f"#{tc} {max(ans_list)}")     # 그 중 max값 출력
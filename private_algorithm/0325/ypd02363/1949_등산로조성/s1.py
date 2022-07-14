import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    visited = [[0] * n for _ in range(n)]                               # bfs 진행
    if not visited[x][y]:
        visited[x][y] = 1
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for di in range(4):
            nx = x + delta[di][1]
            ny = y + delta[di][0]
            if 0 <= nx < n and 0 <= ny < n and arr[x][y] > arr[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
    what_we_need = 0
    if visited:
        for vit in visited:
            if max(vit) > what_we_need:
                what_we_need = max(vit)
        return what_we_need
    return 0

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())                            # n, k 정의
    arr = [list(map(int, input().split())) for _ in range(n)]   # 리스트 입력 받기

    start = 0                                                   # 시작 크기
    for ar in arr:                                              # 최댓값
        if max(ar) > start:
            start = max(ar)

    start_points = []
    for i in range(n):                                          # 시작점 추출
        for j in range(n):
            if arr[i][j] == start:
                start_points.append([i, j])

    ans_list = []                                               # 모든 점에서 1부터 k까지 빼가면서 경우의 수를 볼 예정
    for i in range(n):
        for j in range(n):
            for kk in range(1, k+1):
                arr[i][j] -= kk
                for st in start_points:
                    if arr[st[0]][st[1]] == start:              # 해당 점이 아직까지 max값이 맞다면
                        ans_list.append(bfs(st[0], st[1]))
                arr[i][j] += kk

    print(f'#{tc} {max(ans_list)}')

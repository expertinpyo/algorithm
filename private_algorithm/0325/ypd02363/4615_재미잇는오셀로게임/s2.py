import sys
sys.stdin = open('input.txt')

def dfs(x, y, c):
    for i in range(8):              # 총 여덟 방향
        nx = x + delta[i][1]        # nx, ny 정의
        ny = y + delta[i][0]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 and arr[nx][ny] != c:   # nx, ny가 범위 내에 있고, 0과 c가 아니라면
            for k in range(1, n):                   # 1부터 n까지
                nnx = nx + delta[i][1] * k          # nx, ny를 정의 했을 때와 같은 방향으로 탐색 시작
                nny = ny + delta[i][0] * k
                if 0 <= nnx < n and 0 <= nny < n:       # 탐색하는 점들이 범위 내에 있고
                    if arr[nnx][nny] != c:              # 그 값이 c가 아닐 때
                        if arr[nnx][nny] == 0:          # 0이라면 해당없으므로 break
                            break
                        else:                           # 0이 아니라면 continue
                            continue
                    elif arr[nnx][nny] == c:            # 값이 c라면
                        for j in range(k+1):            # 최초 점(x, y)부터 k값 까지 변환 시작
                            xx = x + delta[i][1] * j
                            yy = y + delta[i][0] * j
                            arr[xx][yy] = c             # c로 변환
                        break                           # break

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())                        # 배열 크기와 입력 개수
    arr = [[0]*n for _ in range(n)]                         # 전체 배열
    arr[n//2-1][n//2-1] = arr[n//2][n//2] = 2               # 가운뎃 값 세팅
    arr[n//2-1][n//2] = arr[n//2][n//2-1] = 1
    delta = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1],[0, -1], [1, -1]]   # 델타함수 정의
    inputs = [list(map(int, input().split())) for _ in range(m)]        # 입력값들
    for ips in range(m):
        dfs(inputs[ips][1]-1, inputs[ips][0]-1, inputs[ips][2])         # 입력값들 탐색 시작
    cnt_1 = cnt_2 = 0

    for ar in arr:
        cnt_1 += ar.count(1)
        cnt_2 += ar.count(2)
    print(f"#{tc} {cnt_1} {cnt_2}")
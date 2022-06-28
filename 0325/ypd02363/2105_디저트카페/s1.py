import sys
sys.stdin = open('input.txt')

def dfs(x, y, di):
    if [x, y] in nope:                              # 시작점이 꼭지점이라면 return
        return
    if di <= 2:                                     # 방향이 0, 1, 2라면 (3은 우측 대각 상향 방향 => 고정되어야함)
        for k in range(di, di+2):                   # 두 뱡향만 확인 (0,1 /1,2 /2,3)
            nx = x + delta[k][1]                    # 새로운 좌표 nx, ny 정의
            ny = y + delta[k][0]
            if 0 <= nx < N and 0 <= ny < N:         # 좌표가 사각형 범위 내에 있다면
                if arr[nx][ny] not in dessert:      # 좌표의 값이 리스트에 없다면
                    dessert.append(arr[nx][ny])     # 리스트에 좌표값 추가
                    dfs(nx, ny, k)                  # dfs 재귀
                    dessert.pop()                   # 다 끝난 것이므로 좌표값 리스트에서 pop
                elif [nx, ny] == start and k == 3:  # 좌표값이 시작점이고, 방향이 3이라면(시작점 도착)
                    ans.append(len(dessert))        # 길이만큼 ans에 추가
                    return
    else:                                           # 방향이 3일 때
        nx = x + delta[di][1]                       # 새로운 좌표 정의
        ny = y + delta[di][0]
        if 0 <= nx < N and 0 <= ny < N:             # 범위내 값이라면
            if arr[nx][ny] not in dessert:          # 좌표값이 리스트 내에 없다면
                dessert.append(arr[nx][ny])         # 좌표 추가
                dfs(nx, ny, di)                     # dfs 재귀
                dessert.pop()                       # 해당 없으므로 pop
            elif [nx, ny] == start:                 # 좌표가 시작점이라면 (방향은 어짜피 3방향)
                ans.append(len(dessert))            # 리스트에 길이 추가
                return
    ans.append(-1)                                  # 해당하는 값이 없을 때 -1 추가
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    delta = [[1, 1], [-1, 1], [-1, -1], [1, -1]]        # 방향  벡터 delta
    nope = [[0, 0], [N-1, 0], [0, N-1], [N-1, N-1]]     # 사각형 꼭지점 부분
    ans = []                                            # 정답 리스트
    for i in range(N):
        for j in range(N):
            start = [i, j]                              # dfs 시작점
            dessert = [arr[i][j]]                       # dessert 리스트
            dfs(i, j, 0)                                # x, y 좌표, 초기방향 0

    print(f"#{tc} {max(ans)}")
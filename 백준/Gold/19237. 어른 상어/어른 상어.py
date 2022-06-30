# 19237 어른 상어

# 1의 번호 가진 어른 상어는 나머지 모두 쫓아낼 수 있음
# 냄새는 상어가 k번 이동하고 나면 사라진다
# 냄새가 없는 칸 => 자신의 냄새가 있는 칸

# sarr : 상 1/ 하 2/ 좌 3/ 우 4


# 각 초 마다 빼주는 과정을 제외하고 해당 점에 언제 방문했는지를 기입해준다.

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    ar = list(map(int, input().split()))
    arr.append(ar)
snum = list(map(int, input().split()))
sarr = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        sarr[i].append(list(map(int, input().split())))
box = [[0] * n for _ in range(n)]
cnt = 0
slocation = [[] for _ in range(m+1)]
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            slocation[arr[i][j]] = [i, j, snum[arr[i][j]-1]]
            box[i][j] = [arr[i][j], 0, 0]


di = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while True:
    total = slocation.count(0)
    if total == m-1:    # 첫번째 상어만 남았을 경우
        print(cnt)
        break
    if cnt >= 1000:     # 1000 초과면
        print(-1)
        break
    cnt += 1  # 시간 1씩 증가
    for i in range(1, m+1):
        if slocation[i]:   # 아직 존재할 떄
            x, y, direction = slocation[i][0], slocation[i][1], slocation[i][2]
            next_d = sarr[i-1][direction-1]     # 우선순위 배열
            for d in next_d:
                new_x, new_y = x + di[d-1][0], y + di[d-1][1]
                if 0 <= new_x < n and 0 <= new_y < n:
                    if not box[new_x][new_y] or box[new_x][new_y][1] < cnt-k:       # 아직 방문하지 않은 점이거나 현 시간보다
                        box[new_x][new_y] = [i, cnt, 0]  # 값 갱신
                        slocation[i] = [new_x, new_y, d]    # 현재 위치 갱신
                        break   # 첫번째 경우, 방향 우선순위 고려 후 칸이 비어있을 때
                    elif box[new_x][new_y][1] == cnt and not box[new_x][new_y][2]:     # 방문한 점이지만, 동시에 어떤 상어가 방문한 점일 때
                        if i > box[new_x][new_y][0]:    # 내가 우선순위가 낮은 상어라면
                            slocation[i] = 0        # 잡아먹힘
                        else:                       # 상대방이 우선순위가 낮다면
                            slocation[box[new_x][new_y][0]] = 0     # 상대방이 잡아먹힘
                            box[new_x][new_y] = [i, cnt, 0]  # 값 갱신
                        break
            else:   # for else, 갈 수 있는 칸이 없을 때 , 내 체취가 있는 곳으로 돌아가야함
                for d in next_d:
                    new_x, new_y = x + di[d - 1][0], y + di[d - 1][1]
                    if 0 <= new_x < n and 0 <= new_y < n and box[new_x][new_y][0] == i:
                        box[new_x][new_y] = [i, cnt, 1]
                        slocation[i] = [new_x, new_y, d]
                        break




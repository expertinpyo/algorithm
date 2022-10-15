from copy import deepcopy
def fish_move(arr, dis, fish):
    for i in range(1, 17):
        if fish[i]:
            x, y = fish[i]
            d = dis[x][y]
            for j in range(d, d+8, 1):
                nx, ny = x + di[j % 8][0], y + di[j % 8][1] # d가 변함
                if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] >= 0:
                    fish[i] = (nx, ny)
                    fish[arr[nx][ny]] = (x, y)
                    arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                    dis[x][y], dis[nx][ny] = dis[nx][ny], j % 8
                    break

ans = 0
arr = [[0] * 4 for _ in range(4)]
dis = [[0] * 4 for _ in range(4)]
di = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fish = [0] * 17
for i in range(4):
    input_list = list(map(int, input().split()))
    for j in range(8):
        if not j % 2:
            arr[i][j//2] = input_list[j]
            fish[input_list[j]] = i, j//2
        else:
            dis[i][j//2] = input_list[j]-1

cnt = arr[0][0]
fish[arr[0][0]] = 0
arr[0][0] = -1
fish_move(arr, dis, fish)
shark = [(0, 0, deepcopy(arr), deepcopy(dis), deepcopy(fish), cnt)]
while shark:
    sx, sy, new_arr, new_dis, new_fish, cnt = shark.pop()
    ans = max(cnt, ans)
    for i in range(1, 4):
        nsx, nsy = sx + di[new_dis[sx][sy]][0] * i, sy + di[new_dis[sx][sy]][1] * i
        if 0 <= nsx < 4 and 0 <= nsy < 4 and new_arr[nsx][nsy] > 0:
            c_arr = deepcopy(new_arr)
            c_dis = deepcopy(new_dis)
            c_fish = deepcopy(new_fish)

            killed = c_arr[nsx][nsy]
            c_arr[sx][sy], c_arr[nsx][nsy] = 0, -1
            c_dis[sx][sy] = 0
            c_fish[killed] = 0
            fish_move(c_arr, c_dis, c_fish)
            shark.append((nsx, nsy, c_arr, c_dis, c_fish, cnt + killed))

print(ans)



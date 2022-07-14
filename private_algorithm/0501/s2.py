# # # n*n 공간 상어 1마리
# # # 초기 상어 크기 2
# # # 큰 물고기 칸은 지나갈 수 없음
# # # 크기가 같은 물고기는 지나갈 수는 있는데 먹지는 못함
# # # 먹을 수 있는 물고기 없다면 엄마 상어에게 도움 요청
# # # 먹을 수 있는 물고기가 1마리보다 많다면 가까운 물고기
# # # 많이 겹친다면 행, 열 순으로
from collections import deque

def bfs(x, y):
    global nums
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for d in di:
            nx, ny = x + d[1], y + d[0]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= level and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
                if 0 < arr[nx][ny] < level:
                    fishes.append([nx, ny])


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
num_fish = [0]*7

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            if arr[i][j] == 9:
                x, y = i, j
                arr[i][j] = 0
            else:
                num_fish[arr[i][j]] += 1
cnt = 0
level = 2
if num_fish.count(0) != 7:
    nums = 0
    while True:
        numFish = 0
        if level <= 6:
            for i in range(1, level, 1):
                numFish += num_fish[i]
            if not numFish:
                break
        else:
            numFish = sum(num_fish)
            if not numFish:
                break

        fishes = []
        visited = [[-1] * n for _ in range(n)]
        visited[x][y] = 0
        bfs(x, y)
        if not fishes:
            break
        x, y = n, n
        mins = 10**6
        for fish in fishes:
            fx, fy = fish[0], fish[1]
            if visited[fx][fy] != -1:
                if visited[fx][fy] < mins:
                    mins = visited[fx][fy]
                    x, y = fx, fy

                elif visited[fx][fy] == mins:
                    if fx < x:
                        mins = visited[fx][fy]
                        x, y = fx, fy

                    elif fx == x:
                        if fy < y:
                            mins = visited[fx][fy]
                            x, y = fx, fy

        nums += 1
        cnt += mins
        num_fish[arr[x][y]] -= 1
        arr[x][y] = 0
        if nums == level:
            level += 1
            nums = 0
print(cnt)
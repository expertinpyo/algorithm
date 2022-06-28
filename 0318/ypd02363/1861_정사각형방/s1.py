import sys
sys.stdin = open('input.txt')
# 이동하려는 방이 존재하고 이동하려는 방에 적힌 숫자가 정확히 현재 방보다 1 커야함

def bfs(x, y):
    visited[x][y] = 1
    queue = [[x, y]]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ans = 1
    while queue:
        x, y = queue.pop(0)
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == arr[x][y] + 1 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                ans += 1
    return ans

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans_list = []
    for i in range(n):
        for j in range(n):
            a = arr[i][j]
            visited = [[0] * n for _ in range(n)]
            result = bfs(i, j)
            ans_list.append([a, result])
    max_nn = 0
    min_nn = 1000000
    for ans in ans_list:
        if ans[1] > max_nn:
            max_nn = ans[1]
    for ans in ans_list:
        if ans[1] == max_nn and ans[0] < min_nn:
            min_nn = ans[0]
    print(f"#{tc} {min_nn} {max_nn}")
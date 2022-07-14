import sys
sys.stdin = open('input.txt')
# bfs 로 풀기
# 파이프 이어지는지 여부 판단해야함
def bfs(x, y):
    global l
    queue = [[x, y]]
    ans = 1
    while l > 1:
        length = len(queue)
        for i in range(length):
            x, y = queue.pop(0)
            direction = cover[arr[x][y]]
            for di in direction:
                nx = x + di[1]
                ny = y + di[0]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                    connection = cover[arr[nx][ny]]
                    for co in connection:
                        nnx = nx + co[1]
                        nny = ny + co[0]
                        if nnx == x and nny == y:
                            visited[nx][ny] = 1
                            ans += 1
                            queue.append([nx, ny])
                            break
                    else:
                        continue
        l -= 1
    return ans


T = int(input())
for tc in range(1, T+1):
    n, m, r, c, l = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    cover = {
        1 : [[1,0],[0,1],[-1,0],[0,-1]],
        2 : [[0, 1], [0, -1]],
        3 : [[1, 0], [-1, 0]],
        4 : [[1, 0], [0, -1]],
        5 : [[1, 0], [0, 1]],
        6 : [[-1, 0], [0, 1]],
        7 : [[-1, 0], [0, -1]]
    }
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    print(f"#{tc} {bfs(r, c)}")
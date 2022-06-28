import sys
sys.stdin = open('input.txt')

def bfs(x):
    queue = [x]
    while queue:
        x = queue.pop(0)
        if x == g:
            return
        for index in range(1, v+1):
            if arr[x][index] and not visited[index]:
                queue.append(index)
                visited[index] = visited[x] + 1

T = int(input())
for tc in range(1, 1+T):
    v, e = map(int, input().split())
    arr = [[0]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    s, g = map(int, input().split())
    visited = [0] * (v+1)
    bfs(s)
    print(f"#{tc} {visited[g]}")
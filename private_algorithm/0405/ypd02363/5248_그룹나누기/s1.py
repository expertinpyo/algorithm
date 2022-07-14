import sys
sys.stdin = open('input.txt')

def bfs(x):
    queue = [x]
    while queue:
        x = queue.pop(0)
        for i in range(1, n+1):
            if i != x and not visited[i] and group[x][i]:
                visited[i] = 1
                check.append(i)
                queue.append(i)
    v.append(check)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    group = [[0]*(n+1) for i in range(n+1)]
    arr = list(map(int, input().split()))
    for i in range(m):
        group[arr[i*2]][arr[i*2+1]] = 1
        group[arr[i * 2 + 1]][arr[i * 2]] = 1
    visited = [0]*(n+1)
    v = []
    for i in range(1, n+1):
        if not visited[i]:
            check = [i]
            visited[i] = 1
            bfs(i)
    print(f"#{tc} {len(v)}")
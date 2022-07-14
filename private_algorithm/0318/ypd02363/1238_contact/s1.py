import sys
sys.stdin = open('input.txt')

def bfs(x):
    queue = [x]
    while queue:
        x = queue.pop(0)
        for i in range(max_num+1):
            if connected[x][i] and not visited[x][i] and i not in num_list:
                num_list.append(i)
                queue.append(i)
                num_dict[i] = x
                visited[x][i] = visited[num_dict[x]][x] + 1


for tc in range(1, 11):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    max_num = max(arr)
    connected = [[0]*(max_num+1) for _ in range(max_num+1)]
    for i in range(n//2):
        connected[arr[i*2]][arr[i*2+1]] = 1
    visited = [[0]*(max_num+1) for _ in range(max_num+1)]
    num_list = [start]
    num_dict = {start:0}
    bfs(start)
    max_n = ans = 0
    for i in range(1, max_num + 1):
        if max_n < max(visited[i]):
            max_n = max(visited[i])
    for i in range(1, max_num+1):
        for j in range(1, max_num+1):
            if visited[i][j] == max_n:
                if j > ans:
                    ans = j
    print(f"#{tc} {ans}")
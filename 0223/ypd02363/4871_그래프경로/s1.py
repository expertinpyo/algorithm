import sys
sys.stdin = open("input.txt")
T = int(input())

def dfs(S):
    stack = [S]                         # 스택 정의
    while stack:                        # 스택이 차있으면 반복
        v = stack.pop()                 # 스택 마지막 pop
        if not visited[v]:              # v를 지나간 적이 없으면
            visited[v] = 1              # 지나감 표시
            if v == G:                  # v가 G(끝점) 이라면 return 1
                return 1
            for w in range(1, V + 1):   # 1부터 V까지
                if node_arr[v][w] == 1 and not visited[w]:  # 해당 노드와 연결되어있고, 그 지점을 아직 지나가지 않았다면
                    stack.append(w)     # stack에 append 해주기
    return 0                            # 다 돌았음에도 값이 없다면(edge가 없다면)


for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    node_arr = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        node_arr[arr[i][0]][arr[i][1]] = 1
    print(f"#{tc} {dfs(S)}")

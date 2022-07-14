# A와 B는 숫자 0, 99로 고정
# 모든 길은 순서쌍으로 나타내짐
# 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것
# 후진 불가

import sys
sys.stdin = open("input.txt")

def dfs(s):
    stack = [s]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            if v == 99:
                return 1
            for i in range(100):
                if G[v][i] == 1 and not visited[i]:
                    stack.append(i)
    return 0

for tcc in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0] * 100 for _ in range(100)]
    for i in range(E):
        G[temp[2*i]][temp[2*i+1]] = 1
    visited = [0]*100
    print(f"#{tc} {dfs(0)}")
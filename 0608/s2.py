# baekjoon 1967
# dfs
from sys import setrecursionlimit
setrecursionlimit(100000)

def dfs(x, w):
    for new_n, new_w in tree[x]:
        if nodes[new_n] == -1:
            nodes[new_n] = new_w + w
            dfs(new_n, nodes[new_n])

n = int(input())    # node 개수
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int,input().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])

nodes = [-1] * (n+1)
nodes[1] = 0
dfs(1, 0)
idx = nodes.index(max(nodes))
nodes = [-1] * (n+1)
nodes[idx] = 0
dfs(idx, 0)
print(max(nodes))
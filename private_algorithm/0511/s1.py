# 17073
# 마지막 노드를 찾아라

n, w = map(int,input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[v].append(u)
    tree[u].append(v)
cnt = 0
for i in range(2, n+1):
    if len(tree[i]) == 1:
        cnt += 1
print(w/cnt)



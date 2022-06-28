# baekjoon 1967
# dfs
# 부모 노드일 때 마다 값을 갱신해준다면 좋은 풀이가 될 것 같다

n = int(input())    # node 개수
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int,input().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])

ans = 0
nodes = [0] * (n+1)
for i in range(n, 0, -1):
    new_n = tree[i][0][0]
    new_w = tree[i][0][1]
    if len(tree[i]) == 1:
        if nodes[new_n] < new_w:
            nodes[new_n] = new_w
        if nodes[new_n] > ans:
            ans = nodes[new_n]
    else:
        each = 0
        for comp in tree[i]:
            if i > comp[0]: # i가 comp[0]의 자식 노드인 경우
                sums = nodes[i] + comp[1]   # 새로운 값
                if not nodes[comp[0]]:
                    nodes[comp[0]] = sums
                    each = sums
                else:
                    each = nodes[comp[0]] + sums
                    if nodes[comp[0]] < sums:
                        nodes[comp[0]] = sums
        if each > ans:
            ans = each
print(ans)
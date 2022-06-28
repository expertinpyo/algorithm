# 12865
# dp 일종, kanpsack

def dijkstra():
    for _ in range(k):
        idx = -1
        maxs = -1
        for i in range(k+1):
            if not visited[i]:
                if dist[i] > maxs:
                    maxs = dist[i]
                    idx = i
        visited[idx] = 1
        for new_n, new_w in arr:
            new_n += idx
            if new_n <= k:
                if not visited[new_n]:
                    if dist[new_n] < new_w + maxs:
                        dist[new_n] = new_w + maxs



n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [0] * (k+1)
dist = [-1] * (k+1)
dist[0] = 0
dijkstra()
print(dist[k])
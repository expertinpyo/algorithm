from heapq import *
import sys
 
input = sys.stdin.readline
 
def dijkstra(s):
    cost = [float('inf')] * (n+1)
    hq = [[0, s]]
    cost[s] = 0
    while hq:
        t,x = heappop(hq)
        if cost[x] != t: continue
        for nx, nt in adj[x]:
            if cost[nx] > t+nt:
                cost[nx] = t+nt
                heappush(hq, [cost[nx], nx])
    return cost
 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    ans = [float('inf')]*(n+1)
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append([b, c])
        adj[b].append([a, c])
    k = int(input())
    friend = [*map(int, input().split())]
    for i in range(1, n+1):
        dist = dijkstra(i)
        ans[i] = sum(dist[f] for f in friend)
    print(ans.index(min(ans)))
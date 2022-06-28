n, k = map(int, input().split())
mlist = []
vlist = []
for _ in range(n):
    m, v = map(int, input().split())
    mlist.append(m,v)
mlist.sort()
for _ in range(k):
    c = map()
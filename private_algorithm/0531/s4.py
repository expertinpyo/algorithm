N, K = map(int, input().split())
arr = []
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))

for i in range(N):
    left = K - arr[i]
    for j in range(N):



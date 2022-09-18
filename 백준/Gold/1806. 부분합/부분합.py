from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
prefix = [0] * N
arr = list(map(int, input().split()))
prefix[0] = arr[0]
for i in range(1, N):
    prefix[i] = prefix[i-1] + arr[i]

if prefix[-1] < S:
    print(0)
    exit()
elif prefix[-1] == S:
    print(N)
    exit()
elif prefix[0] >= S:
    print(1)
    exit()

for i in range(N):
    if prefix[i] >= S:
        right = i
        ans = i + 1
        break

left = 0
while right < N:
    if right - left >= ans:
        left += 1
    if (prefix[right] - prefix[left] >= S):
        left += 1
        ans -= 1
    else:
        right += 1
print(ans)
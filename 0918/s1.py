# 1806 부분합
# 부분합 중 그 합이 S이상 되는 것 중 가장 짧은 것의 길이
# S 이상
# 전략


from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
prefix = [0] * N
arr = list(map(int, input().split()))
prefix[0] = arr[0]
for i in range(1, N):
    prefix[i] = prefix[i-1] + arr[i]
ans = 10 ** 6
print(prefix)
for left in range(N):
    if ans == 1:
        break
    for right in range(left+1, N):
        test = prefix[right] - prefix[left]
        if test < S:
            continue
        elif test == S:
            if right-left < ans:
                ans = right-left
            else:
                break
        else:
            break
    if prefix[left] == S and left < ans:
        ans = left
print(ans)
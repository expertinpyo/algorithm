# 17299
# 오른족에 있으면서 fa보다 큰 수 중 가장 왼족 수

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dic = {}
for i in range(N):
    if not arr[i] in dic:
        dic[arr[i]] = arr.count(arr[i])
stack = [0]
for i in range(N-1, 0, -1):
    while

cnt = [0]

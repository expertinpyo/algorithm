import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    ans_list = []
    for i in range(1, n+1):
        combi = list(combinations(arr, i))
        for com in combi:
            a = sum(list(com))
            if a < b:
                continue
            else:
               ans_list.append(a)
    print(f"#{tc} {min(ans_list)-b}")
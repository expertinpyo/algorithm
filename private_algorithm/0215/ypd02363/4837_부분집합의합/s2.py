import sys
sys.stdin = open("input.txt")

T = int(input())
arr = [i for i in range(1, 13)] # 1~12 집합

for tc in range (1, T+1):
    num, total = map(int, input().split())
    ans = 0 # 해당되는 경우 수
    for i in range(1, 1<<num):
        sum_num = 0 # 부분집합의 합
        x = 0 # 부분집합 내 원소의 개수
        for j in range(num):
            if i & (1 << j):
                sum_num += arr[j]
                x += 1 # 부분 집합 내 원소 개수 + 1
        if x == num and sum_num == total: # 부분 집합 내 원소 원소 수가 맞고, 부분 집합의 합이 total 이라면
            ans += 1
    print(f"#{tc} {ans}")
import sys
sys.stdin = open('input.txt')

T = int(input())
print(T)
for i in range(1, T+1):
    arr = list(map(int, input().split()))
    sum_arr = 0
    for j in arr:
        sum_arr += j
    avg = round(sum_arr / len(arr))
    print(f"#{i} {avg}")
import sys
sys.stdin = open('input.txt')


for j in range(1, 11):
    T = int(input())
    my_list = list(map(int, input().split()))
    cnt = 0
    for i in range(2, T-2):
        d1 = my_list[i] - my_list[i-1]
        d2 = my_list[i] - my_list[i-2]
        u1 = my_list[i] - my_list[i+1]
        u2 = my_list[i] - my_list[i+2]
        if d1 > 0 and d2 > 0 and u1 > 0 and u2 > 0:
            cnt += min(d1, d2, u1, u2)
        else: continue
    print(f'#{j} {cnt}')
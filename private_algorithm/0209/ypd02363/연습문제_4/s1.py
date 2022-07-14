import sys
sys.stdin = open('input.txt')

def gin(arr):
    cnt_list = [0] * 10
    cnt = 0
    for i in range(len(arr)):
        cnt_list[arr[i]] += 1

    for i in range(len(cnt_list)):
        if cnt_list[i] >= 3:
            cnt += 1
            cnt_list[i] -= 3
            if cnt_list[i] == 3:
                return 1

    for i in range(1, len(cnt_list)-1):
        if cnt_list[i-1] == cnt_list[i] == cnt_list[i+1] and cnt_list[i] != 0:
            cnt += 1
            cnt_list[i-1] -= 1
            cnt_list[i] -= 1
            cnt_list[i+1] -= 1
            if cnt_list[i-1] == cnt_list[i] == cnt_list[i+1] and cnt_list[i] != 0:
                return 1
    if cnt >= 2:
        return 1
    return 0

T = int(input())

for i in range(1, T+1):
    num_list = []
    arr = list(map(int, input()))
    print(gin(arr))


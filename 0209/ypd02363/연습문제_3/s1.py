import sys
sys.stdin = open('input.txt')

def bubble(arr):
    cnt_arr = []
    cnt = 1

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            cnt += 1
        else:
            cnt_arr.append(cnt)
            cnt = 0
    cnt_arr.append(cnt)
    max_num = cnt_arr[0]
    for i in cnt_arr:
        if i > max_num:
            max_num = i
    return max_num


T1 = int(input())
for i in range(1, T1+1):
    T2 = int(input())
    arr = list(map(int, input().split()))
    print(bubble(arr))

import sys
sys.stdin = open('input.txt')

def count_num(arr, asd):
    cnt_list = [0]*10
    for i in range(len(arr)):
        cnt_list[arr[i]] += 1
    if max(cnt_list) == 1:
        return f"#{asd} {cnt_list.index()} {1}"
    return f"#{asd} {cnt_list.index(max(cnt_list))} {max(cnt_list)} "

T = int(input())
for asd in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))
    print(count_num(arr, asd))


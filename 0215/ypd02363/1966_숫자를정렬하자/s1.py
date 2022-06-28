import sys
sys.stdin = open("input.txt")

# 1. 선택
def nsort(arr):
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[idx] > arr[j]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

# 2. 버블
def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 3. 카운팅
def counting(arr):
    cnt_list = [0] * (max(arr)+1)
    for i in range(len(arr)):
        cnt_list[arr[i]] += 1
    for i in range(1, len(cnt_list)):
        cnt_list[i] = cnt_list[i] + cnt_list[i-1]
    ans_list = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        ans_list[cnt_list[arr[i]] - 1] = arr[i]
        cnt_list[arr[i]] -= 1
    return ans_list

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    narr = counting(arr)
    print(f"#{tc}", end=' ')
    for i in range(len(narr)):
        print(narr[i], end=' ')
    print()

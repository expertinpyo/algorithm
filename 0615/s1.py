# 1838
# 버블 정렬

n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    btn = True
    for j in range(i, n-1):
        if arr[j] > arr[j+1]:
            [j], arr[j+1] = arr[j+1], arr[j]arr
            btn = False
    if btn:
        print(cnt)
        break
    cnt += 1
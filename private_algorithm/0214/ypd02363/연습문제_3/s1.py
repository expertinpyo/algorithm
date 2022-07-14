import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))

for i in range(1, 1<<len(arr)): # 2**len(arr) = 64, 공집합 제외(index 0 포함 x)
    for j in range(len(arr)):
        # print(1<<j)
        if i & (1<<j): # 이진수와 i가 같다면?
            print(arr[j], end=' ')
    print()



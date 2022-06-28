import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    print(f"{tc} {max(arr) - min(arr)}")


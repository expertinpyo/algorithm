import sys
sys.stdin = open('input.txt')

def finding_room(arr):
    ans = 1
    for i in range(1, len(arr)):
        if not (arr[i][0] > arr[i-1][0] and arr[i][0] > arr[i-1][1] and arr[i][1] > arr[i][0]) or (arr[i][0] > arr[i-1][0] and abs(arr[i][0]-arr[i-1][1]) == 1 and arr[i][1] > arr[i][0]):
            ans += 1
    return ans
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{tc} {finding_room(arr)}")
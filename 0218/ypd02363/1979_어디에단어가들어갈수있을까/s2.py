import sys
sys.stdin = open("input.txt")

def puzzle(arr, n, k):
    num_of_blank = 0
    for i in range(n):
        if arr[i].count('1') >= k:
            target = ''.join(arr[i])
            target = target.split('0')
            pattern = '1'*k
            num_of_blank += target.count(pattern)
    return num_of_blank

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr_h = [list(input().split()) for _ in range(n)]
    arr_v = list(zip(*arr_h))
    puzzle_h = puzzle(arr_h, n, k)
    puzzle_v = puzzle(arr_v, n, k)
    print(f"#{tc} {puzzle_h + puzzle_v}")
    
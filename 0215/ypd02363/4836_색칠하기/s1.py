import sys

sys.stdin = open("input.txt")

def colored(arr):
    x1 = arr[0]
    x = arr[2] - arr[0]
    y1 = arr[1]
    y = arr[3] - arr[1]
    new_arr = [[0]*(x+1) for _ in range(y+1)]
    for i in range(x+1):
        for j in range(y+1):
            new_arr[j][i] = [y1 + j, x1 + i]
    return new_arr


T = int(input())
for tc in range(1, T + 1):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(number)]
    new_arr = []
    for i in range(number):
        new_arr.append(colored(arr[i]))
    print(new_arr)

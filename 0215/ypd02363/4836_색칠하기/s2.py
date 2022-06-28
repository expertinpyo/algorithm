import sys
sys.stdin = open("input.txt")

def colored(arr):
    empty_box = [[0]*10 for _ in range(10)]
    for i in arr:
        x1 = i[0]
        x2 = i[2]
        y1 = i[1]
        y2 = i[3]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                empty_box[x][y] += i[-1]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if empty_box[i][j] == 3:
                cnt += 1
    return cnt

sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T + 1):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(number)]
    print(f"{tc} {colored(arr)}")
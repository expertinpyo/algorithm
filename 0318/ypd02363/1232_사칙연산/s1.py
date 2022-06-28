import sys
sys.stdin = open('input.txt')

def calculation(x):
    if x:
        left = calculation(table[x][0])
        right = calculation(table[x][1])
        if table[x][3] in cal:
            if table[x][3] == '+':
                table[x][3] = left + right
            elif table[x][3] == '-':
                table[x][3] = left - right
            elif table[x][3] == '*':
                table[x][3] = left * right
            elif table[x][3] == '/':
                table[x][3] = left / right
        return table[x][3]

    return table[x][3]

for tc in range(1, 11):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]
    cal = ['+', '-', '*', '/']
    table = [[0]*4 for _ in range(n+1)]
    for i in range(n):
        parent = int(arr[i][0])
        if len(arr[i]) == 4:
            ch1, ch2 = int(arr[i][2]), int(arr[i][3])
            table[parent][0], table[parent][1] = ch1, ch2
            table[ch1][2] = table[ch2][2] = parent
        if arr[i][1] in cal:
            table[parent][3] = arr[i][1]
        else:
            table[parent][3] = int(arr[i][1])
    print(f"#{tc} {int(calculation(1))}")


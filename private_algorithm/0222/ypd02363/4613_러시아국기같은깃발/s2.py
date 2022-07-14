import sys
sys.stdin = open("input.txt")

def russia(arr, n, m):
    stack = []
    for i in range(1, n-1):
        cnt_w = arr[i].count('W')
        cnt_r = arr[i].count('R')
        cnt_b = arr[i].count('B')
        stack.append([m-cnt_w, m-cnt_b, m-cnt_r])
    w_stack = ['w']
    b_stack = ['b']

    w_ans = b_ans = 0

    for i in range(1, n-2):
        mins = min(stack[i])
        if stack[i].index(mins) == 0 and stack[-1] != 'b' or 'r':
            w_stack.append('w')
        elif stack[i].index(mins) == 1 and stack[-1] != 'r':
            w_stack.append('b')
        else:
            w_stack.append('r')

    for i in range(1, n-2):
        mins = min(stack[i])
        if stack[i].index(mins) == 0 and stack[-1] != 'b' or 'r':
            b_stack.append('w')
        elif stack[i].index(mins) == 1 and stack[-1] != 'r':
            b_stack.append('b')
        else:
            b_stack.append('r')

    if w_stack[-1] == 'w':
        w_stack.pop()
        w_stack.append('b')

    w_ans = 2 * m - (arr[0].count('W') + arr[-1].count('R'))
    for i in range(n-2):
        if w_stack[i] == 'w':
            w_ans += stack[i][0]
        elif w_stack[i] == 'b':
            w_ans += stack[i][1]
        else:
            w_ans += stack[i][2]
    b_ans = 2 * m - (arr[0].count('W') + arr[-1].count('R'))
    for i in range(n-2):
        if b_stack[i] == 'w':
            b_ans += stack[i][0]
        elif b_stack[i] == 'b':
            b_ans += stack[i][1]
        else:
            b_ans += stack[i][2]
    return min(b_ans, w_ans)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    print(f"#{tc} {russia(arr, n, m)}")
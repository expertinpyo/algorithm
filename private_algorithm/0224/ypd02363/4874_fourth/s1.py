import sys
sys.stdin = open('input.txt')

def forth(s):
    stack = []
    try:
        for i in s:
            if not i in operator:
                if i == '.':
                    if len(stack) == 1:
                        return stack.pop()
                    else: return 'error'
                else:
                    stack.append(int(i))
            else:
                a2 = stack.pop()
                a1 = stack.pop()
                if i == '+':
                    stack.append(a1 + a2)
                elif i == '-':
                    stack.append(a1 - a2)
                elif i == '*':
                    stack.append(a1 * a2)
                elif i == '/':
                    stack.append(a1 // a2)
    except:
        return 'error'

T = int(input())
for tc in range(1, T+1):
    s = list(input().split())
    operator = ['+', '-', '/', '*']
    print(f"#{tc} {forth(s)}")

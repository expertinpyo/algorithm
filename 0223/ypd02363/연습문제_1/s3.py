import sys
sys.stdin = open('input3.txt')

T = int(input())
for tc in range(1, T+1):
    # 아래에 코드를 작성해주세요.
    s = input()
    stack = []
    operator = ['*', '/', '+', '-']
    for i in s:
        if not i in operator:
            stack.append(i)
        else:
            num2 = float(stack.pop())
            num1 = float(stack.pop())
            if i == '*':
                stack.append(num1 * num2)
            elif i == '/':
                stack.append(num1 / num2)
            elif i == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 - num2)
    print(f"{tc} {stack.pop()}")
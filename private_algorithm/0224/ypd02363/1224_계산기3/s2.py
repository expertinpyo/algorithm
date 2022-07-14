import sys
sys.stdin = open('input.txt')

def first(s):
    stack = []
    ans = ''
    for i in s:
        if i == '(':
            stack.append(i)
        elif i in operator:
            if not stack or stack[-1] == '(':
                stack.append(i)
            elif stack[-1] == '*':
                if i == '*':
                    ans += stack.pop()
                    stack.append(i)
                else:
                    for j in range(len(stack)):
                        ans += stack.pop()
                        if not stack or stack[-1] == '(':
                            stack.append(i)
                            break
                        elif i == '+':
                            ans += stack.pop()
                            stack.append(i)
                            break
            elif stack[-1] == '+':
                if i == '*':
                    stack.append(i)
                else:
                    ans += stack.pop()
                    stack.append(i)
        elif i == ')':
            for j in range(len(stack)):
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    ans += stack.pop()

        else:
            ans += i
    if stack:
        for i in stack:
            ans += i
    return ans
def second(ans):
    stack = []
    for i in ans:
        if not i in operator:
            stack.append(int(i))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                stack.append(num1+num2)
            else:
                stack.append(num1*num2)
    return stack.pop()
for tc in range(1, 11):
    number = int(input())
    s = input()
    operator = ['+', '*']
    a = first(s)
    b = second(a)
    print(f"#{tc} {b}")
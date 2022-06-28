import sys
sys.stdin = open('input.txt')

def middle(s):
    operator1 = ['+', '-']
    operator2 = ['*', '/']
    stack = []
    ans = ''
    for i in s:
        if i in operator1 or i in operator2:
            if not stack:                   # i가 연산자라면
                stack.append(i)             # 스택이 비어있다면 push
            else:                           # 비어있지 않다면
                if stack[-1] in operator2:    # 스택의 마지막 연산자가 우선순위 2에 있다면
                    if i in operator1:          # 만약 i가 연산자 1 이라면
                        for j in range(len(stack)): # 스택 길이만큼
                            ans += stack.pop()  # 스택 마지막 요소 pop
                            if not stack:
                                stack.append(i)
                                break
                            elif stack[-1] in operator1:  # 그 다음 마지막 요소가 operator 1에 있다면 break
                                ans += stack.pop()
                                stack.append(i)
                                break               # 출력 후 push
                    else:
                        ans += stack.pop()
                        stack.append(i)           # operator 2에 있다면 push
                else:
                    if i in operator2:
                        stack.append(i)
                    else:
                        ans += stack.pop()
                        stack.append(i)
        else:
            ans += i
    for i in range(len(stack)):
        ans += stack.pop()
    return ans

def backward(s):
    stack = []
    operator = ['*', '/', '+', '-']
    for i in s:
        if not i in operator:
            stack.append(i)
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if i == '*':
                stack.append(num1 * num2)
            elif i == '/':
                stack.append(num1 / num2)
            elif i == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 - num2)
    return stack.pop()
for tc in range(1, 11):
    number = int(input())
    s = input()
    mid = middle(s)
    back = backward(mid)
    print(f"#{tc} {back}")
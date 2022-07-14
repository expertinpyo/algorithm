import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T+1):
    # 아래에 코드를 작성해주세요.
    operator1 = ['+', '-']
    operator2 = ['*', '/']
    s = input()
    stack = []
    ans = ''
    for i in s:
        if i == '(':                        # 여는 괄호
            stack.append(i)                 # 무조건 push
        elif i in operator1 or i in operator2:
            if not stack:                   # i가 연산자라면
                stack.append(i)             # 스택이 비어있다면 push
            else:                           # 비어있지 않다면
                if stack[-1] == '(':        # top이 열린 괄호라면
                    stack.append(i)         # 무조건 push
                elif stack[-1] in operator2:    # 스택의 마지막 연산자가 우선순위 2에 있다면
                    if i in operator1:          # 만약 i가 연산자 1 이라면
                        for j in range(len(stack)): # 스택 길이만큼
                            ans += stack.pop()      # 스택 마지막 요소 pop
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
        elif i == ')':
            for j in range(len(stack)):       # 닫힌 괄호일 시 len(stack)만큼
                if stack[-1] == '(':          # 스택의 마지막이 열린 괄호라면 pop 후 break
                    stack.pop()
                    break
                else:
                    ans += stack.pop()        # 아니라면 출력
        else:
            ans += i
    for i in range(len(stack)):
        ans += stack.pop()
    print(f"{tc} {ans}")
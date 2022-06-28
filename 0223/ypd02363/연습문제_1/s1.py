"""
수식 문자열을 읽어서 피연산자는 바로 출력하고
연산자는 stack에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(활용하는 연산자는 +*/-)

2+3*4/5 -> 2345/*+
"""

import sys
sys.stdin = open('input.txt')

# 아래에 코드를 작성해주세요.
s = input()
operater = ['*', '/', '+', '-']
stack = []
ans = ''
for i in s:
    if i in operater:
        stack.append(i)
    else:
        ans += i
for i in range(len(stack)):
    ans += stack.pop()
print(ans)
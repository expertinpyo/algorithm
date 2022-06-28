import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    sentence = input()
    stack = []
    ans = 0
    for i in range(len(sentence)):
        if sentence[i] == '(':
            stack.append('(')
        elif sentence[i] == ')':
            stack.pop()
            if sentence[i-1] == '(':
                ans += len(stack)
            elif sentence[i-1] == ')':
                ans += 1
    print(f"#{tc} {ans}")
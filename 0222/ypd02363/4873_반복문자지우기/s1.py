import sys
sys.stdin = open("input.txt")

def removal(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if not stack:
            stack.append(s[i])
        elif s[i] == stack[-1]:
            stack.pop()
            continue
        else:
            stack.append(s[i])
    return len(stack)

T = int(input())
for tc in range(1, T+1):
    s = input()
    print(f"{tc} {removal(s)}")

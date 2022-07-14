import sys
sys.stdin = open("input.txt")

def password(n, s):
    stack = []
    for i in range(n):
        if not stack:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
            continue
        else:
            stack.append(s[i])
    ans = ''
    for i in stack:
        ans += i
    return ans
for tc in range(1, 11):
    n, s = input().split()
    n = int(n)

    print(f"#{tc} {password(n, s)}")
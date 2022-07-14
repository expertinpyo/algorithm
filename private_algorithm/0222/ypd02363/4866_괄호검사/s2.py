import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    sentence = input()
    stack = []
    ans = 1
    for i in range(len(sentence)):
        if sentence[i] == "(" or sentence[i] == "{":
            stack.append(sentence[i])
        elif sentence[i] == ")":
            if not stack:
                ans = 0
                break
            if stack.pop() != "(":
                ans = 0
                break
        elif sentence[i] == "}":
            if not stack:
                ans = 0
                break
            if stack.pop() != "{":
                ans = 0
                break
    if stack:
        ans = 0
    print(f"#{tc} {ans}")
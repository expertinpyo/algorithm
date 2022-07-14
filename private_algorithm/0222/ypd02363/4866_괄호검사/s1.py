import sys
sys.stdin = open("input.txt")
T = int(input())

# 신경써야하는 부분 : 괄호 안에 제대로 괄호가 들어가 있는지 {}, ()
# 괄호가 '' 안에 있는지

for tc in range(1, T+1):
    sentence = input()
    arr = ["{", "("]
    stack = []
    ans = 10

    for i in range(len(sentence)):
        if sentence[i] == "'":
            for j in range(i+1, len(sentence)):
                if not sentence[j] == "'":
                    continue
                if sentence[j] in arr:
                    stack.append(sentence[j])
                elif sentence[j] == '}':
                    if stack.pop() == '(':
                        ans = 0
                        break
                elif sentence[j] == ')':
                    if stack.pop() == '{':
                        ans = 0
                        break
            break
        else:
            if sentence[i] in arr:
                stack.append(sentence[i])
            elif sentence[i] == '}':
                if stack.pop() == '(':
                    ans = 0
                    break
            elif sentence[i] == ')':
                if stack.pop() == '{':
                    ans = 0
                    break
    if ans == 0:
        print(f"#{tc} {ans}")
    else: print(f"#{tc} 1")
# 쇠막대는 자신보다 긴 막대기 위에만 놓일 수 있음
# 쇠 막대기를 다른 막대위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않게
# 각 쇠 막대를 자르는 레이저는 적어도 하나 존재
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음
# () > 레이저
# 레이저 수 +1 해주면 된다.
# stack을 활용하면 쉽게 풀 수 있을 것 같다.
# list의 append와 pop은 일종의 stack 이므로 이를 활용하면 좋을 듯 싶다는 생각을 했다.
# a면 +1 / (면 새로운 리스트에 그 인덱스를 append / )면 그 인덱스 위치까지 가서 a개수 센 다음 새로운 리스트 pop
# 지금 현 코드의 문제점은 (를 만나면 바로 함수가 종료된다. 그 부분을 리스트 화 시켜서 그 리스트에서 (를 제거하는 방법도 좋거나 그냥 j까지 돌려서 닫는것도 좋다.
def raser(s):
    s = s.replace("()", 'a')
    print(s)
    idx = []
    ans = 0
    for i in range(len(s)):
        if s[i] == "(":
            idx.append(i)
        elif s[i] == 'a':
            ans += len(idx)
        elif s[i] == ')':
            ans += 1
            idx.pop()


    return ans

import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    sample = input()
    print(f"#{tc} {raser(sample)}")

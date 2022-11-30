import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    string = input().strip()
    cnt = 0
    for i in range(len(string)):
        if string[i] == '(':
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                cnt = -1
                break
    if cnt:
        print("NO")
    else:
        print("YES")
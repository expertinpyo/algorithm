import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    num = int(input())
    arr = [input() for _ in range(8)]
# 가로 먼저
    cnt = 0
    for i in range(8):
        for j in range(8-num+1):
            p = True
            for k in range(num//2):
                if arr[i][j+k] != arr[i][j+num-k-1]:
                    p = False
                    break
            if p:
                cnt +=1
    for i in range(8):
        for j in range(8-num+1):
            p = True
            for k in range(num//2):
                if arr[j+k][i] != arr[j+num-k-1][i]:
                    p = False
                    break
            if p:
                cnt +=1
    print(f"#{tc} {cnt}")
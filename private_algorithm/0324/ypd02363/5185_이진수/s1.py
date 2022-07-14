import sys
sys.stdin = open('input.txt')

asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

def convert(s):
    if s <= '9':
        return ord(s) - ord('0')
    else:
        return ord(s) - ord('A') + 10

def sixteen_to_binary(s):
    for k in range(4):
        t.append(asc[s][k])

T = int(input())
for tc in range(1, T+1):
    n, h = list(input().split())
    t = []
    for i in h:
        sixteen_to_binary(convert(i))
    ans = ''
    for a in t:
        ans += str(a)
    print(f"#{tc} {ans}")

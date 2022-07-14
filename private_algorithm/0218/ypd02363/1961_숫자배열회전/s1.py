import sys
sys.stdin = open("input.txt")

def first(arr, n):
    new_list = []
    for j in range(n):
        s = ''
        for i in range(n-1, -1, -1):
            s += str(arr[i][j])
        new_list.append(s)
    return new_list

def second(arr, n):
    new_list = []
    for j in range(n-1, -1, -1):
        empty = []
        s = ''
        for i in range(n-1, -1, -1):
            s += str(arr[j][i])
        new_list.append(s)
    return new_list

def third(arr, n):
    new_list = []
    for j in range(n-1, -1, -1):
        s = ''
        for i in range(n):
            s += str(arr[i][j])
        new_list.append(s)
    return new_list

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a = first(arr, n)
    b = second(arr, n)
    c = third(arr, n)
    ans = []
    for i in range(n):
        ans.append([a[i], b[i], c[i]])
    print("#%d"%tc)
    for i in ans:
        print(*i)
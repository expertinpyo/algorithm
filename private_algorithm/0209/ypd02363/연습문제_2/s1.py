import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split())

arr_1 = []
for i in range(a):
    arr_1.append(list(map(int, input().split())))

print(arr_1)
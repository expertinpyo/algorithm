import sys
sys.stdin = open('input.txt')

T = int(input())
print(T)

my_list = list(map(int, input().split()))
print(my_list)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print(arr)

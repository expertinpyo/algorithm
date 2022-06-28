import sys
sys.stdin = open('input.txt')

def baby_gin(li):
    sorted_list = sorted(li)
    for i in range(0,3):
        if sorted_list[i] == sorted_list[i+1]:
        else: break
    for i in range(3,5):
        if sorted_list[i] == sorted_list[i + 1]:
        else: break
T = int(input())

for i in range(T):
    num_list = []
    a = ','.join(input()).split(',')
    for j in a:
        j = int(j)
        num_list.append(j)
    print(baby_gin(num_list))
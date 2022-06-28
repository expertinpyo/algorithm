import sys
sys.stdin = open('input.txt')
odd_num_list = ['ZRO', 'ONE','TWO', 'THR','FOR','FIV',
                'SIX','SVN','EGT','NIN']

T = int(input())
for tc in range(T):
    case, length = input().split()
    arr = input().split()
    real_num_list = [0] * int(length)
    for i in range(int(length)):
        if arr[i] in odd_num_list:
            real_num_list[i] = odd_num_list.index(arr[i])
    real_num_list.sort()
    ans_list = [0] * int(length)
    for i in range(int(length)):
        ans_list[i] = odd_num_list[real_num_list[i]]
    print(case)
    for i in ans_list:
        print(i, end=' ')
    print()

"""
연습문제 2. 부분 집합의 합 구현

2-2) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2}의 모든 부분 집합 중 원소의 합이 0이 되는 부분집합 구하기

** 비트 연산
- 원소 수에 해당하는 N개의 비트열을 활용
- n번째 비트값이 1이면 n번째 원소가 '포함'되었음을 의미

0   0 0 0 0   {A, B, C, D}
1   0 0 0 1   {A}
2   0 0 1 0   {B}
3   0 0 1 1   {B, A}
...........
14  1 1 1 0   {D, C, B}
15  1 1 1 1   {D, C, B, A}
"""


# 1. 재귀 활용
def print_set(n):
    global cnt_subset
    sum_of_subset = 0
    for i in range(n):
        if check[i] == 1:
            sum_of_subset += nums[i]

    if sum_of_subset == 0:
        cnt_subset += 1
        print('{}: '.format(cnt_subset), end='')

        for i in range(n):
            if check[i] == 1:
                print('{} '.format(nums[i]), end='')
        print()


def powerset(n, k):
    if n == k:
        print_set(n)
    else:
        check[n] = 1
        powerset(n + 1, k)
        check[n] = 0
        powerset(n + 1, k)


cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]

powerset(0, N)

print('------------------------------------------------')

# 2-1. 비트 연산 활용
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)

for i in range(1 << N):
    my_sum = []
    for j in range(N):
        if i & (1 << j):
            my_sum.append(nums[j])
    if sum(my_sum) == 0:
        print(*my_sum)

print('------------------------------------')

# 2-2. 비트 연산 활용
nums2 = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums2)

for i in range(1 << N):
    my_sum = 0
    for j in range(N):
        if i & (1 << j):
            my_sum += nums2[j]
    if my_sum == 0:
        for j in range(N):
            if i & (1 << j):
                print(nums[j], end=' ')
        print()
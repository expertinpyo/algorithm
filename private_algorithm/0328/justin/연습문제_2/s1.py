"""
연습문제 2. 부분 집합 구현

2-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""

def print_set(n):
    global cnt_subset
    cnt_subset += 1
    print('{}: '.format(cnt_subset), end='')

    for i in range(n):
        if check[i] == 1:
            print(nums[i], end=' ')
    print()

def powerset(n, k):
    if n == k:
        print_set(n)
    else:
        check[n] = 1
        powerset(n+1, k)
        check[n] = 0
        powerset(n+1, k)


cnt_subset = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]
powerset(0, N)
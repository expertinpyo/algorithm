"""
연습문제 2. 부분 집합 구현

2-1) {-1, 3, -9, 6, 7, -6, 1, 5, 4, -2} 의 모든 부분 집합 구하기
"""
def print_set(n):
    global cnt
    cnt += 1
    print(f'{cnt} : ', end='')
    for i in range(n):
        if check[i]:
            print(nums[i], end=' ')
    print()

def powerset(n, l):
    if n == l:
        print_set(n)
    else:
        check[n] = 1
        powerset(n+1, l)
        check[n] = 0
        powerset(n+1, l)

cnt = 0
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(nums)
check = [0 for _ in range(N)]
powerset(0, N)

"""
-1 3 -9 6 7 -6 1 5 4 -2 
-1 3 -9 6 7 -6 1 5 4 
-1 3 -9 6 7 -6 1 5 -2 
-1 3 -9 6 7 -6 1 5 
-1 3 -9 6 7 -6 1 4 -2 
-1 3 -9 6 7 -6 1 4 
-1 3 -9 6 7 -6 1 -2 
-1 3 -9 6 7 -6 1 
-1 3 -9 6 7 -6 5 4 -2 
-1 3 -9 6 7 -6 5 4 
-1 3 -9 6 7 -6 5 -2 
-1 3 -9 6 7 -6 5 
-1 3 -9 6 7 -6 4 -2 
...
"""
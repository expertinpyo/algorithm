"""
연습문제 1. 순열

1-3) 5개의 숫자 중 3자리의 순열 생성하기
[1, 2, 3, 4, 5]에서 3자리의 순열을 재귀 함수를 활용하여 구현하시오.
"""

def perm(n, k, m):
    if n == k:
        for i in range(k):
            print(nums[i], end=' ')
        print()
    else:

        for i in range(n, m):
            nums[n], nums[i] = nums[i], nums[n]
            perm(n+1, k, m)
            nums[n], nums[i] = nums[i], nums[n]

nums = [1, 2, 3, 4, 5]
perm(0, 3, len(nums))

print('#########################')

# visited 버전
def perm(i, n, k):
    if i == k:
        print(*p)
    else:
        for j in range(n):
            if not u[j]:
                u[j] = 1
                p[i] = nums[j]
                perm(i+1, n, k)
                u[j] = 0

nums = [1, 2, 3, 4, 5]
N = len(nums)
K = 3
u = [0] * N
p = [0] * K
perm(0, N, K)
"""
연습문제 1. 순열

1-2) 재귀로 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 재귀 함수를 활용하여 구현하시오.

** 각 자리를 어떻게 확정 시킬 것인가에 초점을 맞춰 구현해보세요.
** swap하는 방식과 방문 처리를 하는 방식으로 모두 구현해보세요.
"""

"""
    n = 0                            |1|2|3|
                            /           |             \
    n = 1           |1|2|3|          |2|1|3|        |3|2|1|
                    /    \           /     \        /     \
    n = 2       |1|2|3| |1|3|2|  |2|1|3| |2|3|1| |3|2|1| |3|1|2|

                          자리가 확정되면 출력(n == k)  
"""


# 1. swap
def perm_swap(n, k):
    if n == k:
        print(*nums)
    else:
        for i in range(n, k):
            nums[n], nums[i] = nums[i], nums[n]
            perm_swap(n+1, k)
            nums[n], nums[i] = nums[i], nums[n]

nums = [1, 2, 3]
perm_swap(0, len(nums))

print('---------------------------------------')


# 2. visited
def perm_visited(k):
    if n == k:
        print(*sel)
    else:
        for i in range(n):
            if visited[i]: continue
            visited[i] = 1
            sel[k] = nums[i]
            perm_visited(k+1)
            visited[i] = 0

nums = [1, 2, 3]
n = len(nums)
visited = [0] * n
sel = [0] * n
perm_visited(0)
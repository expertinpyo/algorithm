# n개에 대한 순열
from itertools import permutations

n = int(input())
nums = []
for _ in range(n):
    nums.append(input())
k = int(input())
checked = []
arrs = list(permutations(nums, n))

p = 0
q = 0
for arr in arrs:
    num = ''
    for a in arr:
        num += a
    num = int(num)
    if num not in checked:
        q += 1
        checked.append(num)
        if not num % k:
            p += 1
print(p, q)

# num이 k로 나누어 떨어지는 순열을 구해야 한다
# 정답을 맞출 확률을 분수로 출력해라


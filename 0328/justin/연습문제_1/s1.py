"""
연습문제 1. 순열

1-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

nums = [1, 2, 3]

for i in nums:
    for j in nums:
        if i != j:
            for k in nums:
                if j != k and i != k:
                    print(i, j, k)
"""
연습문제 1. 순열

1-1) 단순하게 순열 생성하기
[1, 2, 3]을 포함하는 모든 순열을 반복문을 활용하여 구현하시오.
"""

nums = [1, 2, 3]

for i in range(3):
    for j in range(3):
        for k in range(3):
            if len({i, j, k}) == 3:
                print(nums[i], nums[j], nums[k])

"""
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""
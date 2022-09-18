nums = [True] * 1000001
for i in range(2, 1001):
    if nums[i]:
        for j in range(2*i, 1000001, i):
            nums[j] = False
while True:
    n = int(input())
    if not n:
        break
    for i in range(3, n, 2):
        if nums[i] and nums[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
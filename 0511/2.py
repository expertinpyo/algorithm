# 13549
# bfs 느낌이 난다
n, k = map(int, input().split())
idx = 1
numlist = []
while True:
    if n * idx < k:
        numlist.append(n*idx)
        idx *= 2
    else:
        numlist.append(n*idx)
        break
inf = float('inf')
nums = [inf] * (idx*n + 2)
for i in range(len(numlist)):
    nums[numlist[i]] = 0
    nums[numlist[i]-1] = nums[numlist[i]+1] = 1
    if i == len(numlist) -1:
        break
    elif i == 0:
        for j in range(numlist[0]-2, -1, -1):
            nums[j] = nums[j+1] + 1
    else:
        # 여기서부턴 홀수 짝수로 나눠서 짝수를 먼저 배치한 후 홀수를 배치하는 게 좋을 듯
        if numlist[i] % 2:
            start = numlist[i] + 1
        else:
            start = numlist[i] + 2
        for j in range(start, numlist[i+1], 2):
            nums[j] = min(nums[j], j-numlist[i], numlist[i+1]-j, nums[j//2])


print(nums)
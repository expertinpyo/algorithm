# n개의 물곤
# 각 물건은 무게 w 가치 v를 가짐
# 준서가 v만큼 즐길 수 있음
# 최대 k만큼 배낭에 넣을 수 있음
def dfs(i):
    stack = [arr[i]]

    while stack:
        nx, nk = stack.pop()
        if nx != arr[i][0] and nk != arr[i][1]:
            

n, k = map(int,input().split())
arr = []
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
arr.sort()
for i in range(n):
    dfs(i)
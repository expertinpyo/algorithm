def dfs(x, y):
    global ans
    for d in di:
        nx = x + d[1]
        ny = y + d[0]
        if 0 <= nx < r and 0 <= ny < c:
            if not alphabet[ord(arr[nx][ny])-65]:
                alphabet[ord(arr[nx][ny])-65] = 1
                dfs(nx, ny)
                alphabet[ord(arr[nx][ny])-65] = 0
            else:
                ans = max(sum(alphabet), ans)
# 가지치기가 들어가야 할 것 같다

r, c = map(int, input().split())
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
arr = [list(input()) for _ in range(r)]
alphabet = [0 for _ in range(26)]
for i in range(r):
    for j in range(c):
        alphabet[ord(arr[i][j])-65] += 1
if max(alphabet) == 1:
    ans = r * c
else:
    ans = 0
    alphabet = [0 for _ in range(26)]
    alphabet[ord(arr[0][0])-65] = 1
    dfs(0, 0)
print(ans)
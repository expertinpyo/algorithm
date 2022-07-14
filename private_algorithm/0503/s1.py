# 15684 사다리 조작
# 완전 탐색으로 접근하면 좋을 듯

n, m, h = map(int, input().split())
arr = [[0]*n for _ in range(h)]
for i in range(1, m+1):
    a, b = map(int, input().split())
    arr[a][b] = 1
print(arr)
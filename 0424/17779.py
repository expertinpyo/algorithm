# 1번 선거구 : 1 <= r < x + d1 // 1 <= c <= y
# 2번 선거구 : 1 <= r < x + d2  // y < c <= n
# 3번 선거구 : x + d1 <= r <= n // 1 <= c < y-d1+d2
# 4번 선거구 : x+d2 < r < n // y-d1+d2 <= c <= n
# d1, d2 >= 1
# d1 < y
# 1 <= x < x+d1+d2 <= n // 1 <= y-d1 < y < y+d2 <= n

# x, y 는 기준점 = > 이동하는 점 아님
# d1,d2는 가변하는 길이


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
division = [[0]*n for _ in range(n)]

for x in range(n):
    for y in range(n):


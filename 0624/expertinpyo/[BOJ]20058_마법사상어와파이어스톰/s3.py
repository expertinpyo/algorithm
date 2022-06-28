# 축이 생긴다고 생각해보기
# 현재 좌표 기준으로 기준을 넘어가면 마이너스, 기준 전이면 플러스
#
def fire(n):
    alternative = [[0] * (2 ** N) for _ in range(2 ** N)]
    if not n:
        alternative = arr
    num = 2 ** n
    # 경계가 있을 것임
    # 0 ~ 3 // 4~ 7
    length = num // 2
    for i in range(2**(N-n)):
        for j in range(2**(N-n)):
            x = i * num
            y = j * num
            for xx in range(x, x + num):
                for yy in range(y, y + num):
                    if


di = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
spells = list(map(int, input().split()))

for spell in spells:
    arr = fire(spell)
print(arr)
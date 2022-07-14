# 그 union과 함께 쓰이는 알고리즘 생각해보기
# 서로 알고있다면 그것을 갱신해서 할 수 있는 방법이 있음
import sys
sys.stdin = open('input.txt')

def make_set(x):
    p[x] = x

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    group = [[0] * (n+1) for _ in range(n+1)]

    p = [0]*(n+1)
    for i in range(1, n+1):
        make_set(i)

    visited = [0]*(n+1)
    for _ in range(m):
        x, y = map(int, input().split())
        union(x, y)

    pp = sorted(list(set(p)))
    for i in range(1, len(pp)):
        if p[pp[i]] != pp[i]:
            for j in range(1, n+1):
                if p[j] == pp[i]:
                    p[j] = p[pp[i]]
    pp = sorted(list(set(p)))
    print(f"#{tc} {len(pp)-1}")


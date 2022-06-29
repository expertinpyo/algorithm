"""
각 구역은 다섯 개의 선거구 중 하나에 속해야 함
선거구는 구역을 최소 하나 포함해야 함
한 선거구 포함되어 있는 구역은 모두 연결되어야 함

선거구 나누기
d1, d2 정하기

d1, d2 ≥ 1,

1 ≤ x < x+d1+d2 ≤ N

1 ≤ y-d1 < y < y+d2 ≤ N

2 <= d1 + d2 <= N

1 <= x < x + d1+d2 = N
각 구역
1 : x, y ~ x+d1, y-d1
2 : x, y ~ x+d2, y+d2
3 : x+d1, y-d ~ x+d1+d2, y-d1+d2
4 : x+d2, y+d2 ~ x+d2+d1, y+d2-d1
5 : 나머지 포함되지 않은 구역

인구가 가장 많은 지역과 가장 적은 지역의 인구 차이의 최솟값 찾기
"""

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

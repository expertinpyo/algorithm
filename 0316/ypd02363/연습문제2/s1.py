"""
첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 '부모 -> 자식' 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위/중위/후회 순회하여 정점의 번호를 출력하시오.
13 -> 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

참고)
1) Tree에서는 정점의 개수만 알려줘도 간선 정보를 알 수 있음 (정정미 V개 일 때 간선은 V-1개)
2) 트리는 1차원 배열 / 2차원 배열 모두 표현이 가능하지만 이 문제는 2차원으로 접근 해보자
"""

# 전위 순회 (V -> L -> R)
def pre_order(node):
    if node:
        print(f'{node}', end=' ')
        pre_order(table[node][0])
        pre_order(table[node][1])


# 중위 순회 (L -> V -> R)
def in_order(node):
    if node:
        in_order(table[node][0])
        print(f'{node}', end=' ')
        in_order(table[node][1])


# 후위 순회 (L -> R -> V)
def post_order(node):
    if node:
        post_order(table[node][0])
        post_order(table[node][1])
        print(f'{node}', end=' ')

import sys
sys.stdin = open('input.txt')


v = int(input())
arr = list(map(int, input().split()))
table = [[0]*3 for _ in range(v+1)]

for i in range(v-1):
    parent, child = arr[i*2], arr[i*2+1]
    if not table[parent][0]:
        table[parent][0] = child
    else:
        table[parent][1] = child
    table[child][2] = parent

print(table)

print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()
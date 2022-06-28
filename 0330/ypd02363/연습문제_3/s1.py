"""
연습 문제3. 트리 순회
 문제3-1) 주어진 입력 정보를 활용하여 트리를 그려보고 각 순회 별로 어떤 순서로 노드를 방문하는지 작성하시오.

 문제3-2) 다음 이진 트리 표현에 대하여 전위/중위/후회 순회하여 정점의 번호를 출력하시오
     첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
     간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 '부모 자식' 순서로 표기된다.
     아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
     간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.
"""


# 전위 순회 (V -> L -> R)
def pre_order(node):
    if node:
        print(f"{node}", end=' ')
        pre_order(arr[node][0])
        pre_order(arr[node][1])


# 중위 순회 (L -> V -> R)
def in_order(node):
    if node:
        in_order(arr[node][0])
        print(f"{node}", end=' ')
        in_order(arr[node][1])


# 후위 순회 (L -> R -> V)
def post_order(node):
    if node:
        post_order(arr[node][0])
        post_order(arr[node][1])
        print(f"{node}", end=' ')

import sys

sys.stdin = open('input.txt')
n = int(input())
arr = [[0]*3 for _ in range(n+1)]
a = list(map(int, input().split()))
for i in range(n-1):
    if not arr[a[2*i]][0]:
        arr[a[2*i]][0] = a[2*i+1]
    else:
        arr[a[2*i]][1] = a[2*i+1]
    arr[a[2*i+1]][2] = a[2*i]


print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()
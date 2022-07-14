# 03/16 Tree

| No.  | Title       | Directory         |
| ---- | ----------- | ----------------- |
| 연습문제1 | 트리순회 손으로 그려보기 | `연습문제_1`   |
| 연습문제2 | 트리순회 코드 | `연습문제_2`   |
| 연습문제3 | 최소힙 | `연습문제_3`   |
| 1231 | 중위순회(HW) | `1231_중위순회`   |



## 연습문제 1

![binary_tree](README.assets/binary_tree.PNG)

**전위 순회(pre-order)**



**중위 순회(in-order)**



**후위 순회(post-order)**



## 연습문제 2

```python
# input.txt

13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
```

```python
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
    pass

# 중위 순회 (L -> V -> R)
def in_order(node):
    pass

# 후위 순회 (L -> R -> V)
def post_order(node):
    pass


import sys
sys.stdin = open('input.txt')

print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()
```



## 연습문제 3

```python
"""
** 최소힙의 조건 **
1. 완전 이진 트리
2. 자식 < 부모 (왼쪽 & 오른쪽 자식의 크기는 상관 없음)
"""

def heap_push(value):
    global heap_count
    pass                                 

def heap_pop():
    global heap_count
    pass

heap_count = 0
nums = [7, 2, 5, 3, 4, 6]
N = len(nums)
heap = [0] * (N+1)             # 크기 설정 (+1은 인덱스를 노드 번호에 맞추기 위해서 설정)

#1. heap push
for i in range(N):
    heap_push(nums[i])         # 인덱스 0번에 해당하는 노드부터 heap_push 연산 수행
print(*heap)                   # 0 2 3 5 7 4 6

#2. heap pop
for i in range(N):             # 삭제 -> 루트 노드
    print(heap_pop(), end=' ') # 2 3 4 5 6 7
```
# 0330 분할정복 & 백트래킹

| No.  | Title                        | Directory       |
| ---- | ---------------------------- | --------------- |
|      | 병합, 퀵 정렬                | `연습문제_1`    |
|      | 이진탐색                     | `연습문제_2`    |
|      | 트리 순회                    | `연습문제_3`    |
|      | 최소힙                       | `연습문제_4`    |
| 5204 | 병합정렬(HW)                 | `5204_병합정렬` |



## 연습문제_1

```python
"""
연습 문제1. 
"""

# 병합 정렬
def merge():
    pass

def partition():
    pass

numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)               # 정렬 전
print(partition(numbers))    # 정렬 후


# 퀵 정렬
def quick_sort():
    pass

def partition():
    pass

quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]
```

## 연습문제_2

```python
"""
연습 문제2. 이진 탐색
 - 이진 탐색을 반복문과 재귀 함수를 활용하여 구현하시오.
 - 찾고자 하는 값(target)이 있다면 해당 값의 인덱스를 없다면 -1을 반환하시오.
"""

#1. iteration
def binary_search_iteration():
    pass

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
target = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
# target = 90    # 없는 경우 -> -1


#2. recursion
def binary_search_recursion():
    pass

nums = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
target = 2       # 있는 경우 -> 해당 요소의 인덱스 반환
# target = 90    # 없는 경우 -> -1
```



## 연습문제_3

```python
# input.txt

13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
```

```python
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



## 연습문제_4
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

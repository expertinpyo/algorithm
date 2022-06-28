"""
** 최소힙의 조건 **
1. 완전 이진 트리
2. 자식 < 부모 (왼쪽 & 오른쪽 자식의 크기는 상관 없음)
"""

def heap_push(value):
    # 가장 마지막에 요소 삽입
    # 삽입된 노드와 부모 노드를 비교하여 swap
    # 부모 노드보다 크거나 작고, 루트 노드에 도달하기 전까지 반복
    global heap_count
    heap_count += 1
    heap[heap_count] = value
    child = heap_count
    parent = child // 2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


def heap_pop():
    global heap_count
    return_value = heap[1]
    heap[1] = heap[heap_count]
    heap[heap_count] = 0
    heap_count -= 1
    parent = 1
    child = parent * 2

    if child + 1 <= heap_count:
        if heap[child] > heap[child+1]:
            child = child + 1
    while child <= heap_count and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2

        if child + 1 <= heap_count:
            if heap[child] > heap[child]+1:
                child = child + 1

        return return_value



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
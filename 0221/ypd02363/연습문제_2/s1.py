def push(item):
    stack.append(item)

def pop():
    stack.pop()

def is_empty():
    if stack:
        return False
    return True

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    for i in data:
        if i == '(':
            push(i)
        else:
            if not is_empty():
                pop()
            else: return False
    if stack:
        return False
    return True
import sys
sys.stdin = open('input.txt')
stack = list() # []
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2)) # False
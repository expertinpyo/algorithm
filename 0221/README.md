# 02/21 Stack 1

| No.  | Title               | Directory             |
| ---- | ------------------- | --------------------- |
|      | Stack 구현          | `연습문제_1`          |
|      | 괄호매칭            | `연습문제_2`          |
|  | DFS 구현 | `연습문제_3` |
|  | function(recursive call) (문제 풀이 x - 참고용) | `연습문제_4` |
|  | memoization(문제 풀이 x - 참고용) | `연습문제_5` |
|  | dp (문제 풀이 x - 참고용) | `연습문제_6` |
| 5432 | 쇠막대기 자르기(재풀이)     | `5432_쇠막대기자르기` |
| 2005 | 파스칼의 삼각형(HW) | `2005_파스칼의삼각형` |



## 연습문제 1

```python
class Stack:
    def __init__(self, size):
        pass

    def is_empty(self):
        pass

    def is_full(self):
        pass

    def push(self, item):
        pass

    def peek(self):
        pass

    def pop(self):
        pass

    def __str__(self):
        result = '\n-----'
        for d in self.items:
            result = f'\n| {d} |' + result
        for _ in range(self.size - len(self.items)):
            result = f'\n|   |' + result
        return result
```





## 연습문제 2

```python
# input.txt

()()((()))
((()((((()()((()())((())))))
```

```python
"""
괄호 매칭
1. 괄호의 종류 - [], {}, () -> 단, 이번 연습문제에서는 소괄호만 존재
2. 괄호 매칭의 조건 
- 왼쪽 괄호의 개수와 오른쪽 괄호의 '개수'가 같아야 한다.
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 '먼저' 나와야 한다.
 - 괄호 사이에는 포함 관계만 존재한다.
3. 잘못된 사용의 예시
(a(b) -> 괄호 개수
a(b)c) -> 괄호 개수
a{b(c[d]e}) -> 괄호가 올바르게 매칭되지 않음
"""

def push(item):                 
    pass

def pop():
    pass

def is_empty():
    pass

def check_matching(data):           # 이 함수에서 push, pop, is_empty 활용
    pass

import sys
sys.stdin = open('input.txt')
stack = list() # []
data = input()
data2 = input()

print(check_matching(data))  # True
print(check_matching(data2)) # False
```



## 연습문제 3

```python
# input.txt

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```

```python
"""
1. dfs - 인접 행렬 - 반복
"""

def dfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# dfs 탐색 시작
dfs(1)
```

```python
"""
2. dfs - 인접 행렬 - 재귀
"""

def dfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# dfs 탐색 시작
dfs(1)
```

```python
"""
3. dfs - 인접 리스트
"""

def dfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# dfs 탐색 시작
dfs(1)
```



## 연습문제 4 (참고)

> 해당 코드를 복사하여 결과를 확인해보세요. 😀

``` python
# 디버거를 통해 결과를 확인해보세요
# print 결과는 디버거를 실행 시켰을 때 보이는 'Console'이라는 탭에서 확인 가능합니다.

def func2():
    print('함수 2 시작')
    print('함수 2 종료')

def func1():
    print('함수 1 시작')
    func2()
    print('함수 1 종료')

print('메인시작')
func1()
print('메인끝')

"""
메인시작
함수 1 시작
함수 2 시작
함수 2 종료
함수 1 종료
메인끝
"""
```

```python
# global 영역부터 각 함수의 고유한 영역을 디버거에서 확인해보세요!

n = 10

def f1(a):
    f2(a)

def f2(b):
    f3(b)

def f3(c):
    print(c**2)

f1(n) # 100
```

```python
# 반드시 디버거를 통해 결과를 확인해주세요!

def factorial(n):
    if n == 1:                # base case -> 종료 조건
        return 1
    return n * factorial(n-1) # 인자의 크기가 1씩 줄어감

print(factorial(5))

"""
Step 1. 
|  2 * factorial(1)  |
|  3 * factorial(2)  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

Step2.
2-1.
|  2 * 1  |
|  3 * factorial(2)  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

2-2.
|    |
|  3 * 2  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

2-3.
|    |
|    |
|  4 * 6 |
|  5 * factorial(4)  |
|  main  |

2-4.
|    |
|    |
|    |
|  5 * 24  |
|  main  |

2-5. 
|    |
|    |
|    |
|  120 반환 |
|  main  |

2-6. 끝
|    |
|    |
|    |
|    |
|    |
"""
```

```python
# 재귀로 배열의 각 요소 출력
# 반드시 디버거를 활용하여 결과를 확인해주세요!

a = [1, 2, 3]
N = len(a)

def f(i, N, a):
    if i == N:
        return # return None
    # else:
    print(a[i])
    f(i+1, N, a)
    # return이 없으면? None을 return

f(0, N, a)
```



## 연습문제 5 (참고)

> 해당 코드를 복사하여 결과를 확인해보세요. 😀

```python
import time
start = time.time()

# 재귀
def fibo_recursion(num):
    global cnt
    cnt += 1                            # 재귀 호출 횟수
    if num == 0 or num == 1:
        return num
    return fibo_recursion(num-1) + fibo_recursion(num-2)

cnt = 0
print(fibo_recursion(35), cnt)
# print(fibo_recursion(50))
print('Time: {}초'.format(time.time() - start))
```

```python
import time
start = time.time()

# 저장 공간을 만들어 놓은 상태에서 저장 (길이를 직접 지정)
def fibo(n):
    global cnt
    cnt += 1                            # 재귀 호출 횟수
    if memo[n] == -1:                   # 값을 아직 구하지 않은 경우
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 51 # n의 크기보다 1 크게 생성
memo[0] = 0
memo[1] = 1
cnt = 0

# print(memo)
print(fibo(35), cnt)
print('Time: {}초'.format(time.time() - start))
```

```python
import time
start = time.time()

# 저장 공간을 만들어 놓은 상태에서 저장 (길이를 직접 지정)
def fibo2(n):
    global cnt
    cnt += 1                            # 재귀 호출 횟수
    if n >= 2 and memo2[n] == 0:        # 아직 계산되지 않은 값이면
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

memo2 = [0] * 51
memo2[0] = 0
memo2[1] = 1
cnt = 0

# print(memo)
print(fibo2(50), cnt)
print('Time: {}초'.format(time.time() - start))
```



## 연습문제 6 (참고)

> 해당 코드를 복사하여 결과를 확인해보세요. 😀

```python
# dp - 피보나치
def fibo_dp(num):
    # 피보나치의 하위 -> 상위 결과값이 담길 리스트(테이블) 선언
    result = [0 for _ in range(num+1)]
    # 0항과 1항 값 넣어놓기
    result[0] = 0
    result[1] = 1

    # 두 번째 항부터 시작 (0항과 1항은 미리 계산)
    for i in range(2, num+1):
        # 기존에 리스트에 저장된 값을 그대로 활용
        result[i] = result[i-2] + result[i-1]

    # 마지막 항 반환
    return result[num]

print(fibo_dp(50))
```

```python
# dp - 팩토리얼
def fact(num):
    table[0] = 1

    for i in range(1, num+1):
        table[i] = i * table[i-1]

    return table[num]

n = 10
table = [0] * (n+1)
print(fact(n))
```
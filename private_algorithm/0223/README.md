# 02/23 Stack2

| No.       | Title       | Directory                                  |
| --------- | ----------- | ------------------------------------------ |
| 연습문제1 | 후위표기법  | `연습문제1_후위표기법`                     |
| 연습문제2 | 부분집합    | `연습문제2_부분집합`                       |
| 연습문제3 | 퀵정렬      | `연습문제3_퀵정렬` (`1966_숫자를정렬하자`) |
| 4871 | 그래프 경로 (Learn > Course > Stack1) | `4871_그래프경로` |
| 1219 | 길찾기 | `1219_길찾기` |
| 1223      | 계산기2(HW) | `1223_계산기2`                             |



## 연습문제1

```python
# input.txt

2+3*4/5
```

```python
# output.txt

2345/*+
```

```python
"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(활용하는 연산자는 +*/-)

2+3*4/5 -> 2345/*+
"""

import sys
sys.stdin = open('input.txt')

# 아래에 코드를 작성해주세요.
```



```python
# input2.txt

3
2+3*4/5
(6+5*(2-8)/2)
3-2*5+4/2-2
```

```python
# output.txt

#1 234*5/+
#2 6528-*2/+
#3 325*-42/+2-
```

```python
import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T+1):
    # 아래에 코드를 작성해주세요.
```



```python
# input3.txt

3
234*5/+
6528-2/*+
325*-42/+2-
```

```python
# output.txt

#1 4.4
#2 -9.0
#3 -7.0
```

```python
import sys
sys.stdin = open('input3.txt')

T = int(input())
for tc in range(1, T+1):
    # 아래에 코드를 작성해주세요.
```





## 연습문제 2

```python
#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N

def powerset(idx):
    pass

powerset(0)
```

```python
#2.
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N

def powerset(idx):
    pass

powerset(0)
```



## 연습문제3

- 아래의 입력을 통해 연습하고 추가적으로 `1966_숫자를 정렬하자` 문제도 풀어보세요!

```python
# input.txt

3 9 4 7 5 0 1 6 8 2
```

```python
def quick_sort(nums):
    pass

# 가변 배열
import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums))
```

```python
def partition(arr, start, end):
    pass

def quick_sort(arr, start, end):
    pass

# 고정 배열
import sys
sys.stdin = open('input.txt')
numbers = list(map(int, input().split()))
print(quick_sort(numbers, 0, len(numbers)-1))
```
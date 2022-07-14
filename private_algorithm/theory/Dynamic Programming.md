# Dynamic Programming (DP, 동적 프로그래밍)

DP는 간단히 말해서 복잡한 문제를 간단한 여러개의 문제로 나누어 푸는 방법을 의미한다.



재귀함수에서 동일한 입력의 함수 호출이 반복적으로 일어날 때 그 결과값을 저장해두고 불러 쓰는 것 (Memoization, top down)

최초 입력에서 파생되는 모든 가능한 입력에 대한 답을 모두 저장할 수 있는 메모리가 있어야 한다.

단순히 재귀에서 저장된 값을 찾아보는 것으로도 가능하지만, 결과 값을 순서를 정해서 계산할 수도 있음 (Tabulation, bottom up)



Memoization 예시 피보나치 수열

```python
def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    if memoization[n]:
        return memoization[n]
    memoization[n] = Fibonacci(n-2) + Fibonacci(n-1)
    
    return memoization[n]
# memoization은 기존에 따로 리스트 등으로 빼둔 것 같음
```



 Tabulation 예시 피보나치 수열

```python
def Fibonacci(n):
    F[0] = 0
    F[1] = 1
    
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
       
    return F[n]
```




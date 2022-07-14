# Permutation and Combination



## Permutation(순열)

서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열하는 것



단순한 방법의 순열 구축

ex  = {1, 2, 3}

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j != i:
            for k in range(1, 3):
                if k != i and k != j:
                    print(i, j, k)
```

최소 변경을 통한 방법 : 각각의 순열들은 이전 상태에서 단지 두 개의 요소들만 교환해서 생성



재귀를 통한 순열

```python
def perm(n, k):
    if n == k:
        print(arr)
    else:
        for i in range(k):
            if not used[i]:
                p[n] = arr[i]		# p : 결과 저장 배열 / arr : 순열 만드는데 사용하는 숫자 배열
                used[i] = True
                perm(n+1, k)
                used[i] = False
```



## 부분 집합

집합에 포함된 원소들을 선택하는 것



바이너리 카운팅을 통한 부분집합 생성 코드

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1 << j):
            print('%d'%arr[j], end=' ')
```





## 조합

서로 다른 n개의 원소 중 r개를 순서없이 골라낸 것



재귀 호출을 이용한 조합 알고리즘

```python
def comb(n, r):
    if not r:
        print(arr)
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)
```


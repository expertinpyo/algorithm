import sys
sys.stdin = open('input.txt')

# 기본 풀이 원리 : max idx를 뽑아서 그 인덱스 전까지의 값들을 다 더한다
# 그 이후 max 값과 idx를 갱신해준다
# 현재 코드는 첫번째 max와 그 인덱스만 구현 되었으므로 수정이 필요하다

def becoming_rich(arr):
    ans = 0
    new_arr = sorted(arr)
    i = 0
    while i < (len(arr)):
        max_price = new_arr[-1]
        max_idx = arr.index(max_price)
        if i < max_idx:
            ans += max_price - arr[i]
            new_arr.pop(new_arr.index(arr[i]))
        else:
            new_arr.pop()
        i += 1
    return ans
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"{tc} {becoming_rich(arr)}")

import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    box_size = int(input())                 # 총 크기 입력
    arr = list(map(int, input().split()))   # 각 요소 append
    new_arr = [0]*box_size                  # 새로운 박스 제작
    for j in range(len(arr)):
        new_arr[j] = box_size - (j+1)       # 새 박스에 각 위치별 최대 낙차 입력
        for q in range(j+1, len(arr)):
            if arr[j] > arr[q]:             # 원래 리스트에서 자기보다 작은 값이 있으면 건너뜀
                continue
            else: new_arr[j] -= 1           # 자기보다 크거나 같은 값이 있으면 최대 낙차 -1
    print(new_arr)
    max_num = new_arr[0]
    for n in new_arr:
        if n > max_num:                     # max함수 구현
            max_num = n
    print(f"#{i+1} {max_num}")


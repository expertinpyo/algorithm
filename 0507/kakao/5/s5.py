# 개수를 따져서 하는 것도 하나의 방법이 될 수 있음

def solution(rc, operations):
    arr = rc
    m = len(arr[0])     # 열
    n = len(arr)        # 행
    for oper in operations:
        if oper == "Rotate":
            arr = rotate(arr, n, m)
        else:
            arr = shift(arr, n, m)
    answer = arr
    print(answer)
    return answer

def rotate(arr, n, m):
    box = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                if j == 0:
                    box[i][j] = arr[i+1][j]
                else:
                    box[i][j] = arr[i][j-1]
            elif i == n-1:
                if j != m-1:
                    box[i][j] = arr[i][j+1]
                else:
                    box[i][j] = arr[i-1][j]
            else:
                if j == m-1:
                    box[i][j] = arr[i-1][j]
                elif j == 0:
                    box[i][j] = arr[i+1][j]
                else:
                    box[i][j] = arr[i][j]
    return box

def shift(arr, n, m):
    box = [[]]
    for i in range(n-1):
        box.append(arr[i])
    box[0] = arr[n-1]
    return box

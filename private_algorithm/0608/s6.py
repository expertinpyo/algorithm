# 2636 치즈

# 공기와 접촉 시 한시간 내로 치즈 사라짐
# 면적의 테두리가 없어진다고 생각하면 된다.

# 면적의 테두리인지 알 수 있는 방법
# 각 점마다 판독, 사방이 둘러쌓여있으면 해당 없음
# 각 줄에서 0이나 벽의 번호를 알아내고, 그 것보다 안에 있다면 살려주고 아니면 죽인다.
# 해당 점에서 비교 후 없다면 queue의 형태로 접근하는 것도 좋지 않을까 하는 생각이 있다.



n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

hrs = 0
while True:
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                for k in range(n):
                    
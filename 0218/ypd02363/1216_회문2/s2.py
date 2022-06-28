import sys
sys.stdin = open("a.txt")

arr = [input() for _ in range(100)]
n = arr[0]
case = 1
i = 0
while i < 50:
    for j in range(i, (case+i+1)//2):
        if n[i] == n[case+i]:
            if i == case//2:
                case += 1
        else: break
    i += 1
print(case)
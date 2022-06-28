mm = [0, 0, 1, 1]
n = int(input())

for i in range(4, n+1):
    mm.append(mm[i-1] + 1)
    if not i%2:
        mm[i] = min(mm[i//2]+1, mm[i])
    if not i%3:
        mm[i] = min(mm[i//3]+1, mm[i])
print(mm[n])
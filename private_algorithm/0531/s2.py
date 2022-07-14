sen = input()
arr = [0]*26

for s in sen:
    n = ord(s) - 97
    arr[n] += 1
num = max(arr)
real = chr(arr.index(num)+97)
print(real, num)
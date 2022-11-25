a = input()
b = input()
if a == b:
    print(len(a))
    exit()
ans = 0
start = end = 0
while start < len(a) and len(a[start:end+1]) <= len(b):
    if a[start:end+1] in b:
        ans = max(ans, len(a[start:end+1]))
        if end < len(a) - 1:
            end += 1
        else:
            break
        continue
    start += 1
    end = start if end < start else end
print(ans)
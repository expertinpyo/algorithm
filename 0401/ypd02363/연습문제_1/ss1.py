def make_set(x):
    p[x] = x

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    x, y = find_set(x), find_set(y)
    p[y] = x

#1.
p = [0] * (6+1)

nums = list(range(1,7))
for i in nums:
    make_set(i)
print(p)
print('----------------------------------')

#2.
union(1, 3)
print(p)
print('----------------------------------')

union(2, 3)
print(p)
print('----------------------------------')

union(5, 6)
print(p)
print('----------------------------------')

#3.
print(find_set(6))
print(find_set(3))
print(find_set(2))
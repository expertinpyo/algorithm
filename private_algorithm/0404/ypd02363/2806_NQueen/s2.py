def chess(x, y, st, pl, mi):
    global ans
    if x == n-1:
        ans += 1
        return

    for j in range(n):
        if j not in st and (j - (x+1)) not in pl and (j - (x+1) != y - x) and (j + (x+1)) not in mi and (j + (x+1) != y + x) :
            if y == 0:
                chess(x+1, j, st + [j], pl + [y-x], mi)
            elif y == n-1:
                chess(x+1, j, st + [j], pl, mi + [y+x])
            elif 0 < y < n-1:
                chess(x + 1, j, st + [j], pl + [y-x], mi + [y+x])


n = int(input())
ans = 0
for i in range(n):
    straight = [i]
    minus = []
    plus = []
    chess(0, i, straight, plus, minus)
print(ans)


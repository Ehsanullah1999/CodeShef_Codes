win = 0
ml = 0
p1 = 0
p2 = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    p1 += x
    p2 += y
    mlnew = 0
    if (p1 > p2):
        mlnew = p1 - p2
        if (ml < mlnew):
            ml = p1 - p2
            win = 1
    else:
        mlnew = p2- p1
        if (mlnew > ml):
            ml = p2 - p1
            win = 2
print(win,ml)

# 140 82
# 89 134
# 90 110
# 112 106
# 88 90
from math import fabs
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(int(fabs(x - y)))
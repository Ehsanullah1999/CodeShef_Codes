i = 10
for _ in range(int(input())):
    x, y ,z= map(int, input().split())
    t = i * x
    if (t >= y):
         M = y * z
         print(M)
    else:
        print(t * z)

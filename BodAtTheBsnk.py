for i in range(int (input())):
    w, x, y, z = map(int, input().split())
    r1 = x * z
    r2 = y * z
    result = r1 - r2 + w
    print(result)


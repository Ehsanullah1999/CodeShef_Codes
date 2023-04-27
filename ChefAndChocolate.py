for i in range(int(input())):
    c, x, y = map(int, input().split())
    r1 = c - x
    result = r1 * y
    print(result)
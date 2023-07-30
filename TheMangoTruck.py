for _ in range(int(input())):
    x, y, z = map(int, input().split())
    z = z - y
    print(round(z // x))
for _ in range(int(input())):
    x, y = map(int, input().split())
    if y > x:
        print("YES")
    else:
        print("NO")
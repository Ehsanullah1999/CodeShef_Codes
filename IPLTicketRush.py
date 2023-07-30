for _ in range(int(input())):
    n, m = map(int, input().split())
    if n >= m:
        print(n - m)
    else:
        print(0)
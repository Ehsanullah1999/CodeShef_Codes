for _ in range(int(input())):
    x = int(input())
    if x <= 1000:
        print(100)
    elif x > 1000:
        print(x // 10)
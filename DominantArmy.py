for _ in range(int(input())):
    a, b, c =map(int,input().split())
    if (a > b + c):
        print("yes")
    elif (b > a + c):
        print("yes")
    elif (c > a + b):
        print("yes")
    else:
        print("No!")
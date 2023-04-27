for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if (z >= x):
        if (z >= y + x):
            print(2)
        else:
            print(1)
    else:
        print(0)

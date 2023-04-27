for _ in range(int(input())):
    a, b, c = map(int,input().split())
    if(((a + b) / 2) > c):
        print("yes")
    else:
        print("No")

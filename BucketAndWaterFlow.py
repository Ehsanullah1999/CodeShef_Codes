for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    result = w + (z*y)
    if (x<result):
        print('overFlow')
    elif (x==result):
        print('filled')
    else:
        print('unfilled')
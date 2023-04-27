def countt(x):
    count_x = 0
    for i in x:
        if i == '0' or i == '6' or i == '9':
            count_x += 6
        elif i == '1':
            count_x += 2
        elif i == '2' or i == '3' or i == '5':
            count_x += 5
        elif i == '4':
            count_x += 4
        elif i == '7':
            count_x += 3
        elif i == '8':
            count_x += 7
        else:
            pass
    return count_x;

for i in range(int(input())):
    x,y = map(int, input().split())
    r = x + y
    result = countt(str(r))
    print(result)
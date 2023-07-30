for _ in range(int(input())):
    x = int(input())
    if x % 7 == 0 and x % 2 == 0:
        print("Alice")
    elif x % 9 == 0 and x % 2 == 1:
        print("Bob")
    else:
        print("Charlie")
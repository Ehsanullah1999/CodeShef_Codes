for _ in range(int (input())):
    n=int(input())
    A=[]
    A=list(map(int, input().split()))
    A.sort()
    counter=0
    j=1
    for i in range(n):
       if (A[i]!=A[j]):

           counter+=1
    print(counter)

t=int(input())
while(t):
    n =int(input())
    k=list(map(int,input().split()))
    c=0
    for i in k:
        if k.count(i)>c:
            c=k.count(i)
    print(n-c)
    t-=1
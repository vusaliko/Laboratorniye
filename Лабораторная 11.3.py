while True:
    print("Введите число")
    n=int(input())
    x=0
    k=0
    while x<n:
        x+=k
        k+=1
    k-=1
    print(str(k))

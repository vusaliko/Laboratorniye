while True:
    print("Введите число")
    n=int(input())
    b=0
    for a in range(1,n+1):
        b+=(a*2-1)
        print(str(b))

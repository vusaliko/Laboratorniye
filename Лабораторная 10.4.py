while True:
    print("Введите числа A,N")
    a=float(input())
    n=int(input())
    c=1
    for x in range(1,n+1):
        c+=a**x
    print(str(c))

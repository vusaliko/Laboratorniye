while True:
    print("Введите числа A,N")
    a=float(input())
    n=int(input())
    c=1
    for i in range(1,n+1):
       c+=((-1)**i)*(a**i)
    print(str(c))

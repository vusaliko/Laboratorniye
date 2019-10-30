while True:
    print("Введите N")
    a=1
    b=1
    k=1
    n=int(input())
    while a!=n:
        b,a=b+a,b
        k+=1
    print("Номер числа Финабочи: "+str(k))

while True:
    print("Введите A,B")
    a=int(input())
    b=int(input())
    if a==b:
        print("НОД="+str(a))
    else:
        while a!=b:
            if a>b:
                a-=b
            else:
                b-=a
        print("НОД"+str(a))

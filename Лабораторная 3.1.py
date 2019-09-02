while True:
    print("Введите A,B")
    a=float(input())
    b=float(input())
    c=b
    b=a
    a=c
    print(str(a) + " " + str(b))

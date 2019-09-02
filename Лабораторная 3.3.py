while True:
    print("Введите A,B,C")
    a=float(input())
    b=float(input())
    c=float(input())
    c1=c
    c=b
    b=a
    a=c1
    print(str(a) + " " + str(b) + " " + str(c))

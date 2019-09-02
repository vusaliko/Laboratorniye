while True:
    print("Введите A1,B1,C1,A2,B2,C2")
    a1=float(input())
    b1=float(input())
    c1=float(input())
    a2=float(input())
    b2=float(input())
    c2=float(input())
    y=(a1*c2-a2*c1)/(a1*b2-a2*b1) #Решили систему методом подстановки
    x=(c1-b1*y)/a1
    print("x=" + str(x))
    print("y=" + str(y))

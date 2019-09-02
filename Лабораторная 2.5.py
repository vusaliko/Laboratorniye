import math
while True:
    print("Введите x1,y1,x2,y2,x3,y3")
    x1=float(input())
    y1=float(input())
    x2=float(input())
    y2=float(input())
    x3=float(input())
    y3=float(input())
    a=math.sqrt((x1-x2)**2+(y1-y2)**2) #1 сторона
    b=math.sqrt((x2-x3)**2+(y2-y3)**2) #2 сторона
    c=math.sqrt((x1-x3)**2+(y1-y3)**2) #3 сторона
    P=a+b+c #Периметр
    p=P/2 #Полупериметр
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("P=" + str(P))
    print("S=" + str(S))

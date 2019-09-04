import math
while True:
    print("Введите точки A(x;y),B(x;y),C(x;y)")
    x1=float(input())
    y1=float(input())
    x2=float(input())
    y2=float(input())
    x3=float(input())
    y3=float(input())
    ab=math.sqrt((x1-x2)**2+(y1-y2)**2) #Расстояние AB
    ac=math.sqrt((x1-x3)**2+(y1-y3)**2) #Расстояние AC
    if ab<ac:
        print("B(" + str(x2) + ";" + str(y2) + ") " + str(ab))
    else:
        print("C(" + str(x3) + ";" + str(y3) + ") " + str(ac))
        

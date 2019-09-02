import math
while True:
    print("Введите x точки 1")
    x1=float(input())
    print("Введите y точки 1")
    y1=float(input())
    print("Введите x точки 2")
    x2=float(input())
    print("Введите y точки 2")
    y2=float(input())
    print("Длина=" + str(math.sqrt((x1-x2)**2+(y1-y2)**2)))

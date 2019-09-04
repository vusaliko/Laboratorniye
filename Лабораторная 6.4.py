while True:
    print("Введите A,B,C")
    a=int(input())
    b=int(input())
    c=int(input())
    S=a*b #Площадь прямоугольника
    s=c*c #Площадь квадрата
    print("Разместится " + str(S//s) + " квадратов")

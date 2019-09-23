while True:
    def Quarter(x,y):
        if x>0 and y>0:
            return 1
        if x<0 and y>0:
            return 2
        if x<0 and y<0:
            return 3
        if x>0 and y<0:
            return 4
        if x==0 or y==0:
            return 0
    print("Введите x,y")
    x=float(input())
    y=float(input())
    a=Quarter(x,y)
    if a==0:
        print("Точка лежит на оси координат")
    else:
        print(str(a)+" четверть")

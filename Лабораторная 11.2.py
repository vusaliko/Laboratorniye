while True:
    print("Введите числа A,B")
    a=float(input())
    b=float(input())
    while a>b:
        a-=b
    print("Длина незанятой части "+str(a))

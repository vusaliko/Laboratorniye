while True:
    print("Введите вес конфет X, стоимостью A рублей")
    x=float(input())
    a=float(input())
    print("Введите Y кг конфет")
    y=float(input())
    print("1кг стоит " + str(a/x))
    print(str(y) + "кг стоит " + str(a*y/x))

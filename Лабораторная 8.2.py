while True:
    print("Введите 3 числа")
    a=float(input())
    b=float(input())
    c=float(input())
    if a > b:
        if b>c:
            print(str(a+b))
        else:
            print(str(c+a))
    else:
        if a>c:
            print(str(a+b))
        else:
            print(str(b+c))

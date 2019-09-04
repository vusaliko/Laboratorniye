while True:
    print("Введите числа a,b,c")
    a=int(input())
    b=int(input())
    c=int(input())
    if a+b>c:
        if a+c>b:
            if b+c>a:
                print("Существует")
            else:
                print("Не существует")
        else:
            print("Не существует")
    else:
        print("Не существует")

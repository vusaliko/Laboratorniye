while True:
    print("Введите числа a,b,c")
    a=int(input())
    b=int(input())
    c=int(input())
    if a**2+b**2==c**2:
        print("Истина")
    else:
        if a**2+c**2==b**2:
            print("Истина")
        else:
            if b**2+c**2==a**2:
                print("Истина")
            else:
                print("Ложь")

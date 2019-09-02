while True:
    print("Введите число дней")
    a=float(input())
    a%=7
    b=1+a
    if b==7:
        b=0
    print(str(b))

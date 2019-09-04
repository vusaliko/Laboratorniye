while True:
    print("Введите A,B,C")
    a=int(input())
    b=int(input())
    c=int(input())
    if a < b:
        if b < c:
            print("Истина")
        else:
            print("Ложь")
    else:
        print("Ложь")

while True:
    print("Введите число")
    a=int(input())
    if (a >= 10) and (a<100):
        if (a%2) == 0:
            print("Истина")
        else:
            print("Ложь")
    else:
        print("Ложь")
    

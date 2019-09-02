while True:
    print("Введите A")
    a=float(input())
    b=a
    a*=a # 2 степень
    a*=a # 4 степень
    a*=b # 5 степень
    b=a
    a*=a # 10 степень
    a*=b # 15 степень
    print("A^15=" + str(a))

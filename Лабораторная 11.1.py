while True:
    print("Введите числа A,B")
    a=int(input())
    b=int(input())
    for i in range(a,b+1):
        for c in range(a,i+1):
            print(str(i))

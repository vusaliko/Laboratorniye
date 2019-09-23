while True:
    print("Введите элементы массива A через точку с запятой")
    A=str(input())
    B=A.split(';')
    print("Введите число элементов")
    n=int(input())
    if n%2!=1:
        for i in range(n//2):
            print(B[i])
            print(B[n-i-1])
    else:
        for i in range(n//2):
            print(B[i])
            print(B[n-i-1])
        print(B[n//2])

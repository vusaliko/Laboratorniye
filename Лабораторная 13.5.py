while True:
    print("Введите элементы массива через точку с запятой")
    a=str(input())
    b=a.split(';')
    print("Введите число элементов")
    n=int(input())
    if n%2==1:
        m=n+1
    else:
        m=n
    print("Вывод первый")
    for i in range(m//2):
        print(b[i*2])
    print("Вывод второй")
    m=n
    if n%2==1:
        n-=1
    for i in range(m//2):
        print(b[n-1-i*2])
    

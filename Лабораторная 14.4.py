while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    b=00
    for i in range(0,n):
        a.append(float(input()))
    if a[-1]>a[-2]:
        print("Последний локальный максимум="+str(a[-1]))
    else:
        if a[0]>a[1]:
            b=a[0]
        for i in range(1,n):
            if a[i]>a[i-1] and a[i]>a[i+1]:
                b=a[i]
        if b==00:
            print("Локального максимума нет")
        else:
            print("Локальный максимум ="+str(b))
        

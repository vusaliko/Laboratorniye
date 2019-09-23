while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    for i in range(0,n):
        a.append(float(input()))
    for i in range(1,n):
        if a[i]<a[i-1] or a[i]>a[i+1]:
            a[i],a[i-1]=a[i-1],a[i]
        else:
            break
    print(str(a))

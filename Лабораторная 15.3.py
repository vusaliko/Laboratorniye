while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    for i in range(0,n):
        a.append(int(input()))
    for i in range(0,n):
        if a[i]%2==1:
            x=a[i]
    for i in range(0,n):
        if a[i]%2==1:
            a[i]+=x
    print(str(a))

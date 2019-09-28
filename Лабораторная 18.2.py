while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    n=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,n):
            a[i].append(float(input()))
    print("Введите число К")
    k=int(input())
    s=0
    p=1
    for i in range(0,n):
        s+=a[k-1][i]
        p*=a[k-1][i]
    print("Сумма="+str(s)+" Произведение="+str(p))

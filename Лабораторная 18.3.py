while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    n=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,n):
            a[i].append(float(input()))
    p=1
    s=1
    z=0
    for i in range(0,m):
        p*=a[i][0]
    for i in range(1,n):
        for y in range(0,m):
            s*=a[y][i]
            x=y
        if s<p:
            p=s
            z=x
        s=1
    print("Столбец "+str(z+1))

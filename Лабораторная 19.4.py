while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    n=int(input())
    a=[]
    restart=1
    for i in range(0,m):
        a.append([])
        for y in range(0,n):
            a[i].append(float(input()))
    while restart==1:
        restart=0
        for i in range(0,m-1):
            if a[i][0]>a[i+1][0]:
                for y in range(0,n):
                    a[i][y],a[i+1][y]=a[i+1][y],a[i][y]
        for i in range(0,m-1):
            if a[i][0]>a[i+1][0]:
                restart=1
    for i in range(0,m):
        print(str(a[i]))

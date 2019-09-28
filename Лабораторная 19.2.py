while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    n=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,n):
            a[i].append(float(input()))
    max=a[0][0]
    min=a[0][0]
    smin=0
    smax=0
    for i in range(0,m):
        for y in range(0,n):
            if a[i][y]>max:
                max=a[i][y]
                smax=y
            if a[i][y]<min:
                min=a[i][y]
                smin=y
    for i in range(0,m):
        a[i][smin],a[i][smax]=a[i][smax],a[i][smin]
    for i in range(0,m):
        print(str(a[i]))

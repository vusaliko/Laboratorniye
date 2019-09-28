while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    n=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,n):
            a[i].append(float(input()))
    for i in range(0,m):
        max=a[i][0]
        min=a[i][0]
        mxx=i
        mxy=0
        mnx=i
        mny=0
        for y in range(1,n):
            if a[i][y]>max:
                max=a[i][y]
                mxx=i
                mxy=y
            if a[i][y]<min:
                min=a[i][y]
                mnx=i
                mny=y
        a[mnx][mny],a[mxx][mxy]=a[mxx][mxy],a[mnx][mny]
    for i in range(0,m):
        print(str(a[i]))

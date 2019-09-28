while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,m):
            a[i].append(float(input()))
    for k in range(0,m//2+1):
        for i in range(k,m-k):
            print(str(a[i][k]))
            x=i
        for j in range(k+1,m-k):
            print(str(a[x][j]))
            y=j
        for i in range(m-k-2,k-1,-1):
            print(str(a[i][y]))
            x=i
        for j in range(m-k-2,k,-1):
            print(str(a[x][j]))
            

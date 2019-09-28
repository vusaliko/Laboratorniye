while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    n=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,n):
            a[i].append(float(input()))
    sr=0
    x=0
    for i in range(0,n):
        for y in range(0,m):
            sr+=a[y][i]/m
        for y in range(0,m):
            if a[y][i]>sr:
                x+=1
        print("В столбце "+str(i+1)+" элементов больше среднего арифметического: "+str(x))

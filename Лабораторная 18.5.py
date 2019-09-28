while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    n=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,n):
            a[i].append(float(input()))
    cet=0
    for i in range(0,n):
        for y in range(0,m):
            if a[y][i]%2!=1:
                cet=1
            if cet==1:
                break
            else:
                if y==m-1:
                    x=i+1
        if cet==0:
            break
        cet=0
    if cet==0:
        print("Столбец №"+str(x))
    else:
        print("0")

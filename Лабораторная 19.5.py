while True:
    print("Введите порядок матрицы и ее элементы")
    m=int(input())
    a=[]
    for i in range(0,m):
        a.append([])
        for y in range(0,m):
            a[i].append(float(input()))
    for i in range(0,m):
        del a[i][i]
    d=m*2-2
    p=0
    for k in range(int(d/2),0,-1):
        s=0
        y=0
        for i in range(k-1,m-1):
            s+=a[y][i]
            y+=1
        p+=1
        print("Сумма "+str(p)+" побочной диагонали = "+str(s))
    b=1
    for k in range(0,int(d/2)):
        s=0
        y=b
        for i in range(0,int(d/2)-k):
            s+=a[y][i]
            y+=1
        p+=1
        b+=1
        print("Сумма "+str(p)+" побочной диагонали = "+str(s))
            
            

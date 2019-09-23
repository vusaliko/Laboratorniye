while True:
    print("Введите длину массива и его элементы")
    n=int(input())
    N=[]
    for i in range(0,n):
        N.append(int(input()))
    d=N[1]-N[0]
    a=1
    for i in range(1,n-1):
        if (N[i+1]-N[i])!=d:
            a=0
            break
    if a==1:
        print("Разность арифметической прогрессии ="+str(d))
    else:
        print("0")

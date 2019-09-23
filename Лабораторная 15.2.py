while True:
    print("Введите длину массива и его элементы")
    n=int(input())
    a=[]
    b=[]
    s=0
    for i in range(0,n):
        a.append(float(input()))
    for i in range(0,n):
        for y in range(0,i+1):
            s+=a[y]
        s/=(i+1)
        b.append(s)
        s=0
    print("b="+str(b))

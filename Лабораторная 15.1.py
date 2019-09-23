while True:
    print("Введите длину массивов, а затем их элементы")
    n=int(input())
    a=[]
    b=[]
    for i in range(0,n):
        a.append(float(input()))
    for i in range(0,n):
        b.append(float(input()))
    for i in range(0,n):
        a[i]+=b[i]
        b[i]=a[i]-b[i]
        a[i]=a[i]-b[i]
    print("a="+ str(a))
    print("b="+ str(b))

while True:
    print("Ведите размер массива и его элементы")
    n=int(input())
    a=[]
    for i in range(0,n):
        a.append(float(input()))
    min=min(a)
    max=max(a)
    min=a.index(min)
    max=a.index(max)
    if min<max:
        for i in range(min+1,max):
            a[i]=0
    else:
        for i in range(max+1,min):
            a[i]=0
    print(str(a))
        

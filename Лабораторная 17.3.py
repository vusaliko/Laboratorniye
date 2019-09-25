while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    for i in range(0,n):
        a.append(int(input()))
    print("Введите номер серии K")
    k=int(input())
    m=1
    s=0
    x3=-1
    x4=n-1
    i=0
    while i<n:
        for y in range(i,n):
            if a[i]==a[y]:
                s+=1
            else:
                if m==k:
                    x1=i
                    x2=y
                    s1=s
                break
            if y==n-1:
                x3=i
                s2=s
        if x3!=-1:
            break
        i+=s
        s=0
        m+=1
    b=a[x1]
    del a[x1:x2]
    for i in range(0,s2):
        for y in range(x1,x2):
            a.insert(x1,a[-1])
            break
    a.reverse()
    del a[0:s2]
    for i in range(0, s1):
        a.insert(0,b)
    a.reverse()
    print("a="+str(a))

while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    b=[]
    c=[]
    restart=1
    s=0
    for i in range(0,n):
        a.append(int(input()))
    while restart==1:
        restart=0
        for i in range(0,n):
            for y in range(0,n):
                if a[i]==a[y]:
                    s+=1
                else:
                    break
            b.append(s)
            c.append(a[i])
            n-=s
            for j in range(0,s):
                a.remove(a[i])
            s=0
            if n==0:
                break
            else:
                restart=1
                break
    print("B="+str(b))
    print("C="+str(c))

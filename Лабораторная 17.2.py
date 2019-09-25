while True:
    print("Введите размер массива и его элементыи")
    n=int(input())
    a=[]
    restart=1
    s=0
    for i in range(0,n):
        a.append(int(input()))
    print("Введите число L")
    L=int(input())
    while restart==1:
        restart=0
        for i in range(0,n):
            for y in range(i,n):
                if a[i]==a[y]:
                    s+=1
                else:
                    x=y
                    break
                if y==n-1:
                    x=y
            if s>L:
                a[i]=0
                del a[i+1:x]
                restart=1
                n-=s-1
                s=0
                break
            s=0
    print("a="+str(a))

while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    p=0
    for i in range(0,n):
        a.append(int(input()))
    for i in range(0,n):
        for y in range(0,n):
            if a[i]==a[y]:
                p+=1
            if p==2:
                x=i
                z=y
                break
        if p==2:
            break
        p=0
    print(str(x)+" "+str(z))

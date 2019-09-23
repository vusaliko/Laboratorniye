while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    restart=1
    for i in range(0,n):
        a.append(int(input()))
    while restart==1:
        restart=0
        for i in range(0,n):
            if a[i]==a[i-1]:
                a.remove(a[i])
                n-=1
                restart=1
                break
    print(str(a))
            

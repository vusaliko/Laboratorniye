def Udalenie(a,b):
   return [value for value in a if value != b]
while True:
    print("Введите длину массива и его элементы")
    n=int(input())
    a=[]
    s=0
    restart=1
    for i in range(0,n):
        a.append(int(input()))
    while restart==1:
        restart=0
        for i in range(0,n):
            for y in range(0,n):
                if a[i]==a[y]:
                    s+=1
            if s==2:
                a=Udalenie(a,a[i])
                n-=2
                s=0
                restart=1
                break
            s=0
    print(str(a))
            

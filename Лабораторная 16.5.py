while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    for i in range(0,n):
        a.append(float(input()))
    a.reverse()
    for i in range(0,n):
        if a[i]>0:
            a.insert(i+1,0.0)
            n+=1
    a.reverse()
    if a[0]>0:
        a.insert(0,0.0)
    print(str(a))

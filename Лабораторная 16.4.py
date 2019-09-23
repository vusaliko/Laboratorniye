while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    for i in range(0,n):
        a.append(float(input()))
    for i in range(0,n):
        if a[i]<0:
            a.insert(i+1,0)
            n+=1
    if a[-1]<0:
        a.insert(len(a),0)
    print(str(a))

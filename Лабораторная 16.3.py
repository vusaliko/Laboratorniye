while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[]
    for i in range(0,n):
        a.append(float(input()))
    min=a.index(min(a))
    a.insert(min,0)
    max=a.index(max(a))
    a.insert(max+1,0)
    print(str(a))

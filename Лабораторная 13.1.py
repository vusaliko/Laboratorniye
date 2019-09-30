while True:
    print("Введите N")
    n=int(input())
    N=[]
    a=1
    for i in range(0,n):
        N.append(a)
        a+=2
    print("Массив N:")
    for i in range(len(N)):
        print(N[i])

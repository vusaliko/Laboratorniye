while True:
    print("Введите N,A,D")
    n=int(input())
    a=float(input())
    d=float(input())
    N=[]
    for i in range(n):
        N.append(a)
        a*=d
        print(N[i])

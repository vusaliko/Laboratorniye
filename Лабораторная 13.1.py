while True:
    print("Введите N")
    n=int(input())
    N=[]
    a=1
    if n%2!=1:
        n-=1
    while a!=n:
        N.append(a)
        a+=2
    N.append(a)
    print("Массив N:")
    for i in range(len(N)):
        print(N[i])

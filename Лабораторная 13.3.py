while True:
    print("Введите N,A,B")
    n=int(input())
    a=int(input())
    b=int(input())
    N=[]
    for i in range(n//2):
        N.append(a)
        N.append(b)
        a+=b
        b+=a
    if n%2==1:
        N.append(a)
    for i in range(len(N)):
        print(N[i])
    

while True:
    def Fact2(n):
        N=1
        if(n%2)==0:
            a=2
            while a<=n:
                N*=a
                a+=2
        else:
            a=1
            while a<n:
                a+=2
                N*=a
        return N
    print("Введите N")
    n=int(input())
    print("Двойной факториал="+str(Fact2(n)))

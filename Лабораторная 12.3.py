while True:
    def RingS(r1,r2):
        S=(r1-r2)*3.14
        return S
    print("Введите r1,r2")
    r1=float(input())
    r2=float(input())
    print("S="+str(RingS(r1,r2)))

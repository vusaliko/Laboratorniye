while True:
    def Sign(x):
        if x<0:
            return -1
        if x==0:
            return 0
        if x>0:
            return 1
    print("Введите A,B")
    a=float(input())
    b=float(input())
    print("Sign(A)+Sign(B)="+str(Sign(a)+Sign(b)))

while True:
    print("Введите число")
    n=int(input())
    a=1
    for i in range(11,n+11):
        a*=i/10                
    print(str(a))

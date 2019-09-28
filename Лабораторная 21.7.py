while True:
    print("Введите строку-предложение")
    s=input()
    a=[]
    d=len(s)
    for i in range(0,d//2):
        a.append(s[i*2+1])
    if d%2==1:
        d+=1
    for i in range(d//2-1,-1,-1):
        a.append(s[i*2])
    print(''.join(a))
        

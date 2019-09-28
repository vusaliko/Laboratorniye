while True:
    print("Введите строку")
    s=input()
    a=[]
    b=[]
    for i in range(0,len(s)):
        if s[i]==' ':
            a=[]
            b.append(s[i])
        else:
            if not s[i] in a:
                a.append(s[i])
                b.append(s[i])
            else:
                b.append('.')
    print(''.join(b))
    
    

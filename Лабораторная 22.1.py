while True:
    print("Введите полное имя файла")
    s=str(input())
    s=s.replace('\\','\\'*2)
    with open(s,'r') as f:
        data=f.read()
    exe=0
    a=[]
    for i in range(0,len(data)):
        if data[i]==' ' and exe==0:
            x=i
            exe=1
        a.append(data[i])
    del a[0:x+1]
    with open(s,'w') as f:
        f.write(''.join(a))
    
        

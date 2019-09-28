while True:
    print('Введите пути файлов')
    s1=str(input()).replace('\\','\\'*2)
    s2=str(input()).replace('\\','\\'*2)
    a=[]
    with open(s2,'r') as f:
        data=f.read()
        for i in range(0,len(data)):
            a.append(data[i])
    with open(s1,'r') as f:
        data=f.read()
        for i in range(0,len(data)):
            a.append(data[i])
    with open(s1,'w') as f:
        f.write(''.join(a))

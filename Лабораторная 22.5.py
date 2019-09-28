while True:
    print("Введите полное имя файла")
    s=str(input()).replace('\\','\\'*2)
    with open(s,'r') as f:
        data=f.read()
    p=0
    a=0
    for i in range(0,len(data)):
        if data[i]==' ':
            p+=1
        else:
            p=0
        if p==5:
            p=0
            a+=1
    print("Абзацев: "+str(a))

while True:
    print("Введите полное имя файлы")
    s=str(input())
    exe=0
    exe1=0
    for i in range(len(s)-1,-1,-1):
        if exe==0 and s[i]=='\\':
            y=i
            exe=1
            continue
        if exe1==0 and s[i]=='\\':
            x=i+1
            exe1=1
    if exe1==0:
        print("\\")
    else:
        print(s[x:y])

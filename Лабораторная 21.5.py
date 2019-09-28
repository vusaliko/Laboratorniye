while True:
    print("Введите полное имя файлы")
    s=str(input())
    exe=0
    for i in range(len(s)-1,0,-1):
        if s[i]=='.' and exe==0:
            y=i
            exe=1
        if s[i]=='\\':
            x=i+1
            break
    print(s[x:y])

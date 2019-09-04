s=['С','В','Ю','З']
s0=['Север','Восток','Юг','Запад']
while True:
    print("Введите исходное направление и команду")
    a=s.index(input())
    b=int(input())
    if b==0:
        print(s0[a])
    else:
        if b==1:
            if a==0:
                a=3
            else:
                a-=1
        else:
            if a==3:
                a=0
            else:
                a+=1
        print(s0[a])
            

while True:
    print("Введите % вклада.")
    p=float(input())
    S=1000
    m=0
    while S<=1100:
        S=S*(p+100)/100
        m+=1
    print("Сумма вклада:"+str(S)+" Количество месяцев:"+str(m))

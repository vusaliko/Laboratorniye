b=["Воскресенье","Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
a30=[4,6,9,11]
while True:
    print("Введите год, месяц и день")
    g=int(input()) #Год
    m=int(input())   #Месяц
    d=int(input())   #День
    m1=m
    v=0
    if g%400==0 or (g%4==0 and g+1%100!=0):
        v=1
    if m<3:
        g-=1
        m+=10
    else:
        m-=2
    x=int((d+(31*m)//12+g+g//4-g//100+g//400)%7)
    if (m1==2 and d==29 and v!=1) or (d>31) or (m1 in a30 and d>30):
        print("Ошибка")
    else:
        print(b[x])

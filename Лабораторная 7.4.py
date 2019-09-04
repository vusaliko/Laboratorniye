while True:
    print("Введите трехзначное число")
    b=int(input())
    c=b%10        #Единицы
    a=b//100      #Сотни
    b=(b//10-a*10) #Десятки
    if a<b and b<c:
        print("Истина")
    else:
        if c<b and b<a:
            print("Истина")
        else:
            print("Ложь")
    

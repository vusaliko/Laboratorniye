while True:
    print("Введите строку")
    stroka=str(input())
    k=0
    for i in range(0,len(stroka)):
        if ord(stroka[i])>=65 and ord(stroka[i])<=90:
            k+=1
    print("Количество латинских прописных букв = "+str(k))

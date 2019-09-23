while True:
    print("Введите размер массива и его элементы")
    n=int(input())
    a=[] #Весь массив
    b=[] #Массив из чисел с четным номером
    for i in range(0,n):
        a.append(float(input()))
    for i in range(0,n//2):
        b.append(a[i*2+1])
    print("Минимальный элемент из чисел с четным номером ="+str(min(b)))
    

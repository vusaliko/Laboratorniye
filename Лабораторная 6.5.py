while True:
    print("Введите год")
    a=int(input())
    b=a%100
    c=a//100
    if b >= 1:
        c+=1
    print("Это " + str(c) + " столетие")

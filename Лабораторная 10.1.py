while True:
    print("Введите цену 1 кг")
    n=float(input())
    for i in range(1,11):
        print(str(float(i/10))+"кг="+str(n*i/10))

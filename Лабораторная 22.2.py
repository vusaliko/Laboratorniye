while True:
    print("Введите имя файла и числа N,K")
    name,n,k=str(input()),int(input()),int(input())
    a=[]
    for i in range(0,k):
        a.append('*')
    with open('C:\\Users\\Admin\\Desktop\\Лабораторные\\'+name,'w') as f:
        for i in range(0,n):
            f.write(''.join(a)+'\n')
            

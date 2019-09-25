import math
while True:
    print("Введите N точек, а затем их координаты (x1,y1,x2,y2...xn,yn")
    n=int(input())
    a=[] #Массив всех точек
    b=[] #Массив точек во 2 плоскости
    c=-1
    for i in range(1,n+1):
        a.append([])
        a[i-1].append(float(input()))
        a[i-1].append(float(input()))
    for i in range(0,n):
        if a[i][0]<0 and a[i][1]>0:
            c+=1
            b.append([])
            b[c].append(a[i][0])
            b[c].append(a[i][1])
    if c==-1:
        print("0,0")
    else:
        max=math.sqrt(b[0][0]**2+b[0][1]**2)
        x=0
        y=0
        for i in range(1,len(b)):
            if math.sqrt(b[i][0]**2+b[i][1]**2)>max:
                max=math.sqrt(b[i][0]**2+b[i][1]**2)
                x=b[i][0]
                y=b[i][1]
        print("("+str(x)+","+str(y)+")")

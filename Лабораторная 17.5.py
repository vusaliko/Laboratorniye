import math
while True:
    print("Введите N точек, а затем их координаты (x1,y1,x2,y2...xn,yn")
    n=int(input())
    a=[] #Массив всех точек
    c=-1
    for i in range(1,n+1):
        a.append([])
        a[i-1].append(float(input()))
        a[i-1].append(float(input()))
    p=math.sqrt(a[0][0]**2+a[0][1]**2)+math.sqrt(a[1][0]**2+a[1][1]**2)+math.sqrt(a[2][0]**2+a[2][1]**2)
    x1=a[0][0]
    y1=a[0][1]
    x2=a[1][0]
    y2=a[1][1]
    x3=a[2][0]
    y3=a[2][1]
    for i in range(1,n):
        for y in range(i+1,n):
            for j in range(y+1,n):
               if (math.sqrt(a[i][0]**2+a[i][1]**2)+math.sqrt(a[y][0]**2+a[y][1]**2)+math.sqrt(a[j][0]**2+a[j][1]**2))>p:
                   p=math.sqrt(a[i][0]**2+a[i][1]**2)+math.sqrt(a[y][0]**2+a[y][1]**2)+math.sqrt(a[j][0]**2+a[j][1]**2)
                   x1=a[i][0]
                   y1=a[i][1]
                   x2=a[y][0]
                   y2=a[y][1]
                   x3=a[j][0]
                   y3=a[j][1]
    print("("+str(x1)+";"+str(y1)+") ("+str(x2)+";"+str(y2)+") ("+str(x3)+";"+str(y3)+")")

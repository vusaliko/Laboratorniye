e=['сто','двести','триста','четыреста','пятьсот','шестьсот','семьсот','восемьсот','девятьсот']
#сотни
b3=['одиннадцать','двенадцать','тринадцать','четырнадцать','пятнадцать','шестнадцать','семнадцать','восемнадцать','девятнадцать']
#11-19
b=['','десять','двадцать','тридцать','сорок','пятьдесят','шестьдесят','семьдесят','восемьдесят','девяносто']
#десятки
c=['','один','два','три','четыре','пять','шесть','семь','восемь','девять']
#единицы
while True:
    print("Введите число")
    a=int(input())
    a1=a//100          #Сотни
    c1=a%10            #Единицы
    b1=a//10-a1*10     #Десятки
    b2=b1*10+c1
    if b2>=11 and b2<=19:
        print(e[a1-1]+" "+b3[b2-11])
    else:
        if b1<=0:
            print(e[a1-1]+" "+c[c1])
        else:
            print(e[a1-1]+" "+b[b1]+" "+c[c1])
    

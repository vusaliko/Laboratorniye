day=['первое', 'второе', 'третье', 'четвёртое', 'пятое', 'шестое', 'седьмое', 'восьмое','девятое', 'десятое', 'одиннадцатое', 'двенадцатое','тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое','семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое','двадцать первое', 'двадцать второе', 'двадцать третье', 'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое','тридцатое', 'тридцать первое']
month=['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
while True:
    print("Введите номер дня и месяца")
    d=int(input())-1
    m=int(input())-1
    print(day[d] + " " + month[m])

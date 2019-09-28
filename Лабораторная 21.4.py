while True:
    a=[ord('А'),ord('а'),ord('я'),ord('я'),ord('ё'),ord('Ё'),ord('Е'),ord('е'),ord('У'),ord('у'),ord('Ы'),ord('ы'),ord('О'),ord('о'),ord('И'),ord('и'),ord('Ю'),ord('ю'),ord('Э'),ord('э')]
    print("Введите строку-предложение")
    s=str(input())
    k=0
    for i in range(0,len(s)):
        if ord(s[i]) in a:
            k+=1
    print(str(k))

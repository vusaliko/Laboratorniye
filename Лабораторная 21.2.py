while True:
    print("Введите строку")
    s=input().split()
    min=len(s[0])
    for i in range(0,len(s)):
        if len(s[i])<min:
            min=len(s[i])
    print(str(min))

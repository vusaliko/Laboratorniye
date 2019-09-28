while True:
    print("Введите путь файла")
    s=str(input()).replace('\\','\\'*2)
    with open(s,'r') as f:
        data=' '.join(f.read().split())
    with open(s,'w') as f:
        f.write(data)
        

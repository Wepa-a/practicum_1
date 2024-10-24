from random import randint
fin1 = randint(0, 9)
fin2 = randint(0, 9)
fin3 = randint(0, 9)
fin4 = randint(0, 9)
st0 = str(fin1) + str(fin2) + str(fin3) + str(fin4)
print("Быки и коровы, я загадал.")
print("Введи число из 4-х цифр")
num = 0
while True:
    num += 1    
    print("Номер попытки: ", num)
    st = input(':')
    if st == "test":        
        print(st0)
        continue
    if len(st) != 4:        
        print("Должно быть 4 цифры")
        continue
    ls = list(st)    
    ls0 = list(st0)
    bulls = 0
    for j in range(4):        
         if ls[j] == ls0[j]:
            bulls += 1            
            ls[j] = " "  # Убираем угаданную цифру, чтобы не учитывать ее дважды
            ls0[j] = "*"  # Заменяем угаданную цифру, чтобы не учитывать ее дважды
    if bulls == 4:        
        print("Вы угадали!")
        break
    cows = 0
    for j in range(4):        
        n = ls[j]
        for k in range(4):            
            if n == ls0[k]:
                cows += 1                
                ls0[k] = "*"  # Заменяем найденную цифру, чтобы не учитывать ее дважды
                break
    print("Быков: ", bulls)    
    print("Коров: ", cows)
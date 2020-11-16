a = int(input("Введите начальное количество километров: ")) 
b = int(input("Введите окончательное количество километров: ")) 
counter = 1 
while a < b: 
    a = a + a * 0.1 
    counter+=1  
print('Ответ: ', counter)

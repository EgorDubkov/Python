with open('file_5.txt', 'w+') as file:
    lines = input('Введите числа: ')
    file.writelines(lines)
    numbers = lines.split()
    print(sum(map(int, numbers)))

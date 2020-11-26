out_f = open("new_file.txt", "w")
line = input('Введите текст: ')
while line:
    out_f.writelines(line)
    line = input('Введите текст: ')
    if not line:
        break


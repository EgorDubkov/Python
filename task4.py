new_file = open('text_4.txt', 'r')
lines = new_file.readlines()
translate = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_list = []
for i in lines:
    i = i.split(' ', 1)
    new_list.append(translate[i[0]] + ' ' + i[1])
print(new_list)

with open('text_4.txt', 'w') as file:
    file.writelines(new_list)

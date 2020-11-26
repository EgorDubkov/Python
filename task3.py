new_file = open('text_3.txt', 'r', encoding = 'utf-8')
salary = []
low_salary = []
counter = 0
new_list = new_file.read().split('\n')
for i in new_list:
    i = i.split()
    if float(i[1]) < 20000:
        counter += 1
        low_salary.append(i[0])
    salary.append(i[1])
        

print('Количество работников с окладом менее 20000: ', counter, low_salary, 'Средний оклад: ', sum(map(float, salary))/10)
    

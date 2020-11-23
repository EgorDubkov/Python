from itertools import count
from itertools import cycle

def count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def cycle_func(my_list, iteration):
    i = 0
    while i < iteration:
        print(next(cycle(my_list)))
        i+=1
count_func(start_number = int(input("Начальное значение: ")), stop_number = int(input("Конечное значение: ")))
cycle_func(my_list = [1, 2, 123, 10, 76, 5], iteration = int(input("Количество элементов: ")))

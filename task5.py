a = int(input('Введите занчение выручки фирмы: '))
b = int(input('Введите занчение издержек фирмы: '))
if a > b:
    print("Прибыль")
    print("Прибыль к выручке: ", (a-b)/a)
elif b > a:
    print("Убыток")
else:
    print("В ноль")
c = int(input(("Введите численность сотрудников фирмы: ")))
print("Прибыль фирмы в расчете на одного сотрудника: ", (a-b)/c)

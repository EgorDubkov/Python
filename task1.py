import sys
name, time, salary, bonus = sys.argv
time = int(time)
salary = int(salary)
bonus = int(bonus)
res = time * salary + bonus
print(f'заработная плата сотрудника:  {res}')


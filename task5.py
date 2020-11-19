def new_sum():
    summ = 0
    numbers = input().split()
    for i in range(len(numbers)):
        if numbers[i] == '$':
            break
        else:
            summ = summ + int(numbers[i])
    print(summ)
new_sum()

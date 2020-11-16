new_list = []
i = 0
el = 0
element_count = int(input())
while i < element_count:
    new_list.append(input())
    i += 1
for el in range(int(len(new_list)/2)):
        new_list[el], new_list[el + 1] = new_list [el + 1], new_list[el]
        el += 2
print(new_list) 

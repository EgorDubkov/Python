string = input()
words = []
counter = 1
for i in range(string.count(' ') + 1):
    words = string.split()
    if len(str(words)) <= 10:
        print(counter, " ", words[i])
        counter += 1
    else:
        print(counter, " ", words[i][0:10])
        counter +=1

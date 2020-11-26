subject = {}
with open('text_6.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        subj, practice, lecture, lab = line.split()
        subject[subj] = int(practice) + int(lecture) + int(lab)
    print(f'{subject}')

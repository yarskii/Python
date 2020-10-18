subj = {}
with open('text_task6.txt') as obj:
    for _ in obj:
        subject, lecture, practice, lab = _.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - {subj}')

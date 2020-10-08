phrase = input('Введите несколько слов через пробел').split()
el = 0
b = []
while el < len(phrase):
    if len(phrase[el]) < 11:
        b.append(phrase[el])
        el += 1
        continue
    elif len(phrase[el]) > 10:
        d = phrase[el]
        b.append(d[0:10])
    el += 1
n = ' '.join(b)
for i, j in enumerate(n.split(), 1):
    print(i, j)

a = [1, 1.32, None, True, 'True', [1, 5], {}, ()]
i = 0
while i <= len(a):
    if len(a) == 1:
        break
    if i >= len(a) - 1:
        break
    c = a[i]
    a[i] = a[i + 1]
    a[i + 1] = c
    i += 2
print(a)

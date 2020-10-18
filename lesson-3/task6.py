def int_func(phrase):
    d = phrase.split()
    if len(d) == 1:
        return phrase.title()
    else:
        return phrase.upper()

print(int_func('text'))
print(int_func('text text'))

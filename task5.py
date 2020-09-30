inc = float(input('Введите значение выручки (сумма в рублях)'))
cost = float(input('Введите значение издержек (сумма в рублях)'))
eff = round((inc / cost), 2)
if inc < cost:
    print('Кампания работает в убыток')
elif inc >= cost:
    if inc == cost:
        print('Вы работаете в 0')
    else:
        print('Кампания приносит прибыль!')
        print(f'Рентабельность выручки: {eff}%')
        num = int(input('Введите колличество сотрудников'))
        print(f'Прибыль на одного сотрудника составляет: {round((inc / num), 2)} руб.')

from sys import argv

file_name, work_hours, rate, prize = argv

salary = (int(work_hours) * int(rate)) + int(prize)

print(f'Выработка в часах: {work_hours}')
print(f'Ставка в час: {rate} р.')
print(f'Премия: {prize} р.')
print(f'Заработная плата составляет: {salary} р.')

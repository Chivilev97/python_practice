import random

attempt = 1
life = 5
i = random.randint(1, 100)
suggested = int(input(f'Отгадай число от 1 до 100, у вас {life} попыток: '))

while suggested != i or life != 0:
    if life == 0:
        print(f'Ваши попытки закончились, это число: {i}')
        break
    elif suggested < i:
        print('Выбери больше')
        attempt += 1
        life -= 1
        suggested = int(input(f'Отгадай число от 1 до 100, у вас {life} попыток: '))
    elif suggested > i:
        print('Выбери меньше')
        attempt += 1
        life -= 1
        suggested = int(input(f'Отгадай число от 1 до 100, у вас {life} попыток: '))
    else:
        print(f'Вам удалось отгадать, это число: {i}. Попыток понадобилось: {attempt}.')
        break

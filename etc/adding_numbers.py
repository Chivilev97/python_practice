count = 0
result = []
max_count = int(input('Сколько чисел вы хотите сложить?: '))

while count < max_count:
    number = int(input('Введите число: '))
    count += 1
    result.append(number)
print(f'Сумма чисел равна {sum(result)}')



















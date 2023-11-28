try:
    people, pizzas = int(input('Сколько вас человек?: ')), int(input('Сколько у вас пицц?: '))
except BaseException:
    print('Вы ввели не число')
    exit(1)
    
pieces = pizzas * 8
pieces_each = pieces // people
remains = pieces % people
print(f'Каждому человеку достанется {pieces_each} кусков, и останется {remains} лишних кусков.')


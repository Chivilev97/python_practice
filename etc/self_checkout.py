try:

    price_1, quantity_1 = float(input('Цена товара 1: ')), int(input('Количество товара 1: '))
    price_2, quantity_2 = float(input('Цена товара 2: ')), int(input('Количество товара 2: '))
    price_3, quantity_3 = float(input('Цена товара 3: ')), int(input('Количество товара 3: '))

except BaseException:
    print('Вы ввели не верно')
    exit(1)

price_1 = price_1 * quantity_1
price_2 = price_2 * quantity_2
price_3 = price_3 * quantity_3

subtotal = float(price_3 + price_2 + price_1)
tax = float(0.055 * subtotal)
total = float(subtotal + tax)

print(f'Промежуточный итог: {subtotal}$\n'
      f'Налог: {tax}$\n'
      f'Итог: {total}$')



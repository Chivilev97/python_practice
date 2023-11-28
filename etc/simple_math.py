try:
    num1, num2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
except BaseException:
    print('Вы ввели не число')
    exit(1)

summ = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
output = '''
{num1} + {num2} = {summ}
{num1} - {num2} = {difference}
{num1} * {num2} = {product}
{num1} / {num2} = {division}
'''

print(output.format(num1= num1,num2= num2,summ= summ,difference= difference,product= product,division= division))



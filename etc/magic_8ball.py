import random

input('Ваш вопрос?: ')

i = random.randint(0, 3)
answers = ['Да', 'Нет', 'Может быть', 'Спросите позже']

print(answers[i])

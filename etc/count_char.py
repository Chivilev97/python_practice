
while True:
    word = input('Введите слово: ')
    lenght = len(word)
    if lenght == 0:
        print('Вы не ввели слово')
    else:
        break
print(f'В слове {word}, {lenght} символов')
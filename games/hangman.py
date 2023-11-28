import random

HANGMAN = (
    '''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ==='''
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ('НОУТБУК', 'КОРОВА', 'КОРАБЛЬ', 'АЙФОН')
word = random.choice(WORDS)
so_far = '-' * len(word)
wrong = 0
used = []

print('Добро пожаловать в игру "Виселица"')

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print('\nВы уже предлагали следующие буквы:\n', used)
    print('\nОтгаданное вами слово сейчас выглядит так:\n', so_far)
    guess = input('\n\nВведите букву: ')
    guess = guess.upper()

    while guess in used:
        print('Вы уже предлагали букву:', guess)
        guess = input('\n\nВведите букву: ')
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print('Да! Буква', guess, 'есть в слове!')
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('\nК сожелению, буквы', guess, 'нет в слове')
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print('\nВас повесили!')
else:
    print('\n Вы отгадали!')

print('\nБыло загадано слово: ', word)
input('\n\nНажмите Enter, чтобы выйти')
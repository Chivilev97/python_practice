# Глобальные константы
X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'Ничья'
NUM_SQUARES = 9


def display_instruct():
    '''Выводит на экран инструкцию'''
    print(
        '''
    Добро пожаловать в игру "крестики-нолики".
    Чтобы сделать ход, введи число от 0 до 8.\n
        '''
    )


def ask_yes_no(question):
    '''Задает вопрос с ответом "yes" или "no".'''
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    '''Просит введите число из диапазона'''
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def init_players():
    '''Определяет первый ход'''
    go_first = ask_yes_no('Хочешь оставить за собой первый ход? (y/n): ')
    if go_first == 'y':
        print('Даю тебе фору: играй крестиками.')
        return O, X
    else:
        print('Буду начинать я.')
        return X, O


def new_board():
    '''Создает новую игровую доску'''
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    '''Отображает игровую доску на экране'''
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '---------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '---------')
    print('\t', board[6], '|', board[7], '|', board[8], '\n')


def legal_moves(board):
    '''Создает список доступных ходов'''
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    '''Определяет победителя в игре'''
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    '''Получает ход человека'''
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('Твой ход. Выбери одно из полей (0-8): ', 0, NUM_SQUARES)
        if move not in legal:
            print('Это поле уже занято')
    print('Ладно')
    return move


def computer_move(board, computer, human):
    '''Делает ход за компьютерного противника'''
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('Я выберу поле номер', end=' ')
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    '''Осуществлет переход хода'''
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    '''Поздравляем победителя игры'''

    if the_winner == computer:
        print('Компьютер выиграл')
    elif the_winner == human:
        print('Ты выиграл')
    else:
        print('Ничья')


def main():
    display_instruct()
    computer, human = init_players()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()

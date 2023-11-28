import math


def standard_deviation(numbers):
    if len(numbers) == 0:
        raise ValueError

    average = sum(numbers) / len(numbers)
    squares_of_diffs = []
    for i in numbers:
        squares_of_diffs.append((i - average) ** 2)
    return math.sqrt(sum(squares_of_diffs) / len(squares_of_diffs))


if __name__ == '__main__':

    stop_word = 'done'
    numbers = []

    while True:
        number = input('Введите число: ')
        if number == stop_word:
            break
        else:
            numbers.append(number)

    print(f"Числа: {', '.join(numbers)}")

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    average = sum(numbers) / len(numbers)

    print(f'Среднее число: {average}')
    print(f'Минимальное число: {min(numbers)}')
    print(f'Максимальное число: {max(numbers)}')
    print(f'Среднеквадратическое отклонение: {standard_deviation(numbers)}')
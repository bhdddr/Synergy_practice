import random


def is_it_correct_number(n):
    try:
        n = int(n)
    except ValueError:
        return False

    if 1 <= n <= 100:
        return n
    else:
        return False


def main():
    print('Игра «Угадай число». Нужно угадать число от 1 до 100.')

    while True:
        try:
            number_of_tries = int(input('Введите число попыток: '))
        except ValueError:
            print('Введите целое число!')
            continue

        if number_of_tries > 0:
            break
        else:
            print('Число попыток должно быть больше 0.')

    random_number = random.randint(1, 100)

    while number_of_tries > 0:
        number_to_get = input('Введите число от 1 до 100: ')
        number_to_get = is_it_correct_number(number_to_get)

        if number_to_get == False:
            print('Ошибка: нужно целое число от 1 до 100.')
            continue

        if number_to_get == random_number:
            print('Вы угадали число, поздравляю!')
            break
        elif number_to_get > random_number:
            print('Ваше число больше загаданного.')
        else:
            print('Ваше число меньше загаданного.')

        number_of_tries -= 1
        print(f'Осталось попыток: {number_of_tries}')
    else:
        print('Попытки закончились. Игра завершена.')
        print(f'Было загадано число {random_number}')


if __name__ == '__main__':
    main()

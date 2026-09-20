import math

def factorial_of_number(n):
    return math.factorial(n)

def main():
    try:
        number = int(input('Введите число, пожалуйста: '))
    except ValueError:
        print('Введите целое число!')
    else:
        if number <= 0:
            print('Число должно быть больше 0')
        else:
            result = factorial_of_number(number)
            print(f'Факториалом числа {number} является {result}')




if __name__ == '__main__':
    main()



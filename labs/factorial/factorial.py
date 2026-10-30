"""Вычисление факториала целого неотрицательного числа."""


def factorial(n):
    """Вернуть n!; отрицательный аргумент отклонить."""
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    """Прочитать число и вывести результат либо ошибку ввода."""
    try:
        number = int(input("Введите целое неотрицательное число: "))
        print("Факториал:", factorial(number))
    except ValueError:
        print("Ошибка: введите целое неотрицательное число")
    except EOFError:
        print("Ошибка: ввод отсутствует")


if __name__ == "__main__":
    main()

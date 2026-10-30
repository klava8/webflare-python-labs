from addition import add
from multiplication import multiply


def main():
    try:
        first = float(input("Первое число: "))
        second = float(input("Второе число: "))
        print("Сумма:", add(first, second))
        print("Произведение:", multiply(first, second))
    except ValueError:
        print("Ошибка: введите числа")
    except EOFError:
        print("Ошибка: ввод отсутствует")


if __name__ == "__main__":
    main()

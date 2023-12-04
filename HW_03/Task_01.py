def even_odd_number(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть числом")
    return n % 2 == 0


if __name__ == '__main__':
    print(even_odd_number(9))
    print(even_odd_number(26))
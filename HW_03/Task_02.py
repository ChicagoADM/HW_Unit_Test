def number_in_interval(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть числом")
    return 25 <= n <= 100


if __name__ == '__main__':
    print(number_in_interval(25))
    print(number_in_interval(0))
def average(*args, **kwargs) -> int:
    """
    :param args: any values
    :param kwargs: key-value(will not be used)
    :return: sum of all int or float params, except key-value params
    """
    _ = kwargs
    s = 0
    for i in args:
        if type(i) is int or type(i) is float:
            s = s + i
        else:
            continue

    return s


def n_average(n: int, even=False, odd=False) -> int:
    """
    :param n: limit of numbers to add
    :param even: if is true, take just even numbers
    :param odd: if is true, take just odd numbers
    :return: sum of first n integers numbers, if both variables(even, odd) are True will calculate sum of all numbers
    """
    if even and odd:
        even = False
        odd = False
    if n <= 0:
        return 0
    if even:
        if n % 2 != 0:
            n -= 1
        return n + n_average(n - 2, even=True)
    if odd:
        if n % 2 == 0:
            n -= 1
        return n + n_average(n - 2, odd=True)
    return n + n_average(n - 1)


def read_integers() -> int:
    """
    :return: if input is int->return input, else-> return 0
    """
    a = input("Insert something:")
    try:
        return int(a)
    except ValueError:
        return 0


if __name__ == '__main__':
    print(average("aa", 34, 2, 1, 5, -2, [21, 434, "afa"]))
    print(average())
    print(average(2, 4, 'abc', param_1=2))
    print(n_average(5))
    print(n_average(10, even=True))
    print(n_average(10, odd=True))
    while True:
        print(read_integers())

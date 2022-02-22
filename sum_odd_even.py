def calculate(input_number: int):
    digits_list = [int(digit) for digit in str(input_number)]
    sum_odd_digits = sum(dig for dig in digits_list if dig & 1)
    sum_even_digits = sum(dig for dig in digits_list if not dig & 1)
    return sum_odd_digits, sum_even_digits


if __name__ == '__main__':
    assert calculate(1) == (1, 0)
    print(calculate(1))
    assert calculate(45670) == (12, 10)
    print(calculate(45670))
    assert calculate(7863121) == (12, 16)
    print(calculate(7863121))
    assert calculate(77620) == (14, 8)
    print(calculate(77620))
    assert calculate(1357) == (16, 0)
    print(calculate(1357))
    assert calculate(240664826606) == (0, 50)
    print(calculate(240664826606))
"""
    Написать функцию camel_case, которая возвращает копию исходной строки
    с чередованием прописных и строчных букв
"""


def camel_case(src: str) -> str:
    return ''.join(value if num % 2 else value.upper() for num, value in enumerate(src, 1))


assert camel_case('asdfghjkl') == 'aSdFgHjKl'
print(camel_case('asdfghjkl'))
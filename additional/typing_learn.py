from typing import Union, Optional


def division(a: int, b: Optional[int]) -> Optional[float]:
    if b is None:
        return a

    if b != 0:
        return a / b
    return

def test_unpack():
    pass


def test_func():
    return 'test'


def test_print(a: str) -> str:
    print(a)


test_func()

test_print('little')

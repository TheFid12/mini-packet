from __future__ import annotations
from functools import lru_cache
from .utils import check_non_negative_int

__all__ = ["factorial", "factorial_r", "fib", "fib_r"]

@check_non_negative_int
def factorial(n: int) -> int:
    """
    Иттеративно вычисляет n!.
    """
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

@check_non_negative_int
def factorial_r(n: int) -> int:
    """
    Рекурсивная версия факториала.
    """
    if n < 2:
        return 1
    return n * factorial_r(n - 1)

@check_non_negative_int
def fib(n: int) -> int:
    """
    Итеративно вычисляет n-е число Фибоначчи.
    """
    if n < 2:
        return n
    st = 0
    res = 1
    for i in range(2, n + 1):
        st, res = res, st + res
    return res

@lru_cache(maxsize=None)
@check_non_negative_int
def fib_r(n: int) -> int:
    """
    Рекурсивно вычисляет n-ое число Фибоначчи.
    """
    if n < 2:
        return n
    return fib_r(n - 1) + fib_r(n - 2)

import pytest
from src.algorithms import factorial, factorial_r, fib, fib_r


class TestFactorial:
    """Тесты для функций факториала."""

    def test_factorial_zero(self):
        """Тест факториала нуля."""
        assert factorial(0) == 1

    def test_factorial_one(self):
        """Тест факториала единицы."""
        assert factorial(1) == 1

    def test_factorial_positive(self):
        """Тесты факториала положительных чисел."""
        assert factorial(5) == 120
        assert factorial(10) == 3628800
        assert factorial(3) == 6

    def test_factorial_negative_raises(self):
        """Тест что отрицательное число вызывает ошибку."""
        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_non_int_raises(self):
        """Тест что не-int вызывает ошибку."""
        with pytest.raises(ValueError):
            factorial(5.5)


class TestFactorialRecursive:
    """Тесты для рекурсивного факториала."""

    def test_factorial_recursive_zero(self):
        """Тест рекурсивного факториала нуля."""
        assert factorial_r(0) == 1

    def test_factorial_recursive_one(self):
        """Тест рекурсивного факториала единицы."""
        assert factorial_r(1) == 1

    def test_factorial_recursive_positive(self):
        """Тесты рекурсивного факториала положительных чисел."""
        assert factorial_r(5) == 120
        assert factorial_r(10) == 3628800
        assert factorial_r(3) == 6

    def test_factorial_recursive_match_iterative(self):
        """Тест что рекурсивная и итеративная версии дают одинаковый результат."""
        for n in range(15):
            assert factorial(n) == factorial_r(n)

    def test_factorial_recursive_negative_raises(self):
        """Тест что отрицательное число вызывает ошибку."""
        with pytest.raises(ValueError):
            factorial_r(-1)


class TestFibonacci:
    """Тесты для функций Фибоначчи."""

    def test_fib_zero(self):
        """Тест числа Фибоначчи для n=0."""
        assert fib(0) == 0

    def test_fib_one(self):
        """Тест числа Фибоначчи для n=1."""
        assert fib(1) == 1

    def test_fib_sequence(self):
        """Тест последовательности чисел Фибоначчи."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for n, exp in enumerate(expected):
            assert fib(n) == exp

    def test_fib_large_number(self):
        """Тест большого числа Фибоначчи."""
        assert fib(20) == 6765
        assert fib(30) == 832040

    def test_fib_negative_raises(self):
        """Тест что отрицательное число вызывает ошибку."""
        with pytest.raises(ValueError):
            fib(-1)


class TestFibonacciRecursive:
    """Тесты для рекурсивной функции Фибоначчи."""

    def test_fibo_recursive_zero(self):
        """Тест рекурсивного числа Фибоначчи для n=0."""
        assert fib_r(0) == 0

    def test_fibo_recursive_one(self):
        """Тест рекурсивного числа Фибоначчи для n=1."""
        assert fib_r(1) == 1

    def test_fibo_recursive_sequence(self):
        """Тест последовательности чисел Фибоначчи рекурсивно."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for n, exp in enumerate(expected):
            assert fib_r(n) == exp

    def test_fibo_recursive_match_iterative(self):
        """Тест что рекурсивная и итеративная версии дают одинаковый результат."""
        for n in range(25):
            assert fib(n) == fib_r(n)

    def test_fibo_recursive_negative_raises(self):
        """Тест что отрицательное число вызывает ошибку."""
        with pytest.raises(ValueError):
            fib_r(-1)

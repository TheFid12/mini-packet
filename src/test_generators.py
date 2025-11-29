from typing import List
import random

__all__ = [
    "rand_int_array",
    "nearly_sorted",
    "many_duplicates",
    "reverse_sorted",
    "rand_float_array",
]


def rand_int_array(
    n: int, 
    lo: int, 
    hi: int, 
    *, 
    distinct: bool = False, 
    seed: int | None = None
) -> List[int]:
    """
    Генерирует случайный массив целых чисел.
    
    Args:
        n: Размер массива
        lo: Минимальное значение (включительно)
        hi: Максимальное значение (включительно)
        distinct: Если True, все элементы уникальны
        seed: Seed для генератора случайных чисел
    
    Returns:
        Список случайных целых чисел
    """
    if seed is not None:
        random.seed(seed)
    
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("Недостаточно уникальных значений в диапазоне")
        return random.sample(range(lo, hi + 1), n)
    
    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(
    n: int, 
    swaps: int, 
    *, 
    seed: int | None = None
) -> List[int]:
    """
    Генерирует почти отсортированный массив.
    
    Args:
        n: Размер массива
        swaps: Количество случайных обменов
        seed: Seed для генератора случайных чисел
    
    Returns:
        Почти отсортированный список
    """
    if seed is not None:
        random.seed(seed)
    
    arr = list(range(n))
    
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr


def many_duplicates(
    n: int, 
    k_unique: int = 5, 
    *, 
    seed: int | None = None
) -> List[int]:
    """
    Генерирует массив с большим количеством дубликатов.
    
    Args:
        n: Размер массива
        k_unique: Количество уникальных значений
        seed: Seed для генератора случайных чисел
    
    Returns:
        Список с дубликатами
    """
    if seed is not None:
        random.seed(seed)
    
    unique_values = list(range(k_unique))
    return [random.choice(unique_values) for _ in range(n)]


def reverse_sorted(n: int) -> List[int]:
    """
    Генерирует массив в обратном порядке.
    
    Args:
        n: Размер массива
    
    Returns:
        Список от n-1 до 0
    """
    return list(range(n - 1, -1, -1))


def rand_float_array(
    n: int, 
    lo: float = 0.0, 
    hi: float = 1.0, 
    *, 
    seed: int | None = None
) -> List[float]:
    """
    Генерирует случайный массив float чисел.
    
    Args:
        n: Размер массива
        lo: Минимальное значение
        hi: Максимальное значение
        seed: Seed для генератора случайных чисел
    
    Returns:
        Список случайных float чисел
    """
    if seed is not None:
        random.seed(seed)
    
    return [random.uniform(lo, hi) for _ in range(n)]

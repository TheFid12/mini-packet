import pytest
from src.sorting import bubble_sort, quick_sort, counting_sort, radix_sort, heap_sort
from src.test_generators import (
    rand_int_array,
    nearly_sorted,
    many_duplicates,
    reverse_sorted,
)


class TestGeneratedCases:
    """Тесты с использованием генераторов."""

    @pytest.mark.parametrize("size", [10, 50, 100])
    @pytest.mark.parametrize("seed", [1, 42, 123])
    def test_random_arrays(self, size, seed):
        """Тест на случайных массивах разного размера."""
        data = rand_int_array(size, 0, 1000, seed=seed)
        expected = sorted(data)
        
        assert bubble_sort(data.copy()) == expected
        assert quick_sort(data.copy()) == expected
        assert heap_sort(data.copy()) == expected

    @pytest.mark.parametrize("n,swaps", [(20, 2), (50, 5), (100, 10)])
    def test_nearly_sorted(self, n, swaps):
        """Тест на почти отсортированных массивах."""
        data = nearly_sorted(n, swaps, seed=42)
        expected = sorted(data)
        
        assert bubble_sort(data.copy()) == expected
        assert quick_sort(data.copy()) == expected

    @pytest.mark.parametrize("size,unique", [(50, 5), (100, 10), (200, 20)])
    def test_many_duplicates(self, size, unique):
        """Тест на массивах с дубликатами."""
        data = many_duplicates(size, k_unique=unique, seed=999)
        expected = sorted(data)
        
        assert quick_sort(data.copy()) == expected
        assert heap_sort(data.copy()) == expected

    @pytest.mark.parametrize("size", [10, 50, 100, 500])
    def test_reverse_sorted(self, size):
        """Тест на обратно отсортированных массивах."""
        data = reverse_sorted(size)
        expected = list(range(size))
        
        assert bubble_sort(data.copy()) == expected
        assert quick_sort(data.copy()) == expected
        assert heap_sort(data.copy()) == expected

    def test_distinct_values(self):
        """Тест на массиве с уникальными значениями."""
        data = rand_int_array(30, 1, 100, distinct=True, seed=777)
        expected = sorted(data)
        
        assert quick_sort(data.copy()) == expected
        assert heap_sort(data.copy()) == expected

    @pytest.mark.parametrize("algo", [bubble_sort, quick_sort, heap_sort])
    def test_empty_and_single(self, algo):
        """Тест граничных случаев для всех алгоритмов."""
        assert algo([]) == []
        assert algo([42]) == [42]

    def test_large_random_array(self):
        """Тест на большом случайном массиве."""
        data = rand_int_array(1000, -500, 500, seed=12345)
        expected = sorted(data)
        
        assert quick_sort(data.copy()) == expected
        assert heap_sort(data.copy()) == expected

import pytest
from src.sorting import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
)


class TestBubbleSort:
    """Тесты для bubble sort."""

    def test_empty_list(self):
        """Тест сортировки пустого списка."""
        assert bubble_sort([]) == []

    def test_single_element(self):
        """Тест сортировки одного элемента."""
        assert bubble_sort([5]) == [5]

    def test_sorted_list(self):
        """Тест уже отсортированного списка."""
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Тест обратно отсортированного списка."""
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        """Тест списка с дубликатами."""
        assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_negative_numbers(self):
        """Тест с отрицательными числами."""
        assert bubble_sort([-5, -1, -10, 0, 5]) == [-10, -5, -1, 0, 5]


class TestQuickSort:
    """Тесты для quick sort."""

    def test_empty_list(self):
        assert quick_sort([]) == []

    def test_single_element(self):
        assert quick_sort([5]) == [5]

    def test_sorted_list(self):
        assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_large_list(self):
        """Тест с большим списком."""
        import random
        data = list(range(100, 0, -1))
        assert quick_sort(data) == list(range(1, 101))


class TestCountingSort:
    """Тесты для counting sort."""

    def test_single_element(self):
        assert counting_sort([5]) == [5]

    def test_sorted_list(self):
        assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]


class TestRadixSort:
    """Тесты для radix sort."""

    def test_single_element(self):
        assert radix_sort([5]) == [5]

    def test_sorted_list(self):
        assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]


class TestBucketSort:
    """Тесты для bucket sort."""

    def test_empty_list(self):
        assert bucket_sort([]) == []

    def test_single_element(self):
        assert bucket_sort([0.5]) == [0.5]

    def test_sorted_list(self):
        result = bucket_sort([0.1, 0.2, 0.3, 0.4, 0.5])
        assert result == [0.1, 0.2, 0.3, 0.4, 0.5]

    def test_unsorted_list(self):
        result = bucket_sort([0.897, 0.565, 0.656, 0.123, 0.665, 0.343])
        expected = [0.123, 0.343, 0.565, 0.656, 0.665, 0.897]
        assert result == expected


class TestHeapSort:
    """Тесты для heap sort."""

    def test_empty_list(self):
        assert heap_sort([]) == []

    def test_single_element(self):
        assert heap_sort([5]) == [5]

    def test_sorted_list(self):
        assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_negative_numbers(self):
        assert heap_sort([-5, -1, -10, 0, 5]) == [-10, -5, -1, 0, 5]


class TestSortConsistency:
    """Тесты консистентности между разными алгоритмами сортировки."""

    def test_all_sorts_agree(self):
        """Все алгоритмы сортировки должны давать одинаковый результат."""
        test_data = [3, 7, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 9]

        assert bubble_sort(test_data.copy()) == expected
        assert quick_sort(test_data.copy()) == expected
        assert counting_sort(test_data.copy()) == expected
        assert radix_sort(test_data.copy()) == expected
        assert heap_sort(test_data.copy()) == expected

from typing import Dict, Callable, Any
from .sorting import (
    bubble_sort, quick_sort, counting_sort,
    radix_sort, bucket_sort, heap_sort
)

__all__ = ["SORT_METHODS"]

SORT_METHODS: Dict[str, Callable[..., Any]] = {
    "bubble": bubble_sort,
    "quick": quick_sort,
    "counting": counting_sort,
    "radix": radix_sort,
    "bucket": bucket_sort,
    "heap": heap_sort,
}


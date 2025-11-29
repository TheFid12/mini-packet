from typing import Iterable, List, Optional

__all__ = [
    "check_non_negative_int",
    "to_int_list",
    "SortingHelpers",
]


def check_non_negative_int(func):
    def wrapper(*args, **kwargs):
        if args:
            arg = args[0]
            if not isinstance(arg, int) or arg < 0:
                raise ValueError("Ошибка валидации аргументов")
        return func(*args, **kwargs)
    return wrapper


def to_int_list(values: Iterable[int]) -> List[int]:
    res = list(values)
    for x in res:
        if not isinstance(x, int):
            raise TypeError("Ожидаются целые числа")
    return res


class SortingHelpers:
    @staticmethod
    def normalize_for_bucket(nums: List[int]) -> tuple[List[float], int, int]:
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return [float(nums[0])], mn, mx
        span = mx - mn + 1
        norm = [(x - mn) / span for x in nums]
        return norm, mn, mx
    
    @staticmethod
    def denormalize_bucket(norm: List[float], mn: int, mx: int) -> List[int]:
        span = mx - mn + 1
        return [int(x * span + mn) for x in norm]
    
    @staticmethod
    def apply_sort(method: str, values: List, *, base: int, buckets: Optional[int]) -> List:
        from .constants import SORT_METHODS
        
        func = SORT_METHODS[method]
        kwargs = {}
        
        if method == "radix":
            kwargs["base"] = base
        if method == "bucket" and buckets is not None:
            kwargs["buckets"] = buckets
        
        if method == "bucket":
            if all(isinstance(x, int) for x in values):
                norm, mn, mx = SortingHelpers.normalize_for_bucket(values)
                sorted_norm = func(norm, **kwargs)
                return SortingHelpers.denormalize_bucket(sorted_norm, mn, mx)
            else:
                return func(values, **kwargs)
        
        return func(values, **kwargs)

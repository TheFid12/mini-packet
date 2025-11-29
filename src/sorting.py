from typing import Iterable, List


__all__ = [
    "bubble_sort",
    "quick_sort",
    "counting_sort",
    "radix_sort",
    "bucket_sort",
    "heap_sort",
]


def _to_int_list(values: Iterable[int]) -> List[int]:
    res = list(values)
    for x in res:
        if not isinstance(x, int):
            raise TypeError("Ожидаются целые числа")
    return res


def bubble_sort(values: Iterable[int]) -> List[int]:
    arr = _to_int_list(values)
    n = len(arr)
    for i in range(n):
        sp = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sp = True
        if not sp:
            break
    return arr


def counting_sort(values: Iterable[int]) -> List[int]:
    arr=_to_int_list(values)
    max_val = max(arr)
    cnt = [0] * (max_val + 1)
    while len(arr) > 0:
        num = arr.pop(0)
        cnt[num] += 1
    for i in range(len(cnt)):
        while cnt[i] > 0:
            arr.append(i)
            cnt[i] -= 1
    return arr


def quick_sort(values: Iterable[int]) -> List[int]:
    arr = _to_int_list(values)
    if len(arr) < 2:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        pivot = arr[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if left < j:
            stack.append((left, j))
        if i < right:
            stack.append((i, right))
    return arr


def radix_sort(values: Iterable[int], base: int = 10) -> List[int]:
    arr = _to_int_list(values)
    max_digits = max([len(str(x)) for x in arr])
    bins = [[] for _ in range(base)]
    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base 
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        print(arr)
        print(bins)
        bins = [[] for _ in range(base)]
    return arr


def bucket_sort(values: Iterable[float], buckets: int | None = None) -> List[float]:
    data = list(values)
    if not data:
        return []
    if any(not isinstance(x, (int, float)) for x in data):
        raise TypeError("Ожидаются числа")
    n = len(data)
    bcount = buckets if buckets is not None else n
    bins: List[List[float]] = [[] for _ in range(bcount)]
    for x in data:
        idx = min(int(x * bcount), bcount - 1)
        bins[idx].append(x)
    for bucket in bins:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key
    res: List[float] = []
    for bucket in bins:
        res.extend(bucket)
    return res


def heap_sort(arr: Iterable[int]) -> List[int]:
    arr = _to_int_list(arr)


    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

            
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
# mini-packet — Библиотека алгоритмов и структур данных

**Авторы:** Бычков Евгений М8О-104БВ-25
**Репозиторий:** [mini-packet](https://github.com/TheFid12/mini-packet)

## Описание проекта

Библиотека реализует базовые алгоритмы (факториал, числа Фибоначчи), алгоритмы сортировки (bubble, quick, counting, radix, bucket, heap), структуры данных (очередь через стеки, стек через очереди) и интерактивную CLI для работы с ними.

---

## Структура проекта

```
mini-packet/
├── src/
│   ├── __init__.py
│   ├── algorithms.py          # Факториал и Фибоначчи
│   ├── constants.py            # Константы (словарь методов сортировки)
│   ├── main.py                 # Точка входа, CLI команды
│   ├── sorting.py              # Алгоритмы сортировки
│   ├── structures.py           # Структуры данных
│   ├── test_generators.py      # Генераторы тест-кейсов
│   └── utils.py                # Утилиты (валидация, хелперы)
├── tests/
│   ├── __init__.py
│   ├── test_algorithms.py
│   ├── test_sorting.py
│   ├── test_sorting_generated.py  # Тесты с генераторами
│   └── test_structures.py
├── pyproject.toml              # Зависимости и конфигурация
└── README.md                   # Этот файл
```

---

### Запуск CLI

```bash
# Интерактивный режим
python -m src.main

# Прямой вызов команды
python -m src.main factorial 5
python -m src.main fibonacci 10 --recursive
python -m src.main sort bubble "5 3 8 1 2"
```

---

## Модули и функции

### `algorithms.py`
Математические алгоритмы:
- `factorial(n: int) -> int` — итеративный факториал
- `factorial_r(n: int) -> int` — рекурсивный факториал
- `fib(n: int) -> int` — итеративные числа Фибоначчи
- `fib_r(n: int) -> int` — рекурсивные числа Фибоначчи (с кешированием)

**Ограничения:** `n >= 0` (проверяется декоратором `@check_non_negative_int`)

### `sorting.py`
Алгоритмы сортировки:
- `bubble_sort(values: Iterable[int]) -> List[int]` — пузырьковая сортировка, O(n²)
- `quick_sort(values: Iterable[int]) -> List[int]` — быстрая сортировка (итеративная), O(n log n)
- `counting_sort(values: Iterable[int]) -> List[int]` — сортировка подсчётом, O(n + k)
- `radix_sort(values: Iterable[int], base: int = 10) -> List[int]` — поразрядная сортировка, O(d·n)
- `bucket_sort(values: Iterable[float], buckets: int | None = None) -> List[float]` — блочная сортировка, O(n + k)
- `heap_sort(arr: Iterable[int]) -> List[int]` — пирамидальная сортировка, O(n log n)

**Допущения и ограничения:**
- Все функции (кроме `bucket_sort`) работают с **целыми числами** (`int`)
- `bucket_sort` работает с **float**
- `radix_sort` **не поддерживает отрицательные числа** (вызовет `ValueError`)
- `counting_sort` поддерживает отрицательные числа через смещение индексов
- Пустые списки возвращают пустой список
- Входные данные преобразуются в список (можно передавать итераторы)

### `structures.py`
Структуры данных:
- **`QueueViaStacks`** — очередь через два стека
  - `enqueue(x)` — добавить элемент
  - `dequeue() -> Any` — извлечь первый элемент
  - `front() -> Any` — посмотреть первый элемент
  - `is_empty() -> bool`
  - `__len__() -> int`

- **`StackViaQueues`** — стек через две очереди
  - `push(x)` — добавить элемент
  - `pop() -> Any` — извлечь верхний элемент (O(n))
  - `peek() -> Any` — посмотреть верхний элемент (O(n))
  - `is_empty() -> bool`
  - `__len__() -> int`

**Допущения:**
- `pop()` и `peek()` в `StackViaQueues` имеют сложность O(n)
- При попытке извлечь из пустой структуры вызывается `IndexError`

### `test_generators.py`
Генераторы тестовых данных:
- `rand_int_array(n, lo, hi, *, distinct=False, seed=None)` — случайный массив целых чисел
- `nearly_sorted(n, swaps, *, seed=None)` — почти отсортированный массив
- `many_duplicates(n, k_unique=5, *, seed=None)` — массив с дубликатами
- `reverse_sorted(n)` — обратно отсортированный массив
- `rand_float_array(n, lo=0.0, hi=1.0, *, seed=None)` — случайный массив float

### `utils.py`
Вспомогательные функции:
- `check_non_negative_int(func)` — декоратор для проверки `int >= 0`
- `to_int_list(values)` — преобразование итерируемого в список `int` с проверкой типов
- **`SortingHelpers`** — утилиты для сортировки:
  - `normalize_for_bucket(nums)` — нормализация для bucket sort
  - `denormalize_bucket(norm, mn, mx)` — денормализация
  - `apply_sort(method, values, base, buckets)` — универсальный вызов сортировки

---

## CLI команды

Интерактивный режим запускается командой `python -m src.main`:

### Математика
```bash
factorial 5              # Факториал 5
factorial 10 -r          # Рекурсивный факториал
fibonacci 15             # 15-е число Фибоначчи
fibonacci 20 --recursive # Рекурсивное вычисление
```

### Сортировка
```bash
Для ввода отрицательных чисел ввесть -- после метода сортировки 
sort bubble -- 5 1 -1 32 11 
sort bubble 5 3 8 1 2     # Пузырьковая сортировка
sort quick 9 2 5 1 7        # Быстрая сортировка
sort radix 170 45 75 90   # Поразрядная сортировка
sort bucket 0.5 0.1 0.9     # Блочная (float )
```

**Сортировка стека:**
```bash
push 5
push 3
push 8
sort bubble stack         # Сортирует содержимое стека
```

### Работа со стеком
```bash
push 42          # Добавить в стек
pop              # Извлечь из стека
peek             # Посмотреть вершину
stack-size       # Размер стека
stack-show       # Показать содержимое
stack-clear      # Очистить стек
```

---

## Тестирование

### Запуск всех тестов
```bash
pytest tests/ -v
```

### Запуск конкретных тестов
```bash
pytest tests/test_sorting.py -v
pytest tests/test_sorting_generated.py -v
pytest tests/test_algorithms.py::TestFactorial -v
```

### Тесты с генераторами
Файл `tests/test_sorting_generated.py` :

---
### CLI использование

```bash
$ python -m src.main
mini-packet > factorial 10
3628800
mini-packet > push 5
+ 5
mini-packet > push 3
+ 3
mini-packet > sort bubble stack
Стек отсортирован
mini-packet > stack-show
3
5
mini-packet > exit
```

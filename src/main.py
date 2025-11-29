from typing import List, Optional
import typer
from typer_shell import make_typer_shell
from .algorithms import factorial, factorial_r, fib, fib_r
from .structures import StackViaQueues
from .constants import SORT_METHODS
from .utils import SortingHelpers


app = make_typer_shell(
    prompt="mini-packet > ",
    intro="Добро пожаловать в mini-packet! Наберите 'help' для списка команд.\n"
)

_global_stack = StackViaQueues()


def extract_stack() -> List[int]:
    items = []
    while not _global_stack.is_empty():
        items.append(_global_stack.pop())
    return items


def restore_stack(items: List[int]) -> None:
    for v in reversed(items):
        _global_stack.push(v)


@app.command("factorial")
def factorial_cmd(
    n: int,
    recursive: bool = typer.Option(False, "--recursive", "-r", help="Рекурсивная версия")
):
    result = factorial_r(n) if recursive else factorial(n)
    typer.echo(result)


@app.command("fibonacci")
def fibonacci_cmd(
    n: int,
    recursive: bool = typer.Option(False, "--recursive", "-r", help="Используя Рекурсию")
):
    result = fib_r(n) if recursive else fib(n)
    typer.echo(result)


@app.command("sort")
def sort_cmd(
    method: str = typer.Argument(..., help=f"Метод: {', '.join(SORT_METHODS)}"),
    raw_items: List[str] = typer.Argument(..., help="'stack' или список чисел"),
    base: int = typer.Option(10),
    buckets: Optional[int] = typer.Option(None),
):
    method = method.lower()
    if method not in SORT_METHODS:
        typer.echo(f"Неизвестный метод: {method}", err=True)
        raise typer.Exit(1)
    if len(raw_items) == 1 and raw_items[0].lower() == "stack":
        if _global_stack.is_empty():
            typer.echo("Стек пуст")
            return
        items = extract_stack()
        try:
            result = SortingHelpers.apply_sort(method, items, base=base, buckets=buckets)
        except Exception as exc:
            restore_stack(items)
            typer.echo(f"Ошибка сортировки: {exc}", err=True)
            raise typer.Exit(1)
        restore_stack(result)
        typer.echo("Стек отсортирован")
        return
    try:
        if method == "bucket":
            numbers = [float(x) for x in raw_items]
        else:
            numbers = [int(x) for x in raw_items]
    except ValueError:
        typer.echo("Неверный формат: введите целые числа или 'stack'", err=True)
        raise typer.Exit(1)
    try:
        result = SortingHelpers.apply_sort(method, numbers, base=base, buckets=buckets)
    except Exception as exc:
        typer.echo(f"Ошибка: {exc}", err=True)
        raise typer.Exit(1)
    typer.echo(" ".join(map(str, result)))


@app.command("push")
def push_cmd(value: int):
    _global_stack.push(value)
    typer.echo(f"+ {value}")


@app.command("pop")
def pop_cmd():
    try:
        value = _global_stack.pop()
    except IndexError:
        typer.echo("Стек пуст", err=True)
        raise typer.Exit(1)
    typer.echo(f"- {value}")


@app.command("peek")
def peek_cmd():
    try:
        value = _global_stack.peek()
    except IndexError:
        typer.echo("Стек пуст", err=True)
        raise typer.Exit(1)
    typer.echo(str(value))


@app.command("stack-size")
def stack_size_cmd():
    typer.echo(str(len(_global_stack)))


@app.command("stack-show")
def stack_show_cmd():
    if _global_stack.is_empty():
        return
    items = extract_stack()
    for val in items:
        typer.echo(val)
    restore_stack(items)


@app.command("stack-clear")
def stack_clear_cmd():
    while not _global_stack.is_empty():
        _global_stack.pop()


def main() -> None:
    app()


if __name__ == "__main__":
    main()

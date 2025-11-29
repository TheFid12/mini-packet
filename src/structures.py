from __future__ import annotations
from typing import Any, List
from collections import deque

__all__ = ["QueueViaStacks", "StackViaQueues"]

class QueueViaStacks:
    def __init__(self) -> None:
        self._in: List[Any] = []
        self._out: List[Any] = []

    def enqueue(self, x: Any) -> None:
        self._in.append(x)

    def _transfer(self) -> None:
        while self._in:
            self._out.append(self._in.pop())

    def dequeue(self) -> Any:
        if not self._out and not self._in:
            raise IndexError("dequeue из пустой очереди")
        if not self._out:
            self._transfer()
        return self._out.pop()

    def front(self) -> Any:
        if not self._out and not self._in:
            raise IndexError("front из пустой очереди")
        if not self._out:
            self._transfer()
        return self._out[-1]

    def is_empty(self) -> bool:
        return not self._out and not self._in

    def __len__(self) -> int:
        return len(self._in) + len(self._out)

class StackViaQueues:
    def __init__(self) -> None:
        self._q1: deque = deque()
        self._q2: deque = deque()

    def _enqueue(self, q: deque, x: Any) -> None:
        q.append(x)

    def _dequeue(self, q: deque) -> Any:
        if not q:
            raise IndexError("Очередь пуста")
        return q.popleft()

    def push(self, x: Any) -> None:
        self._enqueue(self._q1, x)

    def pop(self) -> Any:
        if not self._q1:
            raise IndexError("pop из пустого стека")
        while len(self._q1) > 1:
            self._enqueue(self._q2, self._dequeue(self._q1))
        top = self._dequeue(self._q1)
        self._q1, self._q2 = self._q2, self._q1
        self._q2.clear()
        return top

    def peek(self) -> Any:
        if not self._q1:
            raise IndexError("peek из пустого стека")
        while len(self._q1) > 1:
            self._enqueue(self._q2, self._dequeue(self._q1))
        top = self._dequeue(self._q1)
        self._enqueue(self._q2, top)
        self._q1, self._q2 = self._q2, self._q1
        self._q2.clear()
        return top

    def is_empty(self) -> bool:
        return not self._q1

    def __len__(self) -> int:
        return len(self._q1)

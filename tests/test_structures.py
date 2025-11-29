import pytest
from src.structures import QueueViaStacks, StackViaQueues


class TestQueueViaStacks:
    """Тесты для очереди через два стека."""

    def test_enqueue_dequeue(self):
        """Тест базовой работы очереди."""
        queue = QueueViaStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3

    def test_fifo_order(self):
        """Тест что очередь работает в порядке FIFO."""
        queue = QueueViaStacks()
        for i in range(10):
            queue.enqueue(i)
        
        for i in range(10):
            assert queue.dequeue() == i

    def test_front(self):
        """Тест метода front."""
        queue = QueueViaStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        
        assert queue.front() == 1
        assert queue.front() == 1  # front не удаляет элемент
        assert queue.dequeue() == 1

    def test_is_empty(self):
        """Тест метода is_empty."""
        queue = QueueViaStacks()
        assert queue.is_empty()
        
        queue.enqueue(1)
        assert not queue.is_empty()
        
        queue.dequeue()
        assert queue.is_empty()

    def test_len(self):
        """Тест метода __len__."""
        queue = QueueViaStacks()
        assert len(queue) == 0
        
        queue.enqueue(1)
        queue.enqueue(2)
        assert len(queue) == 2
        
        queue.dequeue()
        assert len(queue) == 1

    def test_dequeue_empty_raises(self):
        """Тест что dequeue из пустой очереди вызывает ошибку."""
        queue = QueueViaStacks()
        with pytest.raises(IndexError):
            queue.dequeue()

    def test_front_empty_raises(self):
        """Тест что front из пустой очереди вызывает ошибку."""
        queue = QueueViaStacks()
        with pytest.raises(IndexError):
            queue.front()

    def test_mixed_operations(self):
        """Тест смешанных операций enqueue/dequeue."""
        queue = QueueViaStacks()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4


class TestStackViaQueues:
    """Тесты для стека через две очереди."""

    def test_push_pop(self):
        """Тест базовой работы стека."""
        stack = StackViaQueues()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_lifo_order(self):
        """Тест что стек работает в порядке LIFO."""
        stack = StackViaQueues()
        for i in range(10):
            stack.push(i)
        
        for i in range(9, -1, -1):
            assert stack.pop() == i

    def test_peek(self):
        """Тест метода peek."""
        stack = StackViaQueues()
        stack.push(1)
        stack.push(2)
        
        assert stack.peek() == 2
        assert stack.peek() == 2  # peek не удаляет элемент
        assert stack.pop() == 2

    def test_is_empty(self):
        """Тест метода is_empty."""
        stack = StackViaQueues()
        assert stack.is_empty()
        
        stack.push(1)
        assert not stack.is_empty()
        
        stack.pop()
        assert stack.is_empty()

    def test_len(self):
        """Тест метода __len__."""
        stack = StackViaQueues()
        assert len(stack) == 0
        
        stack.push(1)
        stack.push(2)
        assert len(stack) == 2
        
        stack.pop()
        assert len(stack) == 1

    def test_pop_empty_raises(self):
        """Тест что pop из пустого стека вызывает ошибку."""
        stack = StackViaQueues()
        with pytest.raises(IndexError):
            stack.pop()

    def test_peek_empty_raises(self):
        """Тест что peek из пустого стека вызывает ошибку."""
        stack = StackViaQueues()
        with pytest.raises(IndexError):
            stack.peek()

    def test_mixed_operations(self):
        """Тест смешанных операций push/pop."""
        stack = StackViaQueues()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        
        stack.push(3)
        stack.push(4)
        assert stack.pop() == 4
        assert stack.pop() == 3
        assert stack.pop() == 1

    def test_different_types(self):
        """Тест работы с разными типами данных."""
        stack = StackViaQueues()
        stack.push("hello")
        stack.push(42)
        stack.push([1, 2, 3])
        
        assert stack.pop() == [1, 2, 3]
        assert stack.pop() == 42
        assert stack.pop() == "hello"


class TestStructuresInteraction:
    """Тесты взаимодействия структур данных."""

    def test_queue_and_stack_independence(self):
        """Тест что очередь и стек работают независимо."""
        queue = QueueViaStacks()
        stack = StackViaQueues()
        
        # Добавляем одинаковые данные
        for i in range(5):
            queue.enqueue(i)
            stack.push(i)
        
        # Очередь должна вернуть в порядке FIFO
        assert queue.dequeue() == 0
        
        # Стек должен вернуть в порядке LIFO
        assert stack.pop() == 4

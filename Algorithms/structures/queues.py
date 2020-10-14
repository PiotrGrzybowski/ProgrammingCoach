from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, Optional

from structures.types import T


class AbstractQueue(ABC, Generic[T]):
    @abstractmethod
    def push(self, element: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def front(self) -> T:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class FifoQueue(AbstractQueue[T]):
    class EmptyQueueError(Exception):
        def __init__(self):
            super().__init__('You can not pop from empty Queue')

    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[FifoQueue.Node] = None

    def __init__(self, *args: T) -> None:
        self.head = None
        self.tail = None

        self._push_init_elements(args)

    def push(self, element: T) -> None:
        node = FifoQueue.Node(element)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def front(self) -> T:
        return self.head.value

    def pop(self) -> T:
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise FifoQueue.EmptyQueueError()

    def __str__(self) -> str:
        result = ''
        pointer = self.head
        while pointer:
            result += str(pointer.value)
            pointer = pointer.next
            if pointer:
                result += ' <- '
        return f'[{result}]'

    def _push_init_elements(self, args):
        if args:
            for element in args:
                self.push(element)


class Stack(AbstractQueue[T]):
    class EmptyStackError(Exception):
        def __init__(self):
            super().__init__('You can not pop from empty Stack')

    @dataclass
    class Node(Generic[T]):
        value: T
        next: Optional[Stack.Node] = None

    def __init__(self, *args: T) -> None:
        self.head = None
        self._push_init_elements(args)

    def push(self, element: T) -> None:
        node = FifoQueue.Node(element)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def front(self) -> T:
        return self.head.value

    def pop(self) -> T:
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise Stack.EmptyStackError()

    def __str__(self) -> str:
        result = ''
        pointer = self.head
        while pointer:
            result += str(pointer.value)
            pointer = pointer.next
            if pointer:
                result += ' -> '
        return f'[{result}]'

    def _push_init_elements(self, args):
        if args:
            for element in args:
                self.push(element)

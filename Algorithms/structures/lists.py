from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, Optional, Any, Iterator

from structures.types import T


class List(ABC, Generic[T]):
    @abstractmethod
    def append(self, element: T) -> None:
        pass

    @abstractmethod
    def remove(self, element: T) -> T:
        pass

    @abstractmethod
    def pop(self, index: int) -> T:
        pass

    @abstractmethod
    def index(self, element: T) -> int:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def length(self) -> int:
        pass

    @abstractmethod
    def contains(self, element: T) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other: List[T]) -> bool:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    @abstractmethod
    def __setitem__(self, index: int, value: T) -> T:
        pass

    # @abstractmethod
    # def __iter__(self) -> Iterator[T]:
    #     pass

    def __len__(self):
        return self.length()

    def __contains__(self, element: T) -> bool:
        return self.contains(element)


class LinkedList(List[T]):
    class Node(Generic[T]):
        def __init__(self, value: T, next_node: Optional[LinkedList.Node] = None):
            self.value = value
            self.next = next_node

    def __init__(self, *args: T) -> None:
        self.head = None
        if args:
            for element in args:
                self.append(element)

    def __str__(self) -> str:
        result = ''
        pointer = self.head
        while pointer:
            result += str(pointer.value)
            pointer = pointer.next
            if pointer:
                result += ', '
        return f'[{result}]'

    def length(self) -> int:
        result = 0
        pointer = self.head
        while pointer:
            result += 1
            pointer = pointer.next
        return result

    def clear(self) -> None:
        self.head = None

    def append(self, element: T) -> None:
        if self.head is None:
            self.head = LinkedList.Node(element)
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next

            pointer.next = LinkedList.Node(element)

    def __getitem__(self, index: int) -> T:
        i = 0
        pointer = self.head

        while pointer is not None and i < index:
            pointer = pointer.next
            i += 1

        if pointer is not None and i == index:
            return pointer.value
        else:
            raise IndexError(f'pop index out of range')

    def __setitem__(self, index: int, value: T) -> None:
        i = 0
        pointer = self.head

        while pointer is not None and i < index:
            pointer = pointer.next
            i += 1

        if pointer is not None and i == index:
            pointer.value = value
        else:
            raise IndexError(f'pop index out of range')

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, LinkedList):
            return False
        else:
            pointer = self.head
            other_pointer = other.head

            while pointer is not None and other_pointer is not None and pointer.value == other_pointer.value:
                pointer = pointer.next
                other_pointer = other_pointer.next

            return pointer is None and other_pointer is None

    def index(self, element: T) -> int:
        result = -1
        pointer = self.head
        index = 0
        while pointer and result == -1:
            if pointer.value == element:
                result = index
            pointer = pointer.next
            index += 1

        if result == -1:
            raise ValueError(f'{str(element)} is not in list')
        else:
            return result

    def contains(self, element: T) -> bool:
        try:
            return self.index(element) > -1
        except ValueError:
            return False

    def pop(self, index: int) -> T:
        result = None
        if self.head is not None:
            if index == 0:
                result = self.head.value
                self.head = self.head.next
            else:
                i = 1
                current = self.head.next
                previous = self.head

                while current is not None and i < index:
                    previous = current
                    current = current.next
                    i += 1

                if i == index and current is not None:
                    previous.next = current.next
                    result = current.value
                else:
                    raise IndexError(f'pop index out of range')
        return result

    def remove(self, element: T) -> T:
        result = None
        if self.head is not None:
            if self.head.value == element:
                result = self.head.value
                self.head = self.head.next
            else:
                current = self.head.next
                previous = self.head

                while current is not None and current.value != element:
                    previous = current
                    current = current.next

                if current is not None and current.value == element:
                    previous.next = current.next
                    result = current.value
                else:
                    raise ValueError(f'{str(element)} not in list')
        return result

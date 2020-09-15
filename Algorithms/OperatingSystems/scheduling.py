from abc import ABC, abstractmethod

from typing import TypeVar, List, Generic

T = TypeVar('T')


class EmptyQueueError(Exception):
    def __init__(self):
        super().__init__('You can not pop from empty Queue')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.values: List[T] = []

    def push(self, value: T) -> None:
        self.values.append(value)

    def pop(self) -> T:
        if self.values:
            return self.values.pop(0)
        else:
            raise EmptyQueueError()

    def front(self) -> T:
        return self.values[0]

    def __str__(self) -> str:
        return str(self.values)

    def __len__(self) -> int:
        return len(self.values)


class ProcessQueue(Queue, ABC):
    @abstractmethod
    def go(self):
        pass

class SchedulingAlgorithm(ABC):
    pass


class Scheduler(ABC):
    pass


class FirstComeFirstServed(Scheduler):
    pass


class ShortestJobFirst(Scheduler):
    pass

a = ProcessQueue()
import heapq
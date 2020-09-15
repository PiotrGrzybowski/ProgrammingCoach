from enum import Enum


class State(Enum):
    READY = 0
    RUN = 1
    COMPLETED = 2
    BLOCKED = 3


class Process:
    def __init__(self, duration: int) -> None:
        self.duration = duration
        self.state = State.READY
        self.performed = 0

    def execute_step(self):
        self.performed += 1
        self._check_completion()

    def _check_completion(self):
        if self.performed >= self.duration:
            self.state = State.COMPLETED

    def _block(self) -> None:
        self.state = State.BLOCK

    def _run(self) -> None:
        self.state = State.RUN

    def _complete(self) -> None:
        self.state = State.COMPLETED

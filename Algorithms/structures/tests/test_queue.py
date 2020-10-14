from unittest import TestCase, main

from structures.queues import FifoQueue


class TestQueue(TestCase):
    def test_push(self):
        queue = FifoQueue[int]()

        queue.push(1)
        queue.push(2)
        queue.push(3)

        self.assertEqual(queue.head.value, 1)
        self.assertEqual(queue.head.next.value, 2)
        self.assertEqual(queue.head.next.next.value, 3)

    def test_push_init_elements(self):
        queue = FifoQueue[int](1, 2, 3)

        self.assertEqual(queue.head.value, 1)
        self.assertEqual(queue.head.next.value, 2)
        self.assertEqual(queue.head.next.next.value, 3)

    def test_front(self):
        queue = FifoQueue[int](1, 2, 3)

        self.assertEqual(queue.front(), 1)

    def test_pop_queue_with_elements(self):
        queue = FifoQueue[int](1, 2, 3)

        popped = queue.pop()

        self.assertEqual(popped, 1)
        self.assertEqual(queue.head.value, 2)
        self.assertEqual(queue.head.next.value, 3)

    def test_pop_empty_queue(self):
        queue = FifoQueue[int]()

        self.assertRaises(FifoQueue.EmptyQueueError, queue.pop)


if __name__ == '__main__':
    main()
